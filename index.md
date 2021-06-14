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
 - Validation of DBpedia links (entities) -> In progress (solving problem)
 - Review of the code generated so far -> Done
 - Dashboard draft using [Dash](https://dash.plotly.com/) -> Done
 ![Dashboard draft](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_draft.png)
