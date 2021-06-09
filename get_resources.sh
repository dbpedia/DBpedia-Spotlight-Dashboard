#!/bin/bash

BASE_DIR=$(pwd)
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
EN="en"
DATASETS="dbpedia_datasets"
WIKISTATS="wikistats"
DASHBOARD="dashboard_data"


########################################################################################################
# DBpedia extraction:
########################################################################################################

function download_dbpedia_datasets {
	cd $1/$DATASETS
	echo "Downloading DBpedia datasets for $1 language:
* https://databus.dbpedia.org/dbpedia/generic/disambiguations
* https://databus.dbpedia.org/dbpedia/generic/redirects
* https://databus.dbpedia.org/dbpedia/mappings/instance-types
Note of deviation from original index_db.sh: 
takes the direct AND transitive version of redirects and instance-types and the redirected version of disambiguation 
"

	QUERY="PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dataid: <http://dataid.dbpedia.org/ns/core#>
PREFIX dataid-cv: <http://dataid.dbpedia.org/ns/cv#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
SELECT  ?file WHERE {
    { 
    # Subselect latestVersion by artifact
    SELECT  ?artifact (max(?version) as ?latestVersion)  WHERE {
            ?dataset dataid:artifact ?artifact .
            ?dataset dct:hasVersion ?version
            FILTER (?artifact in (
		        # GENERIC 
                <https://databus.dbpedia.org/dbpedia/generic/disambiguations> ,
                <https://databus.dbpedia.org/dbpedia/generic/redirects> ,
                # MAPPINGS
          	    <https://databus.dbpedia.org/dbpedia/mappings/instance-types>
             	# latest ontology, currently @denis account
          		# TODO not sure if needed for Spotlight
                # <https://databus.dbpedia.org/denis/ontology/dbo-snapshots>
             )) .
             }GROUP BY ?artifact 
	} 
  		
    ?dataset dct:hasVersion ?latestVersion .
    {
          ?dataset dataid:artifact ?artifact .
          ?dataset dcat:distribution ?distribution .
          ?distribution dcat:downloadURL ?file .
          ?distribution dataid:contentVariant '$1'^^xsd:string .
          # remove debug info	
          MINUS {
               ?distribution dataid:contentVariant ?variants . 
               FILTER (?variants in ('disjointDomain'^^xsd:string, 'disjointRange'^^xsd:string))
          }  		
    }   
} ORDER by ?artifact
"

	# execute query and trim " and first line from result set
	RESULT=`curl --data-urlencode query="$QUERY" --data-urlencode format="text/tab-separated-values" https://databus.dbpedia.org/repo/sparql | sed 's/"//g' | grep -v "^file$" `

	# Download
	TMPDOWN="dump-tmp-download"
	mkdir $TMPDOWN 
	cd $TMPDOWN
	for i in $RESULT
		do  
				wget $i 
				ls
				echo $TMPDOWN
				pwd
		done
		
	cd ..

	echo "decompressing"
	bzcat -v $TMPDOWN/instance-types*.ttl.bz2 > $RESOURCES_DIR/$1/$DATASETS/instance_types.nt
	bzcat -v $TMPDOWN/disambiguations*.ttl.bz2 > $RESOURCES_DIR/$1/$DATASETS/disambiguations.nt
	bzcat -v $TMPDOWN/redirects*.ttl.bz2 > $RESOURCES_DIR/$1/$DATASETS/redirects.nt

	# clean
	rm -r $TMPDOWN
	
	echo "splitting" 
	split -l 500000 instance_types.nt instance_types_
	# split -l 500000 disambiguations.nt disambiguations_
	# split -l 500000 redirects.nt redirects_
	
	echo "filtering"
	sed -i -n '/http:\/\/dbpedia.org\/ontology\//p' instance_types_*
	echo "done"
	
	# echo "Separating valid and invalid URLs of all files:"
	# for file in test_*
	# do
		# sh ./check_url_file.sh $file &
	# done
	# wait

	echo "counting types"
	# cat invalid_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' > invalid_types.tsv 
	# cat valid_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' > valid_types.tsv 
	# sed -i 's%http://dbpedia.org/ontology/%%g' invalid_types.tsv
	# sed -i 's%http://dbpedia.org/ontology/%%g' valid_types.tsv
	
	cat instance_types_* | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' > types.tsv 
	sed -i 's%http://dbpedia.org/ontology/%%g' types.tsv
	
	rm instance_types_* 
	# rm disambiguations.nt
	# rm redirects.nt
	
	echo "Done"
	
	mv *.tsv $RESOURCES_DIR/$1/$DASHBOARD
	cd ..
}

