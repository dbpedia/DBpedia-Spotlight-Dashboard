#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
EN="en"
DATASETS="dbpedia_datasets"
WIKISTATS="wikistats"
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

function remove_old_files {
cd $RESOURCES_DIR/$1/$DASHBOARD
rm "stats.txt"
rm *top50*
rm "instance_types.tsv"
}

function get_precision_impact {
cd $RESOURCES_DIR/$1/$DASHBOARD
VALID_URLS_FILE=$RESOURCES_DIR/$1/$DASHBOARD/valid_urls
INVALID_URLS_FILE=$RESOURCES_DIR/$1/$DASHBOARD/invalid_urls
VALID_URLS_LINES=$(cat $VALID_URLS_FILE | wc -l) 
INVALID_URLS_LINES=$(cat $INVALID_URLS_FILE | wc -l)
TOTAL_LINES=$((VALID_URLS_LINES + INVALID_URLS_LINES))
PRECISION=$(echo 'print(round(' $VALID_URLS_LINES/$TOTAL_LINES ', 3))' | python3 )
IMPACT=$(echo 'print(round(' $INVALID_URLS_LINES/$TOTAL_LINES ', 3))' | python3 )
echo "DBpedia Spotlight URLs" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Precision of DBpedia types URLs: $PRECISION" >> stats.txt
echo "Impact of unknown type URLs: $IMPACT" >> stats.txt
echo "" >> stats.txt
# rm *valid_urls*
}

function get_redirects_disambiguations {
cd $RESOURCES_DIR/$1/$DASHBOARD
REDIRECTS_FILE=$RESOURCES_DIR/$1/$DATASETS/redirects.nt
DISAMBIGUATIONS_FILE=$RESOURCES_DIR/$1/$DATASETS/disambiguations.nt
REDIRECTS_LINES=$(cat $REDIRECTS_FILE | awk -F ' ' '{print $1}' | sort | uniq | wc -l)
DISAMBIGUATIONS_LINES=$(cat $DISAMBIGUATIONS_FILE | awk -F ' ' '{print $1}' | sort | uniq | wc -l)
echo "DBpedia Extraction Framework redirects and disambiguations" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Number of redirects (without counting repetitions): $REDIRECTS_LINES" >> stats.txt
echo "Number of disambiguations (without counting repetitions): $DISAMBIGUATIONS_LINES" >> stats.txt
echo "" >> stats.txt
}

