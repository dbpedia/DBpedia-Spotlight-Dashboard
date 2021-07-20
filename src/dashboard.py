# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table import DataTable
import figures as F
import resources as R
import callbacks as CB


app = dash.Dash(external_stylesheets=[dbc.themes.LUX])


app.layout = html.Div(children=[
    html.Br(),
    html.H1(children='DBpedia Spotlight Dashboard'),
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        # Information tab
        dcc.Tab(label='Information', children = [
            html.Br(),
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
        dcc.Tab(id='es_tab', label='Spanish', value = "spanish", children = [
        dcc.Tabs(id='subtabs', value='subtab-1', children=[
        # Instance-types subtab
        dcc.Tab(id='es_types_tab', label='Instance types', value = 'es_types', children = [html.Br(),
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
        DataTable(
            id="es_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
            data=R.top_known_types_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 425
                         }
        )
            ])
        ,
         # uriCounts subtab
         dcc.Tab(label='uriCounts', value = 'es_uricounts', children = [html.Br(),
               html.H4("Number of times each DBpedia entity appears in Wikipedia dump"),
        html.Br(),
        html.Div([
        dcc.RangeSlider(id='uriCounts_slider', min=0, max=1300, step=None, value=[0, 100],
        marks={
            0: '0',
            100: '100',
            200: '200',
            300: '300',
            400: '400',
		    500: '500',
		    600: '600',
		    700: '700',
		    800: '800',
		    900: '900',
		   1000:'1000',
           1100:'1100',
           1200:'1200',
           1300:'1300'
    }
    ),
        dcc.Graph(id="uriCounts_graph", style={'width': '1500px', 'height': '500px'},
                  figure= F.get_uriCounts_figure(R.es_dashboard_directory,R.uriCounts_es)), 
        ])
         ,
        html.H4("Top 50 most frequent entities"),
        html.Br(),
        DataTable(
            id="es_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            data=R.top_uriCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 450
                         }
        )
         ])
              ,
          # pairCounts subtab
         dcc.Tab(label='pairCounts', children = [html.Br(),
              html.H4("Number of times each surface form is linked to a DBpedia entity"),
            html.Br(),
            html.Div([
            dcc.RangeSlider(id='pairCounts_slider', min=0, max=1300, step=None, value=[0, 100],
            marks={
                0: '0',
                100: '100',
                200: '200',
                300: '300',
                400: '400',
    		    500: '500',
    		    600: '600',
    		    700: '700',
    		    800: '800',
    		    900: '900',
    		   1000:'1000',
               1100:'1100',
               1200:'1200',
               1300:'1300'
        }
        ),
            dcc.Graph(id="pairCounts_graph", style={'width': '1500px', 'height': '500px'},
                      figure= F.get_pairCounts_figure(R.es_dashboard_directory,R.pairCounts_es)), 
            ])
          ,          
          html.H4("Top 50 most linked surface forms"),
           html.Br(),
        DataTable(
            id="es_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            data=R.top_pairCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 520
                         }
        )])
              ,
          # tokenCounts subtab
         dcc.Tab(label='tokenCounts', children = [html.Br(),
               html.Div(children=[
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº Wikipedia pages"), html.H4(R.es_stats[43])], 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº tokens per Wikipedia pages"), html.H4(R.es_stats[44])], 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'), 
             ]),
         html.Br(),
          html.H4("Number of tokens per Wikipedia article"),
        html.Br(),
        html.Div([
        dcc.RangeSlider(id='tokenCounts_slider', min=0, max=1300, step=None, value=[0, 100],
        marks={
            0: '0',
            100: '100',
            200: '200',
            300: '300',
            400: '400',
		    500: '500',
		    600: '600',
		    700: '700',
		    800: '800',
		    900: '900',
		   1000:'1000',
           1100:'1100',
           1200:'1200',
           1300:'1300'
    }
    ),
        dcc.Graph(id="tokenCounts_graph", style={'width': '1500px', 'height': '500px'},
                  figure= F.get_tokenCounts_figure(R.es_dashboard_directory,R.tokenCounts_es)), 
        ]),
        html.H4("Top 50 Wikipedia articles with more tokens"),
        html.Br(),
        DataTable(
            id="tokenCounts_table",
             columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
            data=R.top_tokenCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 475
                         }
        )
              ]),
          # sfAndTotalCounts subtab
        dcc.Tab(label='sfAndTotalCounts', children = [html.Br(),
              html.Div([
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº surface forms"), html.H4(R.es_stats[47])]
                                       )]), color='#F5F5F5', style={'display': 'inline-block'})
                   ]),
          html.Br(),
           html.H4("Surface forms"),
          dcc.Graph(id='es_pie', figure=F.es_sfpie_figure),
          html.Br(),
          html.H4("Number of times each surface form is linked to a DBpedia entity"),
            html.Br(),
            html.Div([
            dcc.RangeSlider(id='sfAndTotalCounts_slider', min=0, max=1300, step=None, value=[0, 100],
            marks={
                0: '0',
                100: '100',
                200: '200',
                300: '300',
                400: '400',
    		    500: '500',
    		    600: '600',
    		    700: '700',
    		    800: '800',
    		    900: '900',
    		   1000:'1000',
               1100:'1100',
               1200:'1200',
               1300:'1300'
        }
        ),
            dcc.Graph(id="sfAndTotalCounts_graph", style={'width': '1500px', 'height': '500px'},
                      figure= F.get_sfAndTotalCounts_figure(R.es_dashboard_directory,R.sfAndTotalCounts_es)), 
            ]),
          html.H4("Top 50 most linked surface forms"),
        DataTable(
            id="es_sfAndTotalCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=R.top_sfAndTotalCounts_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 400
                         }
        )
              
              ])
        ])
        ])
          ,
        # English tab
        dcc.Tab(id='en_tab', label='English', value = "english", children = [
        dcc.Tabs(id='en-subtabs', value='en-subtab-1', children=[
        # Instance-types subtab
        dcc.Tab(id='en_types_tab', label='Instance types', value = 'en_types', children = [html.Br(),
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
        DataTable(
            id="en_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
            data=R.top_known_types_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 325
                         }
        )
       ]),
         # uriCounts subtab
        dcc.Tab(label='uriCounts', value = 'en_uricounts', children = [html.Br(),
             html.Div([
        html.H4("Number of times each DBpedia entity appears in Wikipedia dump"),
        html.Br(),
        html.Div([
        dcc.RangeSlider(id='en_uriCounts_slider', min=0, max=1300, step=None, value=[0, 100],
        marks={
            0: '0',
            100: '100',
            200: '200',
            300: '300',
            400: '400',
		    500: '500',
		    600: '600',
		    700: '700',
		    800: '800',
		    900: '900',
		   1000:'1000',
           1100:'1100',
           1200:'1200',
           1300:'1300'
    }
    ),
        dcc.Graph(id="en_uriCounts_graph", style={'width': '1500px', 'height': '500px'},
                  figure= F.get_uriCounts_figure(R.en_dashboard_directory,R.uriCounts_en)), 
        ]),
        html.H4("Top 50 most frequent entities"),
        html.Br(),
        DataTable(
            id="en_uriCounts_table",
             columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            data=R.top_uriCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 500
                         }
        )])
       ]),
         # pairCounts subtab
        dcc.Tab(label='pairCounts', children = [html.Br(),
             html.Div([
         html.H4("Number of times each surface form is linked to a DBpedia entity"),
            html.Br(),
            html.Div([
            dcc.RangeSlider(id='en_pairCounts_slider', min=0, max=1300, step=None, value=[0, 100],
            marks={
                0: '0',
                100: '100',
                200: '200',
                300: '300',
                400: '400',
    		    500: '500',
    		    600: '600',
    		    700: '700',
    		    800: '800',
    		    900: '900',
    		   1000:'1000',
               1100:'1100',
               1200:'1200',
               1300:'1300'
        }
        ),
            dcc.Graph(id="en_pairCounts_graph", style={'width': '1500px', 'height': '500px'},
                      figure= F.get_pairCounts_figure(R.en_dashboard_directory,R.pairCounts_en)), 
            ]),
          html.H4("Top 50 most linked surface forms"),
           html.Br(),
        DataTable(
            id="en_pairCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            data=R.top_pairCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 780
                         }
        )
        ])
       ]),
         # tokenCounts subtab
        dcc.Tab(label='tokenCounts', children = [html.Br(),
             html.Div([
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº Wikipedia pages"), html.H4(R.en_stats[43])], 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº tokens per Wikipedia pages"), html.H4(R.en_stats[44])], 
                                         )]),style={'display': 'inline-block', "margin-left": "30px"}, color='#F5F5F5'), 
             ]),
         html.Br(),
          html.H4("Number of tokens per Wikipedia article"),
        html.Br(),
        html.Div([
        dcc.RangeSlider(id='en_tokenCounts_slider', min=0, max=1300, step=None, value=[0, 100],
        marks={
            0: '0',
            100: '100',
            200: '200',
            300: '300',
            400: '400',
		    500: '500',
		    600: '600',
		    700: '700',
		    800: '800',
		    900: '900',
		   1000:'1000',
           1100:'1100',
           1200:'1200',
           1300:'1300'
    }
    ),
        dcc.Graph(id="en_tokenCounts_graph", style={'width': '1500px', 'height': '500px'},
                  figure= F.get_tokenCounts_figure(R.en_dashboard_directory,R.tokenCounts_en)), 
        ]),
        html.H4("Top 50 Wikipedia articles with more tokens"),
        html.Br(),
        DataTable(
            id="en_tokenCounts_table",
             columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
            data=R.top_tokenCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 500
                         }
        )
       ]),
        
         # sfAndTotalCounts subtab
        dcc.Tab(label='sfAndTotalCounts', children = [html.Br(),
             html.Div([
          dbc.Card(dbc.CardBody([html.Div([html.H4("Nº surface forms"), html.H4(R.en_stats[47])]
                                       )]), color='#F5F5F5', style={'display': 'inline-block'})
                   ]),
          html.Br(),
           html.H4("Surface forms"),
          dcc.Graph(id='en_pie', figure=F.en_sfpie_figure),
          html.Br(),
          html.H4("Number of times each surface form is linked to a DBpedia entity"),
            html.Br(),
            html.Div([
            dcc.RangeSlider(id='en_sfAndTotalCounts_slider', min=0, max=1300, step=None, value=[0, 100],
            marks={
                0: '0',
                100: '100',
                200: '200',
                300: '300',
                400: '400',
    		    500: '500',
    		    600: '600',
    		    700: '700',
    		    800: '800',
    		    900: '900',
    		   1000:'1000',
               1100:'1100',
               1200:'1200',
               1300:'1300'
        }
        ),
            dcc.Graph(id="en_sfAndTotalCounts_graph", style={'width': '1500px', 'height': '500px'},
                      figure= F.get_sfAndTotalCounts_figure(R.en_dashboard_directory,R.sfAndTotalCounts_en)), 
            ]),
          html.H4("Top 50 most linked surface forms"),
        DataTable(
            id="en_sfAndTotalCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=R.top_sfAndTotalCounts_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 625
                         }
        )
       ])
        ])   
    ]),
        # Comparison tab                    
        dcc.Tab(label='Comparison', value='comparison-tab', children = [
            html.Br(),
        html.H3("Choose language version: "),
        dcc.Dropdown(id='lang_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}], 
            placeholder="Language"),
        html.Br(),
        html.H3("Choose 2 versions to compare: "),
        html.Div([
        dcc.Dropdown(id='version1_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 1st 2021', 'value': 'May 1st 2021'},
            {'label': 'June 1st 2021', 'value': 'June 1st 2021'}
            ], 
            placeholder="Version 1", style={'display': 'inline-block', 'width': 700}),
        dcc.Dropdown(id='version2_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 1st 2021', 'value': 'May 1st 2021'},
            {'label': 'June 1st 2021', 'value': 'June 1st 2021'}
            ], 
            placeholder="Version 2", style={'display': 'inline-block', 'width': 700, "margin-left": "25px"})
        ]),
       html.Br(),
       html.Div(id='data_container'),
       html.Br(),
      html.Div(id='figures_container')
        ]),
        
        # Feedback tab
        dcc.Tab(label='Feedback', children = [
            html.Br(),
            dcc.Markdown('''
## Give us your opinion!                         


If you are a user who finds this tool useful, we would like you to `fill out a form` to evaluate the Dashboard and give suggestions for improvement.

`The form is available here:` https://forms.gle/YKiibhasVuYQ5goe6

`We will take into account all opinions for future features / updates ;)`

In this form the following usability principles are contemplated:
- Visibility of System Status
- Match between System and the Real World
- User Control and Freedom
- Consistency and Standards
- Recognition rather than Recall
- Flexibility and Efficiency of Use
- Aesthetic and Minimalist Design / Remove the Extraneous
(Ink)
- Spatial Organization
- Information Coding
- Orientation

If you want to know more about these usability principles and about some aspects to take into account when evaluating a visual tool, you can consult the article by Dawn Dowding and Jacqueline A. Merrill: [The Development of Heuristics for Evaluation of Dashboard Visualizations.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6041119/)

Thanks for your time :)              
                         ''')  
            ])
            ])
            ])

if __name__ == '__main__':
    CB.initialize_callbacks(app)
    app.run_server(host='0.0.0.0', port=8050, debug=False)
    