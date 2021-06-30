#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
EN="en"
DATASETS="dbpedia_datasets"
WIKISTATS="wikistats"
DASHBOARD="dashboard_data"

function file_urls {
	while read line;
			do
				resource=$(echo $line | cut -d ' ' -f 1)
				answer=$(curl -s http://localhost:8890/sparql --data-urlencode "query=
			SELECT COUNT(?type) AS ?count WHERE
{
OPTIONAL {<$resource> <http://dbpedia.org/ontology/wikiPageDisambiguates> ?resource. ?resource a ?type. FILTER 
regex(?type,'dbpedia.org','i')
}
OPTIONAL {<$resource> <http://dbpedia.org/ontology/wikiPageRedirects> ?resource. ?resource a ?type. FILTER 
regex(?type,'dbpedia.org','i')
}
OPTIONAL {<$resource> a ?type. FILTER regex(?type,'dbpedia.org','i')
}
}" --data-urlencode "format=text/csv")
				count=$(echo $answer | cut -d ' ' -f 2)
				if [ "$count" != "0" ]
				then
					echo $resource >> valid_urls
				else
					echo $resource >> invalid_urls
				fi
			done < $1
	echo "$1 URLs file completed"
}

function file_types {
	while read line;
		do
			answer=$(curl -s http://localhost:8890/sparql --data-urlencode "query=
			SELECT  DISTINCT ?type WHERE {
<$line> a ?type.
FILTER regex(?type,'dbpedia.org','i')
}" --data-urlencode "format=text/csv")
			type=$(echo $answer | cut -d ' ' -f 2- | sed s/\"//g | grep -v type)
			echo $type >> valid_instance_types
		done < $1
	echo "$1 valid URLs file completed"
}


function validate_urls {
	cd $RESOURCES_DIR/$1/$WIKISTATS
	echo "Splitting" 
	split -l 500000 uriCounts uriCounts_
	echo "Separating valid and invalid URLs for $1 language of all files:"
	for file in uriCounts_*
	do
	file_urls "$file" &	
	done
	echo "Waiting for all to complete"
	wait
	rm uriCounts_*
	mv *id_urls* $RESOURCES_DIR/$1/$DASHBOARD
	cd $RESOURCES_DIR/$1/$DASHBOARD
	split -l 250000 valid_urls valid_urls_
	echo "Done"
}

function validate_types {
	cd $RESOURCES_DIR/$1/$DASHBOARD
	echo "Getting valid types for $1 language"
	for file in valid_urls_*
	do
	file_types "$file" &	
	done
	echo "Waiting for all to complete"
	wait
	echo "Done"
	cat valid_instance_types | grep "http://dbpedia.org/ontology/" |tr " " "\n" > valid_types
	echo "Done"

	echo "counting types"
	cat valid_types | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' |  grep -v "^ "  > valid_types.tsv 
	sed -i 's%http://dbpedia.org/ontology/%%g' valid_types.tsv
	
	rm valid_instance_types
    rm valid_types
	rm valid_urls_*
	
	echo "Done"
}

validate_urls "$ES"
validate_types "$ES"
validate_urls "$EN"
validate_types "$EN"

echo "Done"
