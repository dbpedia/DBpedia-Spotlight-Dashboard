from SPARQLWrapper import SPARQLWrapper, JSON


en_sparql = SPARQLWrapper("http://dbpedia.org/sparql")
es_sparql = SPARQLWrapper("http://dbpedia.org/sparql")
dbpedia_es = "resources/es/"
dbpedia_en = "resources/en/"

def get_dbpedia_resources(endpoint, lang_directory):
    i = 0
    file = open(lang_directory + "dbpedia_resources.txt", "w", encoding="utf-8")
    offset = 0
    while True:
        i+=1
        print("Iteration: " + str(i))
        endpoint.setQuery("""
   SELECT DISTINCT ?resource
   WHERE 
   { 
    ?resource rdf:type ?resource2
   } 
   LIMIT 100000
   OFFSET """ + str(offset)
                    )
        endpoint.setReturnFormat(JSON)
        results = endpoint.query().convert()
        n_results = len(results["results"]["bindings"])
        if(n_results == 0):
            print("Results obtained")
            file.close()
            break;
        for result in results["results"]["bindings"]:
            file.write(result["resource"]["value"] + "\n")
        offset += 100000
'''
print("Obtaining DBpedia resources for Spanish")
get_dbpedia_resources(es_sparql, dbpedia_es)
'''

print("Obtaining DBpedia resources for English")
get_dbpedia_resources(en_sparql, dbpedia_en)           