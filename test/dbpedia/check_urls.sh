#!/bin/bash

function checkurl
{
    myline=$1
    myurl=$2
    if ! wget -q --method=HEAD $myurl; then
        echo $myline >> invalid_instance_types
    else
        echo $myline >> valid_instance_types
    fi
}

echo "splitting"
split -l 5000 test test_

echo "filtering"
sed -i -n '/http:\/\/dbpedia.org\/ontology\//p' test_*
echo "done"

echo "Separating valid and invalid URLs of all files:"
maxno=500
cno=0

for file in test_*
do
	while read line;
	do
		url=`echo "$line" | cut -d' ' -f1 | cut -d'<' -f2 | cut -d'>' -f1`
		checkurl  "$line" "$url" &
		((cno=cno+1))
		if [ $cno -gt $maxno ]
		then
		    echo "Sleeping"
			sleep 10
			cno=0
		fi
	done < $file
	echo "$file URLs completed"
done
wait

echo "counting types"
cat invalid_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' > invalid_types.tsv 
cat valid_instance_types | cut -d \< -f 4 | cut -d \> -f 1 | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' > valid_types.tsv 
sed -i 's%http://dbpedia.org/ontology/%%g' invalid_types.tsv
sed -i 's%http://dbpedia.org/ontology/%%g' valid_types.tsv

cat invalid_instance_types | cut -d' ' -f1 | cut -d'<' -f2 | cut -d'>' -f1 > invalid_urls

rm test_*
rm *valid_instance_types* 
mv *.tsv "dashboard_test_data/"
mv invalid_urls "dashboard_test_data/"


echo "Done"