function get_types {
cd $RESOURCES_DIR/$1/$DASHBOARD
INSTANCE_TYPES_FILE=$RESOURCES_DIR/$1/$DATASETS/instance_types.nt
echo "Filtering"
cat $INSTANCE_TYPES_FILE | grep "http://dbpedia.org/ontology/" >> filtered_instance_types
INSTANCE_TYPES_LINES=$(cat filtered_instance_types | awk -F ' ' '{print $1}' | sort | uniq | wc -l)
echo "DBpedia Extraction Framework instance-types" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Number of DBpedia entities (without counting repetitions): $INSTANCE_TYPES_LINES" >> stats.txt
echo "Getting number of resources for each DBpedia type"
cat filtered_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' >> instance_types.tsv
sed -i 's%http://dbpedia.org/ontology/%%g' instance_types.tsv
INSTANCE_TYPES_TSV_LINES=$(cat instance_types.tsv | wc -l)
echo "Number of DBpedia types: $INSTANCE_TYPES_TSV_LINES" >> stats.txt
echo "" >> stats.txt
echo "DBpedia Spotlight instance-types" >> stats.txt
echo "-------------------------------------" >> stats.txt
VALID_TYPES_LINES=$(cat valid_urls | wc -l)
VALID_TYPES_TSV_LINES=$(cat valid_types.tsv | wc -l)
echo "Number of DBpedia entities with DBpedia types (without counting repetitions): $VALID_TYPES_LINES" >> stats.txt
echo "Number of DBpedia types: $VALID_TYPES_TSV_LINES" >> stats.txt
echo "Getting most used resources of valid_types.tsv file"
cat valid_types.tsv | head -n 50 >> valid_types_top50
echo "Done"
rm "filtered_instance_types"
echo "Calculating stats of valid_types.tsv URLs"
cat valid_types.tsv | cut -f 2 -d$' ' | datamash mean 1 median 1 pvar 1 sum 1 >> temp.txt
MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
MEDIAN=$(awk -F '\t' '{ print $2 }' temp.txt)
MEDIAN=$(echo 'print(round(' $MEDIAN ',2))' | python3 )
VAR=$(awk -F '\t' '{ print $3 }' temp.txt)
VAR=$(echo 'print(round(' $VAR ',2))' | python3 )
STDDEV=$(bc <<< "scale=2; sqrt($VAR)")
SUM=$(awk -F '\t' '{ print $4 }' temp.txt)
rm temp.txt
echo "Calculating position measures"
cat valid_types.tsv | awk '{for (i=1; i<=$2; i++) print NR}' | datamash q1 1 q3 1 perc:10 1 perc:20 1 perc:30 1 perc:40 1 perc:50 1 perc:60 1 perc:70 1 perc:80 1 perc:90 1 perc:95 1 >> temp.txt
Q1=$(awk -F '\t' '{ print $1 }' temp.txt)
Q1=$(echo 'print(round(' $Q1 '))' | python3 )
Q3=$(awk -F '\t' '{ print $2 }' temp.txt)
Q3=$(echo 'print(round(' $Q3 '))' | python3 )
PERC10=$(awk -F '\t' '{ print $3 }' temp.txt)
PERC10=$(echo 'print(round(' $PERC10 '))' | python3 )
PERC20=$(awk -F '\t' '{ print $4 }' temp.txt)
PERC20=$(echo 'print(round(' $PERC20 '))' | python3 )
PERC30=$(awk -F '\t' '{ print $5 }' temp.txt)
PERC30=$(echo 'print(round(' $PERC30 '))' | python3 )
PERC40=$(awk -F '\t' '{ print $6 }' temp.txt)
PERC40=$(echo 'print(round(' $PERC40 '))' | python3 )
PERC50=$(awk -F '\t' '{ print $7 }' temp.txt)
PERC50=$(echo 'print(round(' $PERC50 '))' | python3 )
PERC60=$(awk -F '\t' '{ print $8 }' temp.txt)
PERC60=$(echo 'print(round(' $PERC60 '))' | python3 )
PERC70=$(awk -F '\t' '{ print $9 }' temp.txt)
PERC70=$(echo 'print(round(' $PERC70 '))' | python3 )
PERC80=$(awk -F '\t' '{ print $10 }' temp.txt)
PERC80=$(echo 'print(round(' $PERC80 '))' | python3 )
PERC90=$(awk -F '\t' '{ print $11 }' temp.txt)
PERC90=$(echo 'print(round(' $PERC90 '))' | python3 )
PERC95=$(awk -F '\t' '{ print $12 }' temp.txt)
PERC95=$(echo 'print(round(' $PERC95 '))' | python3 )
echo "Mean number of DBpedia entities per type: $MEAN" >> stats.txt
echo "Median number of DBpedia entities per type: $MEDIAN" >> stats.txt
echo "Population variance of DBpedia entities per type: $VAR" >> stats.txt
echo "Population standard deviation of DBpedia entities per type: $STDDEV" >> stats.txt
echo "Number of DBpedia entities with DBpedia types (counting repetitions, for checking quartiles and percentiles): $SUM" >> stats.txt
echo "First quartile value of DBpedia entities per type: $Q1" >> stats.txt
echo "Third quartile value of DBpedia entities per type: $Q3" >> stats.txt
echo "10th percentile value of DBpedia entities per type: $PERC10" >> stats.txt
echo "20th percentile value of DBpedia entities per type: $PERC20" >> stats.txt
echo "30th percentile value of DBpedia entities per type: $PERC30" >> stats.txt
echo "40th percentile value of DBpedia entities per type: $PERC40" >> stats.txt
echo "50th percentile value of DBpedia entities per type: $PERC50" >> stats.txt
echo "60th percentile value of DBpedia entities per type: $PERC60" >> stats.txt
echo "70th percentile value of DBpedia entities per type: $PERC70" >> stats.txt
echo "80th percentile value of DBpedia entities per type: $PERC80" >> stats.txt
echo "90th percentile value of DBpedia entities per type: $PERC90" >> stats.txt
echo "95th percentile value of DBpedia entities per type: $PERC95" >> stats.txt
echo "" >> stats.txt
echo "Done"
rm temp.txt
}

