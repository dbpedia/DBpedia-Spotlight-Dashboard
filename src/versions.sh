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

function check {
REQUIRED_PKG=$1
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG 
fi
}


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
	cd $RESOURCES_DIR/versions
	INSTANCE_TYPES_FILE=$RESOURCES_DIR/$1/$VERSIONS/$2/instance_types.nt
	echo "Language -> $1 | Version -> $2" >> versions_statistics.txt
	echo "" >> versions_statistics.txt
	echo "Filtering"
	cat $INSTANCE_TYPES_FILE | grep "http://dbpedia.org/ontology/" > filtered_instance_types
	INSTANCE_TYPES_LINES=$(cat filtered_instance_types | awk -F ' ' '{print $1}' | sort | uniq | wc -l)
	echo "DBpedia Extraction Framework instance-types" >> versions_statistics.txt
	echo "-------------------------------------" >> versions_statistics.txt
	echo "Getting number of resources for each DBpedia type"
	cat filtered_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' >> instance_types_$1_$2
	sed -i 's%http://dbpedia.org/ontology/%%g' instance_types_$1_$2
	INSTANCE_TYPES_TSV_LINES=$(cat instance_types_$1_$2_without_repetitions | wc -l)
	echo "Calculating stats of instance_types_$1_$2 URLs" 
	cat "instance_types_$1_$2_without_repetitions" | cut -f 2 -d$' ' | datamash mean 1 pvar 1 sum 1 > temp.txt
	MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
	MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
	VAR=$(awk -F '\t' '{ print $2 }' temp.txt)
	VAR=$(echo 'print(round('$VAR',2))' | python3 )
	STDDEV=$(bc <<< "scale=2; sqrt($VAR)")
	SUM=$(awk -F '\t' '{ print $3 }' temp.txt)
	MEDIAN=$(echo 'print( ('$SUM' + 1) / 2 )' | python3 )
	echo "Number of DBpedia entities (without counting repetitions): $SUM" >> versions_statistics.txt
	echo "Number of DBpedia types: $INSTANCE_TYPES_TSV_LINES" >> versions_statistics.txt
	echo "Calculating position measures"
	Q1=$(echo 'print( ('$SUM' + 1) / 4 )' | python3 )
	Q3=$(echo 'print( 3 * ('$SUM' + 1) / 4 )' | python3 )
	PERC10=$(echo 'print(round(('$SUM' * 0.1)))' | python3 )
	PERC20=$(echo 'print(round(('$SUM' * 0.2)))' | python3 )
	PERC30=$(echo 'print(round(('$SUM' * 0.3)))' | python3 )
	PERC40=$(echo 'print(round(('$SUM' * 0.4)))' | python3 )
	PERC50=$(echo 'print( ('$SUM' + 1) / 2 )' | python3 )
	PERC60=$(echo 'print(round(('$SUM' * 0.6)))' | python3 )
	PERC70=$(echo 'print(round(('$SUM' * 0.7)))' | python3 )
	PERC80=$(echo 'print(round(('$SUM' * 0.8)))' | python3 )
	PERC90=$(echo 'print(round(('$SUM' * 0.9)))' | python3 )
	PERC95=$(echo 'print(round(('$SUM' * 0.95)))' | python3 )
	echo "Mean number of DBpedia entities per type: $MEAN" >> versions_statistics.txt
	echo "Median number of DBpedia entities per type (occurrences): $MEDIAN" >> versions_statistics.txt
	echo "Population standard deviation of DBpedia entities per type: $STDDEV" >> versions_statistics.txt
	echo "Number of DBpedia entities with DBpedia types (for checking quartiles and percentiles): $SUM" >> versions_statistics.txt
	echo "First quartile value of DBpedia entities per type: $Q1" >> versions_statistics.txt
	echo "Third quartile value of DBpedia entities per type: $Q3" >> versions_statistics.txt
	echo "10th percentile value of DBpedia entities per type: $PERC10" >> versions_statistics.txt
	echo "20th percentile value of DBpedia entities per type: $PERC20" >> versions_statistics.txt
	echo "30th percentile value of DBpedia entities per type: $PERC30" >> versions_statistics.txt
	echo "40th percentile value of DBpedia entities per type: $PERC40" >> versions_statistics.txt
	echo "50th percentile value of DBpedia entities per type: $PERC50" >> versions_statistics.txt
	echo "60th percentile value of DBpedia entities per type: $PERC60" >> versions_statistics.txt
	echo "70th percentile value of DBpedia entities per type: $PERC70" >> versions_statistics.txt
	echo "80th percentile value of DBpedia entities per type: $PERC80" >> versions_statistics.txt
	echo "90th percentile value of DBpedia entities per type: $PERC90" >> versions_statistics.txt
	echo "95th percentile value of DBpedia entities per type: $PERC95" >> versions_statistics.txt
	echo "" >> versions_statistics.txt
    rm filtered_instance_types
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

check "python3"
check "datamash"
echo "Calculating versions statistics"
if [ -f $RESOURCES_DIR/versions/versions_statistics.txt ]; then
	rm $RESOURCES_DIR/versions/versions_statistics.txt
	rm $RESOURCES_DIR/versions/*.01
else
	cd $RESOURCES_DIR
	mkdir versions
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