function download_wikistats {
	cd $WIKISTATS
	echo "Downloading Wikipedia statistics for $1 language"
	QUERY="PREFIX dataid: <http://dataid.dbpedia.org/ns/core#>
PREFIX dct:    <http://purl.org/dc/terms/>
PREFIX dcat:   <http://www.w3.org/ns/dcat#>
PREFIX db:     <https://databus.dbpedia.org/>
PREFIX rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?file WHERE {
	GRAPH ?g {
		?dataset dcat:distribution ?distribution .
		?distribution dataid:file ?file .
		?dataset dataid:artifact <https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats> .
		{
			?distribution dct:hasVersion ?version {
				SELECT (?v as ?version) { 
					?dataset dataid:artifact <https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats> . 
					?dataset dct:hasVersion ?v . 
				} ORDER BY DESC (?version) LIMIT 1 
			}
		}
		{ ?distribution <http://dataid.dbpedia.org/ns/cv#lang> '$1'^^<http://www.w3.org/2001/XMLSchema#string> . }
	}
}"
	
	# execute query and trim " and first line from result set
	RESULT=`curl --data-urlencode query="$QUERY" --data-urlencode format="text/tab-separated-values" https://databus.dbpedia.org/repo/sparql | sed 's/"//g' | grep -v "^file$" `
	
	# Download
	TMPDOWN="dump-tmp-download"
	mkdir $TMPDOWN 
	cd $TMPDOWN
	for i in $RESULT
		do  
				wget $i 
				ls
				echo $TMPDOWN
				pwd
		done
		
	cd ..

	echo "decompressing"
	bzcat -v $TMPDOWN/*pairCounts*.tsv.bz2 > $RESOURCES_DIR/$1/$WIKISTATS/pairCounts
	bzcat -v $TMPDOWN/*uriCounts*.tsv.bz2 > $RESOURCES_DIR/$1/$WIKISTATS/uriCounts
	bzcat -v $TMPDOWN/*sfAndTotalCounts*.tsv.bz2 > $RESOURCES_DIR/$1/$WIKISTATS/sfAndTotalCounts
	bzcat -v $TMPDOWN/*tokenCounts*.tsv.bz2 > $RESOURCES_DIR/$1/$WIKISTATS/tokenCounts

	# clean
	rm -r $TMPDOWN
	
	echo "splitting" 
	# split -l 500000 pairCounts pairCounts_
	split -l 500000 uriCounts uriCounts_
	# split -l 500000 sfAndTotalCounts sfAndTotalCounts_
	# split -l 500000 tokenCounts tokenCounts_
	
	mv uriCounts_* $RESOURCES_DIR/$1/$DASHBOARD
	
	# rm pairCounts
	# rm uriCounts
	# rm sfAndTotalCounts
	# rm tokenCounts
	
	cd $RESOURCES_DIR
}

if [ -d "$RESOURCES_DIR" ]; then
	read -p "Do you want to download DBpedia Databus resources again? [y/n] " download
	if [[ $download == [yY] ]]; then
		cd $RESOURCES_DIR
		echo "Downloading resources"
		download_dbpedia_datasets "$ES"
		download_wikistats "$ES"
	fi
else
	echo "Making resources folder"
	mkdir -p $RESOURCES_DIR
	cd $RESOURCES_DIR
	echo "Making languages folder"
	mkdir -p $ES/$DATASETS
	mkdir -p $ES/$WIKISTATS
	mkdir -p $ES/$DASHBOARD
	mkdir -p $EN/$DATASETS
	mkdir -p $EN/$WIKISTATS
	mkdir -p $EN/$DASHBOARD
	echo "Downloading resources"
	download_dbpedia_datasets "$ES"
	download_wikistats "$ES"
	download_dbpedia_datasets "$EN"
	download_wikistats "$EN"
fi

echo "Done"







