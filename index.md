**[17/05/2021]**: Proposal acceptance and community bonding period started.

**[27/05/2021]**: Meeting the mentors on Google Meet to introduce ourselves and talk about the project and interesting ideas:
 - Load data from **Wikistats** (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts) and **DBpedia artifacts** (instance-types, redirects and disambiguations) in dataframes using [Pandas](https://pandas.pydata.org/) and [RDFLib](https://rdflib.readthedocs.io/en/stable/) libraries.
 - Create the desired visualizations using [Matplotlib](https://matplotlib.org/) library.
 - Use frameworks like [Dash](https://dash.plotly.com/) for building the dashboard. 
 - Compute the desired statistics over the dataframe using [NumPy](https://numpy.org/) library. 
 - Publish the statistical data generated using [Linked Open Vocabularies](https://lov.linkeddata.es/dataset/lov/) once the dashboard is built.

 **[10/06/2021]**: Second meeting with the mentors, first advances in the project and new ideas:
 - Get model raw data for Spanish and English -> Done
 - Visualize DBpedia types for Spanish and English -> Done (**problem**: some hierarchy types are missing in the instance_types file) 
 - Validation of DBpedia links (entities) -> In progress (**problem**: IP address blocked for 1 day due to excessive requests) (**new idea**: get ALL DBpedia distinct resources doing SPARQL queries and store results in local file, then look for valid URLs comparing that **generated file URLs** and **instance_types URLs** using UNIX commands)
![Blocked IP](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dbpedia_ban.png)

**[14/06/2021]**: Some progress:
 - Validation of DBpedia links (entities) -> In progress (solving problem). I found out that all entities (both valid and invalid entities) are found on SPARQL endpoints, so the idea I came up with doesn't work in this case. Regarding the first idea, even putting timeout between each request my IP address is still blocked (already 3 times in total)
 - Review of the code generated so far -> Done
 - Dashboard draft using [Dash](https://dash.plotly.com/) -> Done
 ![Dashboard draft](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_draft.png)

**[24/06/2021]**: The problem of URLs validation has been resolved:
 - URLs of the latest version of uriCounts file have been validated for Spanish language. For this, each URL of the file has been checked by means of the following SPARQL query (using a local SPARQL Endpoint to avoid DBpedia IP blocking):
 
![SPARQL validation](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/validate_query.png)

If the value returned by the query is 0, it means that this URL does not have any type, that is, it is a URL that does not exist and therefore is invalid.
- Once valid and invalid URLs for Spanish were obtained, types of valid URLs have been obtained and can be viewed according to the DBpedia hierarchy:

 ![Spanish valid types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_valid_types.png)

- Precision and impact of Spanish URLs has also been calculated.
 ![Spanish statistics](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_urls_impact.png)

- URLs validation of the latest version of uriCounts file for English language -> In progress (executing)
- Types of valid English URLs -> In progress (executing)
- Precision and impact of English URLs -> In progress (executing)

**[25/06/2021]**: DBpedia entities used by Spotlight have been validated for both Spanish and English languages. Now is time to think of other interesting statistical measures to show on the dashboard: 
- URLs validation of the latest version of uriCounts file for English language -> Done
- Types of valid English URLs -> Done

![English valid types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/en_valid_types.png)

- Precision and impact of English URLs -> Done

![English statistics](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/en_urls_impact.png)

- Think about other interesting statistical measures to show on the dashboard -> In progress