function get_uriCounts {
cd $RESOURCES_DIR/$1/$DASHBOARD
URICOUNTS_FILE=$RESOURCES_DIR/$1/$WIKISTATS/uriCounts
echo "Getting most used resources of uriCounts file"
cat $URICOUNTS_FILE | sort -t$'\t' -k2 -nr | uniq | head -n 50 >> uriCounts_top50
if [ "$1" = "$ES" ]
then
	sed -i 's%http://es.dbpedia.org/resource/%%g' uriCounts_top50
else
	sed -i 's%http://dbpedia.org/resource/%%g' uriCounts_top50
fi
echo "Done"
echo "DBpedia Spotlight uriCounts" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Calculating stats of uriCounts URLs"
cat $URICOUNTS_FILE | cut -f 2 -d$'\t' | datamash mean 1 median 1 pvar 1 >> temp.txt
MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
MEDIAN=$(awk -F '\t' '{ print $2 }' temp.txt)
MEDIAN=$(echo 'print(round(' $MEDIAN ',2))' | python3 )
VAR=$(awk -F '\t' '{ print $3 }' temp.txt)
VAR=$(echo 'print(round(' $VAR ',2))' | python3 )
STDDEV=$(bc <<< "scale=2; sqrt($VAR)")
echo "Mean number of uriCounts URLs per DBpedia resource: $MEAN" >> stats.txt
echo "Median number of uriCounts URLs per DBpedia resource: $MEDIAN" >> stats.txt
echo "Population variance of uriCounts URLs per DBpedia resource: $VAR" >> stats.txt
echo "Population standard deviation of uriCounts URLs per DBpedia resource: $STDDEV" >> stats.txt
echo "" >> stats.txt
echo "Done"
rm temp.txt
}

function get_pairCounts {
cd $RESOURCES_DIR/$1/$DASHBOARD
PAIRCOUNTS_FILE=$RESOURCES_DIR/$1/$WIKISTATS/pairCounts
echo "Cleaning pairCounrs file"
cat $PAIRCOUNTS_FILE | awk -F '\t' '{if($3~/^[0-9]+$/){print}}' >> cleaned_pairCounts 
echo "Getting most used resources of pairCounts file"
cat cleaned_pairCounts | sort -t$'\t' -k3 -nr | uniq | head -n 50 >> pairCounts_top50
if [ "$1" = "$ES" ]
then
	sed -i 's%http://es.dbpedia.org/resource/%%g' pairCounts_top50
else
	sed -i 's%http://dbpedia.org/resource/%%g' pairCounts_top50
fi
echo "Done"
echo "DBpedia Spotlight pairCounts" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Calculating stats of pairCounts URLs"
cat cleaned_pairCounts | cut -f 3 -d$'\t' | datamash mean 1 median 1 pvar 1 >> temp.txt
MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
MEDIAN=$(awk -F '\t' '{ print $2 }' temp.txt)
MEDIAN=$(echo 'print(round(' $MEDIAN ',2))' | python3 )
VAR=$(awk -F '\t' '{ print $3 }' temp.txt)
VAR=$(echo 'print(round(' $VAR ',2))' | python3 )
STDDEV=$(bc <<< "scale=2; sqrt($VAR)")
echo "Mean number of pairCounts URLs per surface form: $MEAN" >> stats.txt
echo "Median number of pairCounts URLs per surface form: $MEDIAN" >> stats.txt
echo "Population variance of pairCounts URLs per surface form: $VAR" >> stats.txt
echo "Population standard deviation of pairCounts URLs per surface form: $STDDEV" >> stats.txt
echo "" >> stats.txt
rm cleaned_pairCounts 
echo "Done"
rm temp.txt
}

function get_tokenCounts {
cd $RESOURCES_DIR/$1/$DASHBOARD
TOKENCOUNTS_FILE=$RESOURCES_DIR/$1/$WIKISTATS/tokenCounts
TOKENCOUNTS_LINES=$(cat $TOKENCOUNTS_FILE | wc -l)
echo "DBpedia Spotlight tokenCounts" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Number of Wikipedia pages: $TOKENCOUNTS_LINES" >> stats.txt
echo "Calculating stats of tokens per Wikipedia page"
cat $TOKENCOUNTS_FILE | awk '{print gsub(/\([^)]*\)/,"&")}' | datamash mean 1 >> temp.txt
MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
echo "Mean number of tokens per Wikipedia page: $MEAN" >> stats.txt
echo "" >> stats.txt
echo "Done"
rm temp.txt
}

