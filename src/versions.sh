#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
EN="en"
_2016_10_01="2016.10.01"
_2020_10_01="2020.10.01"
_2021_05_01="2021.05.01"
_2021_06_01="2021.06.01"
VERSIONS="instance_types_versions"
DASHBOARD="dashboard_data"


########################################################################################################
# DBpedia extraction:
########################################################################################################

function download_versions {
	cd $1/$VERSIONS
	echo "Downloading DBpedia instance-types versions:
* https://databus.dbpedia.org/dbpedia/mappings/instance-types
"

	QUERY="PREFIX dataid: <http://dataid.dbpedia.org/ns/core#>
PREFIX dct:    <http://purl.org/dc/terms/>
PREFIX dcat:   <http://www.w3.org/ns/dcat#>
PREFIX db:     <https://databus.dbpedia.org/>
PREFIX rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?file WHERE {
	GRAPH ?g {
		?dataset dcat:distribution ?distribution .
		?distribution dataid:file ?file .
		?dataset dataid:artifact <https://databus.dbpedia.org/dbpedia/mappings/instance-types> .
		{ ?distribution <http://dataid.dbpedia.org/ns/cv#lang> '$1'^^<http://www.w3.org/2001/XMLSchema#string> . }
		{ ?distribution <http://purl.org/dc/terms/hasVersion> '$2'^^<http://www.w3.org/2001/XMLSchema#string> . }
	}
}
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
	bzcat -v $TMPDOWN/instance-types*.ttl.bz2 > $RESOURCES_DIR/$1/$VERSIONS/$2/instance_types.nt
	# clean
	rm -r $TMPDOWN
	cd $RESOURCES_DIR
}

function versions_statistics {
	cd $RESOURCES_DIR
	INSTANCE_TYPES_FILE=$RESOURCES_DIR/$1/$VERSIONS/$2/instance_types.nt
	echo "Language: $1 | Version: $2" >> versions_statistics.txt
	echo "" >> versions_statistics.txt
	echo "Filtering"
	cat $INSTANCE_TYPES_FILE | grep "http://dbpedia.org/ontology/" > filtered_instance_types
	INSTANCE_TYPES_LINES=$(cat filtered_instance_types | awk -F ' ' '{print $1}' | sort | uniq | wc -l)
	echo "DBpedia Extraction Framework instance-types" >> versions_statistics.txt
	echo "-------------------------------------" >> versions_statistics.txt
	echo "Number of DBpedia entities (without counting repetitions): $INSTANCE_TYPES_LINES" >> versions_statistics.txt
	echo "Getting number of resources for each DBpedia type"
	cat filtered_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' >> instance_types
	sed -i 's%http://dbpedia.org/ontology/%%g' instance_types
	INSTANCE_TYPES_TSV_LINES=$(cat instance_types | wc -l)
	echo "Number of DBpedia types: $INSTANCE_TYPES_TSV_LINES" >> versions_statistics.txt
	echo "" >> versions_statistics.txt
    rm filtered_instance_types
	rm instance_types
}

if [ -d "$RESOURCES_DIR/$ES/$VERSIONS" ]; then
	read -p "Do you want to download DBpedia instance-types versions again? [y/n] " download_versions
	if [[ $download_versions == [yY] ]]; then
		cd $RESOURCES_DIR
		echo "Downloading..."
		download_versions "$ES" "$_2016_10_01"
		download_versions "$ES" "$_2020_10_01"
		download_versions "$ES" "$_2021_05_01"
		download_versions "$ES" "$_2021_06_01"
		download_versions "$EN" "$_2016_10_01"
		download_versions "$EN" "$_2020_10_01"
		download_versions "$EN" "$_2021_05_01"
		download_versions "$EN" "$_2021_06_01"
	fi
else
	cd $RESOURCES_DIR
	mkdir -p $ES/$VERSIONS/$_2016_10_01
	mkdir -p $ES/$VERSIONS/$_2020_10_01
	mkdir -p $ES/$VERSIONS/$_2021_05_01
	mkdir -p $ES/$VERSIONS/$_2021_06_01
	mkdir -p $EN/$VERSIONS/$_2016_10_01
	mkdir -p $EN/$VERSIONS/$_2020_10_01
	mkdir -p $EN/$VERSIONS/$_2021_05_01
	mkdir -p $EN/$VERSIONS/$_2021_06_01
	echo "Downloading versions"
	download_versions "$ES" "$_2016_10_01"
	download_versions "$ES" "$_2020_10_01"
	download_versions "$ES" "$_2021_05_01"
	download_versions "$ES" "$_2021_06_01"
	download_versions "$EN" "$_2016_10_01"
	download_versions "$EN" "$_2020_10_01"
	download_versions "$EN" "$_2021_05_01"
	download_versions "$EN" "$_2021_06_01"
fi
echo "Calculating versions statistics"
if [ -f $RESOURCES_DIR/versions_statistics.txt ]; then
	rm $RESOURCES_DIR/versions_statistics.txt
fi
versions_statistics "$ES" "$_2016_10_01"
versions_statistics "$ES" "$_2020_10_01"
versions_statistics "$ES" "$_2021_05_01"
versions_statistics "$ES" "$_2021_06_01"
versions_statistics "$EN" "$_2016_10_01"
versions_statistics "$EN" "$_2020_10_01"
versions_statistics "$EN" "$_2021_05_01"
versions_statistics "$EN" "$_2021_06_01"
echo "Done"
