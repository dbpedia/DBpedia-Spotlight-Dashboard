#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
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
	echo "Downloading latest version of DBpedia datasets for $1 language:
* https://databus.dbpedia.org/dbpedia/generic/disambiguations
* https://databus.dbpedia.org/dbpedia/generic/redirects
* https://databus.dbpedia.org/dbpedia/mappings/instance-types
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
	
	cd $RESOURCES_DIR
}

function download_wikistats {
	cd $1/$WIKISTATS
	echo "Downloading latest version of Wikipedia statistics for $1 language"
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
	cd $RESOURCES_DIR
}

function split_files {
    cd $RESOURCES_DIR/$1/$WIKISTATS
	echo "Splitting files"
	split -l 250000 uriCounts uriCounts_
	split -l 250000 pairCounts pairCounts_
	split -l 250000 sfAndTotalCounts sfAndTotalCounts_
	echo "Filtering"
	if [ "$1" = "$ES" ]
	then
		for i in *Counts_*; do
			sed -i 's%http://es.dbpedia.org/resource/%%g' $i
		done
	else
		for i in *Counts_*; do
			sed -i 's%http://dbpedia.org/resource/%%g' $i
		done
	fi
	mv *Counts_* $RESOURCES_DIR/$1/$DASHBOARD
}

if [ -d "$RESOURCES_DIR/$ES/$DATASETS" ]; then
	read -p "Do you want to download DBpedia Databus resources again? [y/n] " download_dbpedia
	if [[ $download_dbpedia == [yY] ]]; then
		cd $RESOURCES_DIR
		echo "Downloading..."
		download_dbpedia_datasets "$ES"
		download_dbpedia_datasets "$EN"
	fi
else
	cd $RESOURCES_DIR
	mkdir -p $ES/$DATASETS
	mkdir -p $EN/$DATASETS
	echo "Downloading resources"
	download_dbpedia_datasets "$ES"
	download_dbpedia_datasets "$EN"
fi
if [ -d "$RESOURCES_DIR/$ES/$WIKISTATS" ]; then
	read -p "Do you want to download DBpedia Databus wikipedia statistics again? [y/n] " download_wikistats
	if [[ $download_wikistats == [yY] ]]; then
		cd $RESOURCES_DIR
		echo "Downloading..."
		download_wikistats "$ES"
		download_wikistats "$EN"
	fi
else
	cd $RESOURCES_DIR
	mkdir -p $ES/$WIKISTATS
	mkdir -p $EN/$WIKISTATS
	download_wikistats "$ES"
	download_wikistats "$EN"
fi
split_files "$ES"
split_files "$EN"
echo "Done"
