#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
EN="en"
DASHBOARD="dashboard_data"

function join_wikistats {
cd $RESOURCES_DIR/$1/$DASHBOARD
cat *uriCounts_a* >> uriCounts
cat *pairCounts_a* >> pairCounts
cat *sfAndTotalCounts_a* >> sfAndTotalCounts
if [ "$1" = "$EN" ]
then
	cat *tokens_a* >> tokens
	cat *pairCounts_b* >> pairCounts
	cat *sfAndTotalCounts_b* >> sfAndTotalCounts
	cat *sfAndTotalCounts_c* >> sfAndTotalCounts
	rm *Counts_b*
	rm *Counts_c*
	rm *tokens_a*
fi
echo "Cleaning pairCounts file"
cat pairCounts | awk -F '\t' '{if($3~/^[0-9]+$/){print}}' > cleaned_pairCounts
rm *Counts_a*
rm pairCounts
}

echo "Joining files"
join_wikistats "$ES"
join_wikistats "$EN"
echo "Done"