function get_sfAndTotalCounts {
cd $RESOURCES_DIR/$1/$DASHBOARD
SFANDTOTALCOUNTS_FILE=$RESOURCES_DIR/$1/$WIKISTATS/sfAndTotalCounts
SFANDTOTALCOUNTS_LINES=$(cat $SFANDTOTALCOUNTS_FILE | wc -l)
SFANDTOTALCOUNTS_NOLINKEDLINES=$(cat $SFANDTOTALCOUNTS_FILE | awk -F '\t' '{if($2==-1){print}}' | wc -l)
SFANDTOTALCOUNTS_NOTEXTLINES=$(cat $SFANDTOTALCOUNTS_FILE | awk -F '\t' '{if($3==0){print}}' | wc -l)
SFANDTOTALCOUNTS_NOLINKEDLINES_NOTEXTLINES=$(cat $SFANDTOTALCOUNTS_FILE | awk -F '\t' '{if($2==-1 && $3==0){print}}' | wc -l)
echo "Getting most used resources of sfAndTotalCounts file"
cat $SFANDTOTALCOUNTS_FILE | sort -t$'\t' -k2 -nr | uniq | head -n 50 >> sfAndTotalCounts_top50 
if [ "$1" = "$ES" ]
then
	sed -i 's%http://es.dbpedia.org/resource/%%g' sfAndTotalCounts_top50
else
	sed -i 's%http://dbpedia.org/resource/%%g' sfAndTotalCounts_top50
fi
echo "Done"
echo "DBpedia Spotlight sfAndTotalCounts" >> stats.txt
echo "-------------------------------------" >> stats.txt
echo "Number of surface forms: $SFANDTOTALCOUNTS_LINES" >> stats.txt
echo "Number of surface forms without associated link: $SFANDTOTALCOUNTS_NOLINKEDLINES" >> stats.txt
echo "Number of surface forms not appearing as text: $SFANDTOTALCOUNTS_NOTEXTLINES" >> stats.txt
echo "Number of surface forms not appearing as text without associated link: $SFANDTOTALCOUNTS_NOLINKEDLINES_NOTEXTLINES" >> stats.txt
echo "Calculating stats of sfAndTotalCounts URLs"
cat $SFANDTOTALCOUNTS_FILE | cut -f 2 -d$'\t' |  awk -F '\t' '{if($1 == -1){$1=0}{print $1}}' | datamash mean 1 median 1 pvar 1 >> temp.txt
MEAN=$(awk -F '\t' '{ print $1 }' temp.txt)
MEAN=$(echo 'print(round(' $MEAN ',2))' | python3 )
MEDIAN=$(awk -F '\t' '{ print $2 }' temp.txt)
MEDIAN=$(echo 'print(round(' $MEDIAN ',2))' | python3 )
VAR=$(awk -F '\t' '{ print $3 }' temp.txt)
VAR=$(echo 'print(round(' $VAR ',2))' | python3 )
STDDEV=$(bc <<< "scale=2; sqrt($VAR)")
echo "Mean number of sfAndTotalCounts linked URLs per surface form: $MEAN" >> stats.txt
echo "Median number of sfAndTotalCounts linked URLs per surface form: $MEDIAN" >> stats.txt
echo "Population variance of sfAndTotalCounts linked URLs per surface form: $VAR" >> stats.txt
echo "Population standard deviation of sfAndTotalCounts linked URLs per surface form: $STDDEV" >> stats.txt
echo "Done"
rm temp.txt
}

check "python3"
check "datamash"
remove_old_files "$ES"
remove_old_files "$EN"
echo "Done"
echo "Getting number of redirects and disambiguations"
get_redirects_disambiguations "$ES"
get_redirects_disambiguations "$EN"
echo "Done"
echo "Getting number of DBpedia instance-types"
get_types "$ES"
get_types "$EN"
echo "Done"
echo "Getting precision and impact of URLs"
get_precision_impact "$ES"
get_precision_impact "$EN"
echo "Done"
get_uriCounts "$ES"
get_uriCounts "$EN"
echo "Done"
get_pairCounts "$ES"
get_pairCounts "$EN"
echo "Done"
get_tokenCounts "$ES"
get_tokenCounts "$EN"
echo "Done"
get_sfAndTotalCounts "$ES"
get_sfAndTotalCounts "$EN"
echo "Done"
