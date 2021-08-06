# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_table import DataTable
import figures as F
import resources as R
import callbacks as CB


tabs_styles = {
    'height': '2.8645833333333335vw',
    'align-items': 'center',
    'margin-left': '3.2552083333333335vw',
    'margin-right': '3.2552083333333335vw'
}

subtabs_styles = {
    'height': '2.8645833333333335vw',
    'width' : '65.10416666666667vw',
    'align-items': 'center',
    'margin-left': '13.020833333333334vw',
    'margin-right': '3.2552083333333335vw'
}

tab_style = {
    'borderBottom': '0.06510416666666667vw solid #d6d6d6',
    'padding': '0.390625vw',
    'fontWeight': 'bold',
    'border-radius': '0.9765625vw',
    'background-color': '#F2F2F2',
    'box-shadow': '0.2604166666666667vw 0.2604166666666667vw 0.2604166666666667vw 0.2604166666666667vw lightgrey',
 
}
 
tab_selected_style = {
    'borderTop': '0.06510416666666667vw solid #d6d6d6',
    'borderBottom': '0.06510416666666667vw solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '0.390625vw',
    'border-radius': '0.9765625vw',
}


app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(children=[
    # Header
    html.Div([
        html.Div([], className = 'col-2'),
        
        html.Div([
            html.H1(children='DBpedia Spotlight Dashboard',
                    style = {'textAlign' : 'center'}
            )],
            className='col-8',
            style = {'padding-top' : '1%'}
        ),
        
        html.Div([
            html.Img(
                    src = app.get_asset_url('spotlight_logo.png'),
                    height = '43px',
                    width = 'auto')
            ],
            className = 'col-2',
            style = {
                    'align-items': 'center',
                    'padding-top' : '1%',
                    'height' : 'auto'})

        ], 
        className = 'row',
        style = {'height' : '4%', 'background-color' : '#F5F5F5'}),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        # Information tab
        dcc.Tab(label='Information', children = [
            html.Div([
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
                                                                                                                                                                                                                                                                                                                                                                                                                                       
### Model raw data
As mentioned before, Spotlight models are created from the **DBpedia datasets** and the Wikipedia statistical files (**Wikistats**)

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
                        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
            ], style = tab_style, selected_style = tab_selected_style),
        # Spanish tab
        dcc.Tab(id='es_tab', label='Spanish', value = "spanish", children = [
        dcc.Tabs(id='subtabs', value='subtab-1', children=[
            
        # Summary subtab    
          dcc.Tab(id='es_summary_tab', label='Summary', value = 'es_summary', children = [
            html.Div([
             html.Br(),
            html.H3("Choose files version: "),
            dcc.Dropdown(id='es_summary_dropdown',options=[
                {'label': 'Oct 2016', 'value': 'Oct 2016'},
                {'label': 'Oct 2020', 'value': 'Oct 2020'},
                {'label': 'May 2021', 'value': 'May 2021'},
                {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
                placeholder="Version"),
             html.Br(),
            html.Div(id='es_summary_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),   
            
        # Instance-types subtab
        dcc.Tab(id='es_types_tab', label='Instance types', value = 'es_types', children = [
            html.Div([
            html.Br(),
             html.Div(children=[html.H3(html.B("DBpedia Extraction Framework - May 2021"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),
        html.Br(),
        html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia entities"), html.H4(R.versions_stats[36])]
                                         )]),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia types"), html.H4(R.versions_stats[37])] 
                                         )]), style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
         html.Br(),
         html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº redirects"), html.H4(R.es_stats[0])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº disambiguations"), html.H4(R.es_stats[1])] 
                                         )]),style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.versions_stats[38])])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H5("Intermediate DBpedia type (median)"), html.H4('dbo:AdministrativeRegion')])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Agent')])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H5("Standard deviation"), html.H4(R.versions_stats[40])])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Br(),
          html.Br(),
          html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontologyy', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='es_instance_types', figure=F.es_instance_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})]
            )]),
         html.Br(),
         html.Div([html.H3(html.B("DBpedia Spotlight - May 2021"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),      
         html.Br(),
         html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia entities"), html.H4(R.es_stats[2])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia types"), html.H4(R.es_stats[3])])]),
                  style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5')]),
          dcc.Graph(id='es_statistics', figure=F.es_statistics_figure),
        html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontology', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='es_known_types', figure=F.es_known_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})]
            ),
        html.Br(),
        html.H4("Position measures for DBpedia types"),
        html.Div([
         dcc.Graph(id='ontology_pos', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
         dcc.Graph(id='es_known_types_pos', figure=F.es_pos_known_types_figure, 
                                 style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})
        ]),
        html.Br(),
        html.H4("Top 50 DBpedia types with more entities"),
        html.Br(),
        html.Div([
        html.Div([
        DataTable(
            id="es_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw'
           },
            data=R.top_known_types_2021_05_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 425, 'margin-left': '0.6510416666666666vw'
                         }
        )
        ])])
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style)
        ,
         # uriCounts subtab
         dcc.Tab(label='uriCounts', value = 'es_uricounts', children = [
        html.Div([
        html.Br(),
        html.H3("Choose uriCounts file version: "),
        dcc.Dropdown(id='uriCounts_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='uriCounts_container')
        ],style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
         ], style = tab_style, selected_style = tab_selected_style)
              ,
          # pairCounts subtab
         dcc.Tab(label='pairCounts', children = [
             html.Div([
                html.Br(),
        html.H3("Choose pairCounts file version: "),
        dcc.Dropdown(id='pairCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='pairCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
          ], style = tab_style, selected_style = tab_selected_style)
              ,
          # tokenCounts subtab
         dcc.Tab(label='tokenCounts', children = [
          html.Div([
          html.Br(),
        html.H3("Choose tokenCounts file version: "),
        dcc.Dropdown(id='tokenCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='tokenCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
          # sfAndTotalCounts subtab
        dcc.Tab(label='sfAndTotalCounts', children = [
            html.Div([
             html.Br(),
        html.H3("Choose sfAndTotalCounts file version: "),
        dcc.Dropdown(id='sfAndTotalCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='sfAndTotalCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
              ], style = tab_style, selected_style = tab_selected_style)
        ], style = subtabs_styles)
        ], style = tab_style, selected_style = tab_selected_style)
          ,
        # English tab
        dcc.Tab(id='en_tab', label='English', value = "english", children = [
        dcc.Tabs(id='en-subtabs', value='en-subtab-1', children=[
            
        # Summary subtab    
        dcc.Tab(id='en_summary_tab', label='Summary', value = 'en_summary', children = [
        html.Div([
        html.Br(),
            html.H3("Choose files version: "),
            dcc.Dropdown(id='en_summary_dropdown',options=[
                {'label': 'Oct 2016', 'value': 'Oct 2016'},
                {'label': 'Oct 2020', 'value': 'Oct 2020'},
                {'label': 'May 2021', 'value': 'May 2021'},
                {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
                placeholder="Version"),
             html.Br(),
            html.Div(id='en_summary_container')        
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),   
        # Instance-types subtab
        dcc.Tab(id='en_types_tab', label='Instance types', value = 'en_types', children = [
            html.Div([
            html.Br(),
            html.Div(children=[html.H3(html.B("DBpedia Extraction Framework - May 2021"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),
        html.Br(),
        html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia entities"), html.H4(R.versions_stats[108])]
                                         )]),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia types"), html.H4(R.versions_stats[109])] 
                                         )]), style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),  
          html.Br(),
          html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº redirects"), html.H4(R.en_stats[0])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº disambiguations"), html.H4(R.en_stats[1])] 
                                         )]),style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
          html.Br(),
          html.Br(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.versions_stats[110])])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H5("Intermediate DBpedia type (median)"), html.H4('dbo:Work')])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Agent')])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H5("Standard deviation"), html.H4(R.versions_stats[112])])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Br(),
          html.Br(),
          html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='en_ontologyy', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='en_instance_types', figure=F.en_instance_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})]
            )]),
         html.Br(),
         html.Div([html.H3(html.B("DBpedia Spotlight - May 2021"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),      
         html.Br(),        
         html.Br(),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia entities"), html.H4(R.en_stats[2])] 
                                         )]),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.Div([html.H5("Nº DBpedia types"), html.H4(R.en_stats[3])])]),
                  style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5')]),
          dcc.Graph(id='en_statistics', figure=F.en_statistics_figure),
        html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='en_ontology', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='en_known_types', figure=F.en_known_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})]
            ),
        html.Br(),
        html.H4("Position measures for DBpedia types"),
        html.Div([
         dcc.Graph(id='en_ontology_pos', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
         dcc.Graph(id='en_known_types_pos', figure=F.en_pos_known_types_figure, 
                                 style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})
        ]),
        html.Br(),
        html.H4("Top 50 DBpedia types with more entities"),
        html.Br(),
        html.Div([
        html.Div([
        DataTable(
            id="en_top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw'
           },
            data=R.top_known_types_2021_05_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 375, 'margin-left': '0.6510416666666666vw'
                         }
        )
        ])])
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
        # uriCounts subtab
         dcc.Tab(label='uriCounts', value = 'en_uricounts', children = [
        html.Div([
        html.Br(),
        html.H3("Choose uriCounts file version: "),
        dcc.Dropdown(id='en_uriCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='en_uriCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
         ], style = tab_style, selected_style = tab_selected_style),
        # pairCounts subtab
         dcc.Tab(label='pairCounts', children = [
        html.Div([
        html.Br(),
        html.H3("Choose pairCounts file version: "),
        dcc.Dropdown(id='en_pairCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='en_pairCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
          ], style = tab_style, selected_style = tab_selected_style),
          # tokenCounts subtab
         dcc.Tab(label='tokenCounts', children = [
        html.Div([
          html.Br(),
        html.H3("Choose tokenCounts file version: "),
        dcc.Dropdown(id='en_tokenCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='en_tokenCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
          # sfAndTotalCounts subtab
        dcc.Tab(label='sfAndTotalCounts', children = [
            html.Div([
             html.Br(),
        html.H3("Choose sfAndTotalCounts file version: "),
        dcc.Dropdown(id='en_sfAndTotalCounts_dropdown',options=[
             {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 25th 2021', 'value': 'May 25th 2021'},
            {'label': 'Jun 25th 2021', 'value': 'Jun 25th 2021'}], 
            placeholder="Version"),
         html.Br(),
        html.Div(id='en_sfAndTotalCounts_container')
              ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style)]
            , style = subtabs_styles)
        ], style = tab_style, selected_style = tab_selected_style),
        # Comparison tab                    
        dcc.Tab(label='Instance types comparison', value='comparison-tab', children = [
            html.Div([
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
            placeholder="Version 1", style={'display': 'inline-block', 'width': '39.0625vw'}),
        dcc.Dropdown(id='version2_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 1st 2021', 'value': 'May 1st 2021'},
            {'label': 'June 1st 2021', 'value': 'June 1st 2021'}
            ], 
            placeholder="Version 2", style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})
        ]),
       html.Br(),
       html.Div(id='data_container'),
       html.Br(),
       html.Div(id='figures_container')
      ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
        
      # Feedback tab
        dcc.Tab(label='Feedback', children = [
            html.Div([
            html.Br(),
            dcc.Markdown(
'''
## Give us your opinion!                         
If you are a user who finds this tool useful, we would like you to `fill out a form` to evaluate the Dashboard and give suggestions for improvement.

`The form is available here:` https://forms.gle/YKiibhasVuYQ5goe6

`We will take into account all opinions for future features/updates`

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

Thanks for your time!              
'''
          )
                ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
], style = tab_style, selected_style = tab_selected_style)
], style = tabs_styles)
])

if __name__ == '__main__':
    CB.initialize_callbacks(app)
    app.run_server(host='0.0.0.0', port=8050, debug=False)
    