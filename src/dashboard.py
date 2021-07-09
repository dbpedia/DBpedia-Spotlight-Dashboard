# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table import DataTable
import figures as F
import resources as R
import callbacks as CB


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(children=[
    html.H1(children='DBpedia Spotlight Dashboard'),
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        # Information tab
        dcc.Tab(label='Information', children = [
            dcc.Markdown('''
## DBpedia Spotlight 
**DBpedia Spotlight** is a tool for automatically **annotating mentions of DBpedia resources in text**,  providing a solution for linking unstructured information sources to the Linked Open Data cloud through DBpedia. Spotlight can annotate texts in multiple languages (e.g., English, German, French, Portuguese, etc). 

### How does Spotlight link DBpedia resources with their corresponding text?
 First it is necessary to **create a model for the desired language** (Spanish, English ...).  Then Spotlight takes the model as input and **performs 4 steps**:   
 - `Spotting`: texts that may correspond to a DBpedia resource are detected
- `Candidate selection`: candidate DBpedia resources are selected for each text detected in the previous step
- `Disambiguation`: for each text, the DBpedia resource that most corresponds to all the candidates is selected.
- `Filtering`: the annotations obtained are filtered according to the needs of each user.

### How are the models created?
The following datasets for the desired language are first downloaded from the DBpedia Databus:  [instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/).   Wikipedia dump is then downloaded for the desired language in `XML` format. Subsequently, [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (Wikistats)  are generated from the Wikipedia dump: `uriCounts`, `pairCounts`, `sfAndTotalCounts`  and `tokenCounts`. Once the three DBpedia datasets and Wikipedia statistics are obtained, **the model for the corresponding  language is created**.

### DBpedia Spotlight Flowchart

![DBpedia Spotlight Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/spotlight_flowchart.png)

## DBpedia Spotlight Dashboard

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets and Wikistats** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, it is first necessary to **obtain the raw data**.  Subsequently, it is verified that the DBpedia entities (URLs) that Spotlight uses (URLs of the `uriCounts` file) are found  in one of the three DBpedia datasets (`instance-types`, `redirects` and `disambiguations`).  If they are found in a dataset, they are entities whose type is **known** (from DBpedia), on the contrary,  if they are not found in any dataset, they are entities whose type is **unknown**.  This process is called **entity validation**. 
Once `valid URLs` (of known type), `invalid URLs` (of unknown type)  and the `DBpedia types` that each URL present are known, a series of **statistical measures** are calculated on the data  (percentage of valid URLs over the total (**precision**), percentage of invalid URLs over the total (**impact**), mean, median, standard deviation, quartiles , percentiles, etc).   
Afterwards, **necessary figures** are generated to visualize the statistics.  Once all the figures are ready, they are placed and the final dashboard is obtained.

### DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)              
                         ''')  
            ]),
        # Spanish tab
        dcc.Tab(label='Spanish', children = [
        html.Br(),    
        html.Div(children=[html.H2("DBpedia Extraction Framework"),
        html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia entities"), html.H3(R.es_stats[2])]
                                         )]),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia types"), html.H3(R.es_stats[3])] 
                                         )]), style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),  
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº redirects"), html.H3(R.es_stats[0])] 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº disambiguations"), html.H3(R.es_stats[1])] 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          html.Div(children=[html.H3("Entities by DBpedia types"),
           dcc.Graph(id='ontologyy', figure=F.ontology_figure, style={'display': 'inline-block'}),
           dcc.Graph(id='es_instance_types', figure=F.es_instance_types_figure, 
                                   style={'display': 'inline-block'})]
            )]),
         html.Br(),
         html.Div([html.H2("DBpedia Spotlight"),      
         html.Br(),        
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia entities"), html.H3(R.es_stats[4])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia types"), html.H3(R.es_stats[5])])]),
                  style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          dcc.Graph(id='es_statistics', figure=F.es_statistics_figure)]),
        html.Div(children=[html.H3("Entities by DBpedia types"),
           dcc.Graph(id='ontology', figure=F.ontology_figure, style={'display': 'inline-block'}),
           dcc.Graph(id='es_known_types', figure=F.es_known_types_figure, 
                                   style={'display': 'inline-block'})]
            ),
        html.Br(),
        html.H3("Position measures for DBpedia types"),
        html.Div([
         dcc.Graph(id='ontology_pos', figure=F.ontology_figure, style={'display': 'inline-block'}),
         dcc.Graph(id='es_known_types_pos', figure=F.es_pos_known_types_figure, 
                                 style={'display': 'inline-block'})
        ]),
        html.Br(),
        html.H3("Top 50 DBpedia types with more entities"),
        html.Br(),
        html.Div([
        html.Div([
        DataTable(
            id="es_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"}],
            data=R.top_known_types_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 310
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="es_known_types_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.es_top_known_types_figure)], style={'display': 'flex'}),
         html.Br(),
          html.Div([html.H2("Wikistats"),
                   ]),
          html.Div([html.H3("uriCounts"),
        html.H4("Top 50 most frequent entities"),
        html.Br(),
           html.Div([
        html.Div([
        DataTable(
            id="es_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"}],
            data=R.uriCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 375
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="es_uriCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.es_uriCounts_figure)], style={'display': 'flex'}),
                   ]),
           html.Br(),
          html.Div([html.H3("pairCounts"),
          html.H4("Top 50 most linked surface forms"),
           html.Br(),
           html.Div([
        html.Div([
        DataTable(
            id="es_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"}],
            data=R.pairCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 385
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="es_pairCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.es_pairCounts_figure)], style={'display': 'flex'}),
                   
                   ]),
           html.Br(),
         html.Div(children=[html.H3("tokenCounts"),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº Wikipedia pages"), html.H4(R.es_stats[43])], 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº tokens per Wikipedia pages"), html.H4(R.es_stats[44])], 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'), 
             ]),
          html.Br(),
          html.Div([html.H3("sfAndTotalCounts"),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº surface forms"), html.H4(R.es_stats[45])]
                                       )]), color='#F5F5F5', style={'display': 'inline-block'})
                   ]),
          html.Br(),
          html.H4("Top 50 most linked surface forms"),
           html.Div([
        html.Div([
        DataTable(
            id="es_sfAndTotalCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=R.sfAndTotalCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 325
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="es_sfAndTotalCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.es_sfAndTotalCounts_figure)], style={'display': 'flex'}),
            html.Br(),
           html.H4("Surface forms"),
          dcc.Graph(id='es_pie', figure=F.es_sfpie_figure),
          ]),
        # English tab
        dcc.Tab(label='English', children = [
        html.Br(),    
        html.Div(children=[html.H2("DBpedia Extraction Framework"),
        html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia entities"), html.H3(R.en_stats[2])]
                                         )]),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia types"), html.H3(R.en_stats[3])] 
                                         )]), style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),  
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº redirects"), html.H3(R.en_stats[0])] 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº disambiguations"), html.H3(R.en_stats[1])] 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          html.Div(children=[html.H3("Entities by DBpedia types"),
           dcc.Graph(id='en_ontologyy', figure=F.ontology_figure, style={'display': 'inline-block'}),
           dcc.Graph(id='en_instance_types', figure=F.en_instance_types_figure, 
                                   style={'display': 'inline-block'})]
            )]),
         html.Br(),
         html.Div([html.H2("DBpedia Spotlight"),      
         html.Br(),        
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia entities"), html.H3(R.en_stats[4])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H3("Nº DBpedia types"), html.H3(R.en_stats[5])])]),
                  style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          dcc.Graph(id='en_statistics', figure=F.en_statistics_figure)]),
        html.Div(children=[html.H3("Entities by DBpedia types"),
           dcc.Graph(id='en_ontology', figure=F.ontology_figure, style={'display': 'inline-block'}),
           dcc.Graph(id='en_known_types', figure=F.en_known_types_figure, 
                                   style={'display': 'inline-block'})]
            ),
        html.Br(),
        html.H3("Position measures for DBpedia types"),
        html.Div([
         dcc.Graph(id='en_ontology_pos', figure=F.ontology_figure, style={'display': 'inline-block'}),
         dcc.Graph(id='en_known_types_pos', figure=F.en_pos_known_types_figure, 
                                 style={'display': 'inline-block'})
        ]),
        html.Br(),
        html.H3("Top 50 DBpedia types with more entities"),
        html.Br(),
        html.Div([
        html.Div([
        DataTable(
            id="en_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"}],
            data=R.top_known_types_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 230
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="en_known_types_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.en_top_known_types_figure)], style={'display': 'flex'}),
         html.Br(),
          html.Div([html.H2("Wikistats"),
                   ]),
          html.Div([html.H3("uriCounts"),
        html.H4("Top 50 most frequent entities"),
        html.Br(),
           html.Div([
        html.Div([
        DataTable(
            id="en_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"}],
            data=R.uriCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 430
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="en_uriCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.en_uriCounts_figure)], style={'display': 'flex'}),
                   ]),
           html.Br(),
          html.Div([html.H3("pairCounts"),
          html.H4("Top 50 most linked surface forms"),
           html.Br(),
           html.Div([
        html.Div([
        DataTable(
            id="en_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"}],
            data=R.pairCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 670
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="en_pairCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.en_pairCounts_figure)], style={'display': 'flex'}),
                   
                   ]),
           html.Br(),
         html.Div(children=[html.H3("tokenCounts"),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº Wikipedia pages"), html.H4(R.en_stats[43])], 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº tokens per Wikipedia pages"), html.H4(R.en_stats[44])], 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'), 
             ]),
          html.Br(),
          html.Div([html.H3("sfAndTotalCounts"),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº surface forms"), html.H4(R.en_stats[45])]
                                       )]), color='#F5F5F5', style={'display': 'inline-block'})
                   ]),
          html.Br(),
          html.H4("Top 50 most linked surface forms"),
           html.Div([
        html.Div([
        DataTable(
            id="en_sfAndTotalCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=R.sfAndTotalCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 520
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="en_sfAndTotalCounts_stats", style={'width': '900px', 'height': '400px'},
                  figure= F.en_sfAndTotalCounts_figure)], style={'display': 'flex'}),
            html.Br(),
           html.H4("Surface forms"),
          dcc.Graph(id='en_pie', figure=F.en_sfpie_figure),
          ]),
        # To be modified                    
        dcc.Tab(label='Comparison', value='comparison-tab', children = [
            html.Div(children=[
            html.H3('Choose metric to compare:'),
          dcc.Dropdown(id='dropdown',options=[
            {'label': 'Precision', 'value': 'Precision'},
            {'label': 'Impact', 'value': 'Impact'}], value = 'Precision'),
          dcc.Graph(id='metric', figure={})
    ])])
            ])])

if __name__ == '__main__':
    CB.initialize_callbacks(app)
    app.run_server(debug=True)
    