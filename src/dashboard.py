# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
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
    'margin-left': '0.9765625vw' ,
    'box-shadow': ' 0.13020833333333334vw  0.13020833333333334vw  0.13020833333333334vw  0.13020833333333334vw lightgrey',
 
}
 
tab_selected_style = {
    'borderTop': '0.06510416666666667vw solid #d6d6d6',
    'borderBottom': '0.06510416666666667vw solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '0.390625vw',
    'border-radius': '0.9765625vw',
    'margin-left': '0.9765625vw'
}

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.title = 'DBpedia Spotlight Dashboard'

app.layout = html.Div(children=[
    # Header
    html.Div([
        html.Div([], className = 'col-1'),
        html.Div([
            html.Img(
                    src = app.get_asset_url('spotlight_logo.png'),
                    height = '43px',
                    width = 'auto')
            ],
            className = 'col-1',
            style = {
                    'align-items': 'center',
                    'padding-top' : '1%',
                    'height' : 'auto'
                    }),
        html.Div([
            html.H1(children='DBpedia Spotlight Dashboard',
                    style = {'textAlign' : 'center'}
            )],
            className='col-8',
            style = {'padding-top' : '1%'}
        ),
         html.Div([], className = 'col-2')
        ], 
        className = 'row',
        style = {'height' : '4%', 'background-color' : '#F5F5F5'}),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        # Information tab
        dcc.Tab(label='Information', children = [
            html.Div([
            html.Br(),
            dcc.Markdown('''
## DBpedia Spotlight Dashboard

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets and Wikistats** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, these steps have been followed:

 1. `Obtain raw data` from the DBpedia Databus
 2. `Entity validation process`: throughout the project, it was seen that there are Spotlight entities whose type is **unknown**. This process consists of determining the DBpedia entities with `known types` and those with `unknown types`.
DBpedia entities with `known types` will be found in one of the following datasets: `instance-types`, `redirects`, and `disambiguations`. 
Whereas entities with `unknown types` will not be found in any of them. 
 3. `Computation of statistical measures`: percentage of entities with known types over the total (precision), percentage of entities with unknown types over the total (impact), mean, median, standard deviation, quartiles, percentiles...
 4. `Plot dashboard figures`


### Statistics Calculation
For the computation of statistics, [Datamash command-line program](https://www.gnu.org/software/datamash/) has been used.

The measures of central tendency and dispersion (`mean`, `mode` and `standard deviation`) have been calculated using the corresponding frequencies that appear in the different files (instance-types, uriCounts, pairCounts, tokenCounts and sfAndTotalCounts).

For the position measures (`median`, `quartiles` and `percentiles`), these frequencies have been ordered and the number obtained in each statistical measure has been mapped with its corresponding label in each file.

### DBpedia Spotlight Dashboard Flowchart
'''),
html.Img(src='https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png', style={'height':'26.041666666666668vw', 'width':'65.10416666666667vw'}),
html.Br(),
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
'''),
html.Img(src='https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/spotlight_flowchart.png', style={'height':'26.041666666666668vw', 'width':'65.10416666666667vw'}),
                        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
            ], style = tab_style, selected_style = tab_selected_style),
         # Comparison tab                    
        dcc.Tab(label='Instance-types comparison', value='comparison-tab', children = [
            html.Div([
            html.Br(),
            dcc.Markdown('''
              In this section, it is shown the difference instance-types size between two versions from the same language.          
                         '''),    
        html.H3("Choose language and 2 versions to compare: "),
        html.Div([
        dcc.Dropdown(id='lang_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            value='English',
            style={'display': 'inline-block', 'width': '29.296875vw'}), 
        dcc.Dropdown(id='version1_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 1st 2021', 'value': 'May 1st 2021'},
            {'label': 'June 1st 2021', 'value': 'June 1st 2021'}
            ],
            value='Oct 1st 2016',
            style={'display': 'inline-block', 'width': '29.296875vw', "margin-left": "0.8138020833333334vw"}),
        dcc.Dropdown(id='version2_dropdown',options=[
            {'label': 'Oct 1st 2016', 'value': 'Oct 1st 2016'},
            {'label': 'Oct 1st 2020', 'value': 'Oct 1st 2020'},
            {'label': 'May 1st 2021', 'value': 'May 1st 2021'},
            {'label': 'June 1st 2021', 'value': 'June 1st 2021'}
            ], 
            value='June 1st 2021',
             style={'display': 'inline-block', 'width': '29.296875vw', "margin-left": "1.25vw"})
        ]),
       html.Hr(),
       html.Div(id='data_container'),
       html.Hr(style={'margin-top': '-0.6510416666666666vw'}),
       html.Div(id='figures_container')      
      ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
                         
        # Details tab
         dcc.Tab(id='details_tab', label='Details', value = "details", children = [        
            dcc.Tabs(id='subtabs', value='subtab-1', children=[
            
        # Summary subtab    
          dcc.Tab(id='summary_tab', label='Summary', value = 'summary', children = [
            html.Div([
             html.Br(),
            html.H3("Choose language and files version: "),
            html.Div([
              dcc.Dropdown(id='summary_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),  
            dcc.Dropdown(id='summary_version_dropdown',options=[
                {'label': 'Oct 2016', 'value': 'Oct 2016'},
                {'label': 'Oct 2020', 'value': 'Oct 2020'},
                {'label': 'May 2021', 'value': 'May 2021'},
                {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
                placeholder="Version", 
                style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})
            ]
            ),
             html.Hr(),
            html.Div(id='summary_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),   
            
        # Instance-types subtab
        dcc.Tab(id='types_tab', label='Instance-types', value = 'types', children = [
            html.Div([
            html.Br(),
             html.H3("Choose language and instance-types file version: "),
            html.Div([
              dcc.Dropdown(id='types_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),
            dcc.Dropdown(id='types_version_dropdown',options=[
                {'label': 'May 2021', 'value': 'May 2021'}], 
                value="May 2021", 
                style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})
            ]),
             html.Hr(),
             html.Div(id='types_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style)
        ,
         # uriCounts subtab
         dcc.Tab(label='uriCounts', value = 'es_uricounts', children = [
        html.Div([
        html.Br(),
        html.H3("Choose language and uriCounts file version: "),
        html.Div([
        dcc.Dropdown(id='uriCounts_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),    
        dcc.Dropdown(id='uriCounts_version_dropdown',options=[
            {'label': 'Oct 2016', 'value': 'Oct 2016'},
            {'label': 'Oct 2020', 'value': 'Oct 2020'},
            {'label': 'May 2021', 'value': 'May 2021'},
            {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
            placeholder="Version", style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})]),
         html.Hr(),
        html.Div(id='uriCounts_container')
        ],style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
         ], style = tab_style, selected_style = tab_selected_style)
              ,
          # pairCounts subtab
         dcc.Tab(label='pairCounts', children = [
             html.Div([
                html.Br(),
        html.H3("Choose language and pairCounts file version: "),
        html.Div([
        dcc.Dropdown(id='pairCounts_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),    
        dcc.Dropdown(id='pairCounts_version_dropdown',options=[
            {'label': 'Oct 2016', 'value': 'Oct 2016'},
            {'label': 'Oct 2020', 'value': 'Oct 2020'},
            {'label': 'May 2021', 'value': 'May 2021'},
            {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
            placeholder="Version", style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})]),
         html.Hr(),
        html.Div(id='pairCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
          ], style = tab_style, selected_style = tab_selected_style)
              ,
          # tokenCounts subtab
         dcc.Tab(label='tokenCounts', children = [
          html.Div([
          html.Br(),
        html.H3("Choose language and tokenCounts file version: "),
        html.Div([
        dcc.Dropdown(id='tokenCounts_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),    
        dcc.Dropdown(id='tokenCounts_version_dropdown',options=[
            {'label': 'Oct 2016', 'value': 'Oct 2016'},
            {'label': 'Oct 2020', 'value': 'Oct 2020'},
            {'label': 'May 2021', 'value': 'May 2021'},
            {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
            placeholder="Version", style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})]),
         html.Hr(),
        html.Div(id='tokenCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
        ], style = tab_style, selected_style = tab_selected_style),
          # sfAndTotalCounts subtab
        dcc.Tab(label='sfAndTotalCounts', children = [
            html.Div([
             html.Br(),
        html.H3("Choose language and sfAndTotalCounts file version: "),
        html.Div([
        dcc.Dropdown(id='sfAndTotalCounts_language_dropdown',options=[
            {'label': 'Spanish', 'value': 'Spanish'},
            {'label': 'English', 'value': 'English'}],
            placeholder="Language", style={'display': 'inline-block', 'width': '39.0625vw'}),    
        dcc.Dropdown(id='sfAndTotalCounts_version_dropdown',options=[
            {'label': 'Oct 2016', 'value': 'Oct 2016'},
            {'label': 'Oct 2020', 'value': 'Oct 2020'},
            {'label': 'May 2021', 'value': 'May 2021'},
            {'label': 'Jun 2021', 'value': 'Jun 2021'}], 
            placeholder="Version", style={'display': 'inline-block', 'width': '39.0625vw', "margin-left": "1.6276041666666667vw"})]),
         html.Hr(),
        html.Div(id='sfAndTotalCounts_container')
        ], style = {'margin-left': '3.2552083333333335vw', 'margin-right': '3.2552083333333335vw'})
              ], style = tab_style, selected_style = tab_selected_style)
        ], style = subtabs_styles)
        ], style = tab_style, selected_style = tab_selected_style) ,             
        
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
    