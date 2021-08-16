# DBpedia-Spotlight-Dashboard - GSoC 2021
An integrated statistical information tool from the Wikipedia dumps and the DBpedia Extraction Framework artifacts

Dashboard URL: http://134.155.95.24:8050/

## Table of Contents
- [Objective](#objective)
- [Dashboard chart](#dbpedia-spotlight-dashboard-flowchart)
- [Dashboard content](#dashboard-content)
- [Raw data](#raw-data)
- [Used tools](#used-tools)
- [How to run](#how-to-run)
- [Future work](#future-work)

### Objective

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets ([instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/)) and [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts)** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, it is first necessary to **obtain the raw data**.  Subsequently, it is verified that the DBpedia entities (URLs) that Spotlight uses (URLs of the `uriCounts` file) are found  in one of the three DBpedia datasets (`instance-types`, `redirects` and `disambiguations`).  If they are found in a dataset, they are entities whose type is **known** (from DBpedia), on the contrary,  if they are not found in any dataset, they are entities whose type is **unknown**.  This process is called **entity validation**. 
Once `valid URLs` (of known type), `invalid URLs` (of unknown type)  and the `DBpedia types` that each URL present are known, a series of **statistical measures** are calculated on the data  (percentage of valid URLs over the total (**precision**), percentage of invalid URLs over the total (**impact**), mean, median, standard deviation, quartiles , percentiles, etc).   
Afterwards, **necessary figures** are generated to visualize the statistics.  Once all the figures are ready, they are placed and the final dashboard is obtained.

### DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)

### Dashboard Content
The dashboard consists of 4 tabs: 
 - [**Information**](#information-tab)
 - [**Instance-types comparison**](#instance-types-comparison-tab)
 - [**Details**](#details-tab)
 - [**Feedback**](#feedback-tab)

![Tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/1_tabs.png)

#### Information tab
This tab explains:
 - The **purpose** of this dashboard
 - How the **statistics** have been computed
 - The **entity validation** process
 - The **raw files** that DBpedia Spotlight uses during the generation of a language model
 
![Information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/2_information.png)
 
#### Instance-types comparison tab
This tab is used to compare the `instance-types` of the versions *October 2016,* *October 2020*, *May 2021* and *June 2021* for **English** and **Spanish** languages

It is divided into 3 views:
 - **Version comparison**: a table to compare the number of entities and types of the selected versions as well as the diffs
 
 ![Version Comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/3_comparison.png)

 - **Version 1 VS Version 2**: allows to see graphically the number of entities of selected versions
 
![VS](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/4_comparison.png)

 - **DBpedia types comparison**: allows to compare the entities of each selected version according to the DBpedia classes following a [hierarchy structure](http://mappings.dbpedia.org/server/ontology/classes/)
 
![Types comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/5_comparison.png)

#### Details tab
It contains 6 sub-tabs:
 - Summary
 - Instance-types
 - uriCounts
 - pairCounts
 - tokenCounts
 - sfAndTotalCounts

![Sub-tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/6_details.png)
 
 ##### Summary
 It is used to view the calculated statistics in table form

![Summary](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/7_details.png)

##### Instance-types
Allows to view the instance-types in more detail for the selected language and version

![Instance-types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/8_details.png)


It is divided in two main sections:

 - **DBpedia Extraction Framework**: to see metrics about the `raw files` of the DBpedia Databus that Spotlight uses to generate the models
 - **DBpedia Spotlight**: to see metrics about the entities and types that are actually used by DBpedia Spotlight after the `entity validation process`
 
 Both sections are formed by the following views:
 - **Measures of Central Tendency**: mean, mode
 - **Measures of Dispersion**: standard deviation
 
 ![Instance-types measures](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/9_details.png)

 - **Entities by DBpedia types** 
 
![Instance-types entities and types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/10_details.png)

Moreover, the following views can be seen in the **DBpedia Spotlight** section:
 - **Precision and impact** calculated after entity validation process

![Precision and impact](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/11_details.png)

 - **Position measures for DBpedia types** (quartiles and percentiles)

![Position measures](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/12_details.png)

 - **Top 50 DBpedia types with more entities**
 
![Top](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/13_details.png)

##### uriCounts
Allows to see metrics calculated from the **uriCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 ![uriCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/14_details.png)

##### pairCounts
Allows to see metrics calculated from the **pairCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 ![pairCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/15_details.png)

##### tokenCounts
Allows to see metrics calculated from the **tokenCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 ![tokenCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/16_details.png)

##### sfAndTotalCounts
Allows to see metrics calculated from the **sfAndTotalCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
![sfAndTotalCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/17_details.png)

In addition, it can be seen the surface forms according to their state in the **Wikipedia dump**:
 - **Without associated link** (**-1** in second file column)
 - **Not appearing as text** (**0** in third file column)
 - **Not appearing as text without associated link** (**-1** in second file column and **0** in third file column)
 - **Rest** (surface forms with associated link and appearing as text)

![sfAndTotalCounts pie chart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/18_details.png)

#### Feedback tab
Any questions or suggestions for improvement can be made by filling out the following form: https://forms.gle/YKiibhasVuYQ5goe6

![Feedback tab](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/19_feedback.png)

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

###  Used Tools
 - [GNU datamash](https://www.gnu.org/software/datamash/) for statistics calculation
 - [Dash framework](https://dash.plotly.com/) for building the web app
 - [Plotly Python graphing library](https://plotly.com/python/) for visualizations
 - [Spyder IDE](https://www.spyder-ide.org/) for development and integration

### How to Run
In order to run the dashboard on yout local system, it is only necessary to:
- Clone the repository
- Go to the root folder and execute `main.sh` script

The script will install all the necessary packages and modules

### Future Work
These are some tasks that would be interesting to do in the future:
- Include the rest of the languages available in DBpedia-Spotlight in the `Details` and `Instance-types comparison` tabs.
- Define the statistical information as Linked Data
- Define an onotlogy for the representation of statistical information
