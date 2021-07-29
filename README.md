# DBpedia-Spotlight-Dashboard
An integrated statistical information tool from the Wikipedia dumps and the DBpedia Extraction Framework artifacts

## Table of contents
- [Objective](#objective)
- [Dashboard chart](#dbpedia-spotlight-dashboard-flowchart)
- [Raw data](#raw-data)

### Objective

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets ([instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/)) and [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts)** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, it is first necessary to **obtain the raw data**.  Subsequently, it is verified that the DBpedia entities (URLs) that Spotlight uses (URLs of the `uriCounts` file) are found  in one of the three DBpedia datasets (`instance-types`, `redirects` and `disambiguations`).  If they are found in a dataset, they are entities whose type is **known** (from DBpedia), on the contrary,  if they are not found in any dataset, they are entities whose type is **unknown**.  This process is called **entity validation**. 
Once `valid URLs` (of known type), `invalid URLs` (of unknown type)  and the `DBpedia types` that each URL present are known, a series of **statistical measures** are calculated on the data  (percentage of valid URLs over the total (**precision**), percentage of invalid URLs over the total (**impact**), mean, median, standard deviation, quartiles , percentiles, etc).   
Afterwards, **necessary figures** are generated to visualize the statistics.  Once all the figures are ready, they are placed and the final dashboard is obtained.

### DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)

### Raw Data
As mentioned before, the statistical measures have been calculated from the **DBpedia datasets** and the Wikipedia statistical files (**Wikistats**)

#### DBpedia Datasets
- **redirets.nt**: contains the redirect links extracted from Wikipedia redirection pages
- **disambiguations.nt**: contains the disambiguation links extracted from Wikipedia disambiguation pages
- **instance_types.nt**: classification of instances with the DBpedia Ontology. Triple containers of the form `<$ resource> rdf: type <$ dbpedia_ontology_class>` generated by the mappings extraction.

![DBpedia Datasets](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/information_dbpedia_datasets.png)

#### Wikistats
- **uriCounts**: Contains the number of times each DBpedia resource (URI) appears in the Wikipedia dump
- **pairCounts**: contains the number of times that a text (surface form) is used to link a DBpedia resource
- **sfAndTotalCounts**: Contains the number of times a text (surface form) appears linked to a DBpedia resource (second column) and also the number of times it appears unlinked (third column).
- **tokenCounts**: contains the number of times the words (tokens) appear in each Wikipedia article

![Wikistats](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/information_wikistats.png)