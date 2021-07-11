echo "Getting valid types"
while read line;
do
	answer=$(curl -s http://localhost:8890/sparql --data-urlencode "query=
			SELECT  DISTINCT ?type WHERE {
<$line> a ?type.
FILTER regex(?type,'dbpedia.org','i')
}" --data-urlencode "format=text/csv")
	type=$(echo $answer | cut -d ' ' -f 2- | sed s/\"//g | grep -v type)
	echo $type >> valid_instance_types
done < "valid_urls"
cat valid_instance_types | tr " " "\n" > valid_types
echo "Done"

echo "counting types"
cat valid_types | sort | uniq -c | sort -bgr | awk '{ print $2 " " $1}' |  grep -v "^ "  > valid_types.tsv 
sed -i 's%http://dbpedia.org/ontology/%%g' valid_types.tsv
echo "Done"

#rm valid_instance_types
#rm valid_types