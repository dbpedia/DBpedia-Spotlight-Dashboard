input=$1
while IFS= read -r line
do
	# echo "$line"

	resource=$(echo $line | cut -d ' ' -f 1)
	# echo $resource

        # echo  curl -s http://localhost:8890/sparql --data-urlencode "query=ASK {OPTIONAL {<$resource> <http://dbpedia.org/ontology/wikiPageDisambiguates> ?resource. ?resource a ?type.} OPTIONAL {<$resource> <http://dbpedia.org/ontology/wikiPageRedirects> ?resource. ?resource a ?type.} OPTIONAL {<$resource> a ?type.} FILTER regex(?type,'dbpedia.org','i') }" --data-urlencode "format=text/csv"

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
	
	if [ $count != "0" ]
	then
		echo $resource >> valid_urls
	else
		echo $resource >> invalid_urls
	fi
	
done < "$input"
