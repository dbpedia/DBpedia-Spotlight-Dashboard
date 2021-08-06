# -*- coding: utf-8 -*-
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_table import DataTable
import resources as R
import figures as F

es_executed = False
en_executed = False


def initialize_callbacks(app):
     # Spanish Tab callback
     @app.callback(dash.dependencies.Output('subtabs', 'value'),
              [dash.dependencies.Input('tabs', 'value')])
     def es_switch_tab(value):
             global es_executed
             if value == "spanish" and not es_executed:
                 es_executed = True
                 return "es_summary"
             else:
                 return dash.no_update
             
     # English Tab callback
     @app.callback(dash.dependencies.Output('en-subtabs', 'value'),
              [dash.dependencies.Input('tabs', 'value')])
     def en_switch_tab(value):
             global en_executed
             if value == "english" and not en_executed:
                 en_executed = True
                 return "en_summary"
             else:
                 return dash.no_update
             
    # Spanish summary callback
     @app.callback(
    dash.dependencies.Output('es_summary_container', 'children'),
    [dash.dependencies.Input('es_summary_dropdown', 'value')])
     def es_summary(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.es_stats
            versions_stats = R.versions_stats
            
            if value == 'Oct 2016':
               it_elements = versions_stats[1]
               it_mean = versions_stats[2]
               it_median = 'dbo:Athlete'
               it_mode = 'dbo:Agent'
               it_std_dev = versions_stats[4]
               uri_elements = stats[42]
               uri_mean = stats[43]
               uri_median = 'dbpedia-es:Hinduismo'
               uri_mode = 'dbpedia-es:' + R.top_2016_uriCounts_es['DBpedia entity'].iloc[0]
               uri_std_dev = stats[45]
               pair_elements = stats[46]
               pair_mean = stats[47]
               pair_median = '[hinduista - dbpedia-es:Hinduismo]'
               pair_mode =  "[" + R.top_2016_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2016_pairCounts_es['DBpedia entity'].iloc[0] + "]"
               pair_std_dev = stats[49]
               token_elements = stats[50]
               token_mean = stats[51]
               token_median = 'http://es.wikipedia.org/wiki/Imperio_almohade'
               token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_es['Wikipedia article'].iloc[0]
               token_std_dev = stats[52]
               sf_elements = stats[54]
               sf_mean = stats[59]
               sf_median = 'doris miller'
               sf_mode =  R.top_2016_sfAndTotalCounts_es['Surface form'].iloc[0]
               sf_std_dev = stats[61]
            
            if value == 'Oct 2020':
                it_elements = versions_stats[19]
                it_mean = versions_stats[20]
                it_std_dev = versions_stats[22]
                it_mode = 'dbo:Agent'
                it_median = 'dbo:AdministrativeRegion'
                uri_elements = stats[82]
                uri_mean = stats[83]
                uri_median = 'dbpedia-es:Huiracocha_Inca'
                uri_mode = 'dbpedia-es:' + R.top_2020_uriCounts_es['DBpedia entity'].iloc[0]
                uri_std_dev = stats[85]
                pair_elements = stats[86]
                pair_mean = stats[87]
                pair_median = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
                pair_mode =  "[" + R.top_2020_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2020_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[89]
                token_elements = stats[90]
                token_mean = stats[91]
                token_median = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
                token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_es['Wikipedia article'].iloc[0]
                token_std_dev = stats[92]
                sf_elements = stats[94]
                sf_mean = stats[99]
                sf_median = 'Ciudad del Vaticano'
                sf_mode =  R.top_2020_sfAndTotalCounts_es['Surface form'].iloc[0]
                sf_std_dev = stats[101]
               
    
            if value == 'May 2021':
                it_elements = versions_stats[37]
                it_mean = versions_stats[38]
                it_std_dev = versions_stats[40]
                it_mode = 'dbo:Agent'
                it_median = 'dbo:AdministrativeRegion'
                uri_elements = stats[22]
                uri_mean = stats[23]
                uri_median = 'dbpedia-es:III_milenio_a._C.'
                uri_mode = 'dbpedia-es:' + R.top_2021_05_uriCounts_es['DBpedia entity'].iloc[0]
                uri_std_dev = stats[25]
                pair_elements = stats[26]
                pair_mean = stats[27]
                pair_median = '[ambiente - dbpedia-es:Hábitat]'
                pair_mode =  "[" + R.top_2021_05_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_05_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[29]
                token_elements = stats[30]
                token_mean = stats[31]
                token_median = 'http://es.wikipedia.org/wiki/Impunidad'
                token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_es['Wikipedia article'].iloc[0]
                token_std_dev = stats[32]
                sf_elements = stats[34]
                sf_mean = stats[39]
                sf_median = 'pulmonar'
                sf_mode =  R.top_2021_05_sfAndTotalCounts_es['Surface form'].iloc[0]
                sf_std_dev = stats[41]
               
            if value == 'Jun 2021':
                it_elements = versions_stats[55]
                it_mean = versions_stats[56]
                it_std_dev = versions_stats[58]
                it_mode = 'dbo:Agent'
                it_median = 'dbo:AdministrativeRegion'
                uri_elements = stats[62]
                uri_mean = stats[63]
                uri_median = 'dbpedia-es:ITunes_Store'
                uri_mode = 'dbpedia-es:' + R.top_2021_06_uriCounts_es['DBpedia entity'].iloc[0]
                uri_std_dev = stats[65]
                pair_elements = stats[66]
                pair_mean = stats[67]
                pair_median = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
                pair_mode =  "[" + R.top_2021_06_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_06_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[69]
                token_elements = stats[70]
                token_mean = stats[71]
                token_median = 'http://es.wikipedia.org/wiki/Invierno'
                token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_es['Wikipedia article'].iloc[0]
                token_std_dev = stats[72]
                sf_elements = stats[74]
                sf_mean = stats[79]
                sf_median = 'culebrera europea'
                sf_mode =  R.top_2021_06_sfAndTotalCounts_es['Surface form'].iloc[0]
                sf_std_dev = stats[81]
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="es_summary_table",
           columns=[
        {"name": ["", "File"], "id": "file"},
        {"name": ["", "Nº elements"], "id": "elements"},
        {"name": ["Measures of central tendency", "Mean"], "id": "mean"},
        {"name": ["Measures of central tendency", "Median"], "id": "median"},
        {"name": ["Measures of central tendency", "Mode"], "id": "mode"},
        {"name": ["Measures of dispersion", "Standard deviation"], "id": "std_dev"}
    ],
       style_header=
           {
              'fontWeight': 'bold',
              'font-size': '0.9765625vw',
              'text-align': 'center'
           },
            data=[
        {
            "file": "Instance types",
            "elements": it_elements,
            "mean": it_mean,
            "median": it_median,
            "mode":it_mode,
            "std_dev": it_std_dev,
        },
        {
            "file": "uriCounts",
            "elements": uri_elements,
            "mean": uri_mean,
            "median": uri_median,
            "mode": uri_mode,
            "std_dev": uri_std_dev,
        },
        {
            "file": "pairCounts",
            "elements": pair_elements,
            "mean": pair_mean,
            "median": pair_median,
            "mode": pair_mode,
            "std_dev": pair_std_dev,
        },
        {
            "file": "tokenCounts",
            "elements": token_elements,
            "mean": token_mean,
            "median": token_median,
            "mode": token_mode,
            "std_dev": token_std_dev,
        },
        {
            "file": "sfAndTotalCounts",
            "elements": sf_elements,
            "mean": sf_mean,
            "median": sf_median,
            "mode": sf_mode,
            "std_dev": sf_std_dev,
        }
        ],
            fill_width=False,
            merge_duplicate_headers=True,
            style_table={
                'overflowY': 'scroll', 'height': '19.53125vw', 'width': '97.65625vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
    
        return table_container
    
    # English summary callback
     @app.callback(
    dash.dependencies.Output('en_summary_container', 'children'),
    [dash.dependencies.Input('en_summary_dropdown', 'value')])
     def en_summary(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.en_stats
            versions_stats = R.versions_stats
            
            if value == 'Oct 2016':
               it_elements = versions_stats[73]
               it_mean = versions_stats[74]
               it_median = 'dbo:Work'
               it_mode = 'dbo:Agent'
               it_std_dev = versions_stats[76] 
               uri_elements = stats[42]
               uri_mean = stats[43]
               uri_median = 'dbr:Latvian_constitutional_referendum,_2008'
               uri_mode = 'dbr:' + R.top_2016_uriCounts_en['DBpedia entity'].iloc[0]
               uri_std_dev = stats[45]
               pair_elements = stats[46]
               pair_mean = stats[47]
               pair_median = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
               pair_mode =  "[" + R.top_2016_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2016_pairCounts_en['DBpedia entity'].iloc[0] + "]"
               pair_std_dev = stats[49]
               token_elements = stats[50]
               token_mean = stats[51]
               token_median = 'http://en.wikipedia.org/wiki/Kushti'
               token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_en['Wikipedia article'].iloc[0]
               token_std_dev = stats[52]
               sf_elements = stats[54]
               sf_mean = stats[59]
               sf_median = 'Deep Cove'
               sf_mode =  R.top_2016_sfAndTotalCounts_en['Surface form'].iloc[0]
               sf_std_dev = stats[61]
            
            if value == 'Oct 2020':
                it_elements = versions_stats[91]
                it_mean = versions_stats[92]
                it_std_dev = versions_stats[94]
                it_median = 'dbo:Work'
                it_mode = 'dbo:Agent'
                uri_elements = stats[82]
                uri_mean = stats[83]
                uri_median = 'dbr:Lamar_University'
                uri_mode = 'dbr:' + R.top_2020_uriCounts_en['DBpedia entity'].iloc[0]
                uri_std_dev = stats[85]
                pair_elements = stats[86]
                pair_mean = stats[87]
                pair_median = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
                pair_mode =  "[" + R.top_2020_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2020_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[89]
                token_elements = stats[90]
                token_mean = stats[91]
                token_median = 'http://en.wikipedia.org/wiki/Klondike_Open'
                token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_en['Wikipedia article'].iloc[0]
                token_std_dev = stats[92]
                sf_elements = stats[94]
                sf_mean = stats[99]
                sf_median = 'The Herald'
                sf_mode =  R.top_2020_sfAndTotalCounts_en['Surface form'].iloc[0]
                sf_std_dev = stats[101]
               
    
            if value == 'May 2021':
                it_elements = versions_stats[109]
                it_mean = versions_stats[110]
                it_std_dev = versions_stats[112]
                it_median = 'dbo:Work'
                it_mode = 'dbo:Agent'
                uri_elements = stats[22]
                uri_mean = stats[23]
                uri_median = 'dbr:Kyrgyzstan_national_football_team'
                uri_mode = 'dbr:' + R.top_2021_05_uriCounts_en['DBpedia entity'].iloc[0]
                uri_std_dev = stats[25]
                pair_elements = stats[26]
                pair_mean = stats[27]
                pair_median = '[Wallenpaupack - dbr:Lake_Wallenpaupack]'
                pair_mode =  "[" + R.top_2021_05_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_05_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[29]
                token_elements = stats[30]
                token_mean = stats[31]
                token_median = 'http://en.wikipedia.org/wiki/Klas_Lund'
                token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_en['Wikipedia article'].iloc[0]
                token_std_dev = stats[32]
                sf_elements = stats[34]
                sf_mean = stats[39]
                sf_median = 'DC Comics'
                sf_mode =  R.top_2021_05_sfAndTotalCounts_en['Surface form'].iloc[0]
                sf_std_dev = stats[41]
               
                
            if value == 'Jun 2021':
                it_elements = versions_stats[127]
                it_mean = versions_stats[128]
                it_std_dev = versions_stats[130]
                it_median = 'dbo:AdministrativeRegion'
                it_mode = 'dbo:Agent'
                uri_elements = stats[62]
                uri_mean = stats[63]
                uri_median = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
                uri_mode = 'dbr:' + R.top_2021_06_uriCounts_en['DBpedia entity'].iloc[0]
                uri_std_dev = stats[65]
                pair_elements = stats[66]
                pair_mean = stats[67]
                pair_median = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
                pair_mode =  "[" + R.top_2021_06_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_06_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                pair_std_dev = stats[69]
                token_elements = stats[70]
                token_mean = stats[71]
                token_median = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
                token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_en['Wikipedia article'].iloc[0]
                token_std_dev = stats[72]
                sf_elements = stats[74]
                sf_mean = stats[79]
                sf_median = 'Cyropaedia'
                sf_mode =  R.top_2021_06_sfAndTotalCounts_en['Surface form'].iloc[0]
                sf_std_dev = stats[81]
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="en_summary_table",
           columns=[
        {"name": ["", "File"], "id": "file"},
        {"name": ["", "Nº elements"], "id": "elements"},
        {"name": ["Measures of central tendency", "Mean"], "id": "mean"},
        {"name": ["Measures of central tendency", "Median"], "id": "median"},
        {"name": ["Measures of central tendency", "Mode"], "id": "mode"},
        {"name": ["Measures of dispersion", "Standard deviation"], "id": "std_dev"}
    ],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '0.9765625vw',
              'text-align': 'center'
           },
            data=[
        {
            "file": "Instance types",
            "elements": it_elements,
            "mean": it_mean,
            "median": it_median,
            "mode":it_mode,
            "std_dev": it_std_dev,
        },
        {
            "file": "uriCounts",
            "elements": uri_elements,
            "mean": uri_mean,
            "median": uri_median,
            "mode": uri_mode,
            "std_dev": uri_std_dev,
        },
        {
            "file": "pairCounts",
            "elements": pair_elements,
            "mean": pair_mean,
            "median": pair_median,
            "mode": pair_mode,
            "std_dev": pair_std_dev,
        },
        {
            "file": "tokenCounts",
            "elements": token_elements,
            "mean": token_mean,
            "median": token_median,
            "mode": token_mode,
            "std_dev": token_std_dev,
        },
        {
            "file": "sfAndTotalCounts",
            "elements": sf_elements,
            "mean": sf_mean,
            "median": sf_median,
            "mode": sf_mode,
            "std_dev": sf_std_dev,
        }
        ],
            fill_width=False,
            merge_duplicate_headers=True,
            style_table={
                'overflowY': 'scroll', 'height': '19.53125vw', 'width': '97.65625vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
    
        return table_container
         
    # Comparison callback - cards
     @app.callback(
    dash.dependencies.Output('data_container', 'children'),
    [dash.dependencies.Input('version1_dropdown', 'value'),
     dash.dependencies.Input('version2_dropdown', 'value'),
     dash.dependencies.Input('lang_dropdown', 'value')])
     def version_data(value1, value2, lang_value):
        if(lang_value is None or value1 is None or value2 is None):
            return dash.no_update
        else:
            versions_stats = R.versions_stats
            if lang_value == 'Spanish':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[0]
                    types_version1 = versions_stats[1]
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[18]
                    types_version1 = versions_stats[19]
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[36]
                    types_version1 = versions_stats[37]
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[54]
                    types_version1 = versions_stats[55]
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[0]
                    types_version2 = versions_stats[1]
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[18]
                    types_version2 = versions_stats[19]
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[36]
                    types_version2 = versions_stats[37]
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[54]
                    types_version2 = versions_stats[55]
            
            if lang_value == 'English':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[72]
                    types_version1 = versions_stats[73]
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[90]
                    types_version1 = versions_stats[91]
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[108]
                    types_version1 = versions_stats[109]
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[126]
                    types_version1 = versions_stats[127]
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[72]
                    types_version2 = versions_stats[73]
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[90]
                    types_version2 = versions_stats[91]
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[108]
                    types_version2 = versions_stats[109]
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[126]
                    types_version2 = versions_stats[127]
                
            entity_growth = abs(int(entities_version1) - int(entities_version2))
            type_growth = abs(int(types_version1) - int(types_version2))
            version1_container = html.Div(id='entity_container', children = [
                html.H4(value1),
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia entities"), html.H4(entities_version1)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia types"), html.H4(types_version1)]
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "1.6276041666666667vw"}
                )
                ], style={'display': 'inline-block'})
                
            version2_container = html.Div(id='type_container', children = [
                html.H4(value2),
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia entities"), html.H4(entities_version2)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia types"), html.H4(types_version2)]
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "1.6276041666666667vw"}
                )
                ], style={'display': 'inline-block', "margin-left": "3.0598958333333335vw"})
            
            version_container=  html.Div(id='version_container', children = [
                version1_container, version2_container
                ]
                )
            
            growth_container = html.Div(id='growth_container', children = [
            html.H3("Growth between versions"),
            dbc.Card(dbc.CardBody(
                        [html.H5("Entity growth"), html.H4(str(entity_growth))]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
            dbc.Card(dbc.CardBody(
                [html.H5("Type growth"), html.H4(str(type_growth))]
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "1.6276041666666667vw"}
                )
                ])
            title = html.H3("Version comparison")
            
            return title, version_container, html.Br(), growth_container
    
    
    
# Comparison callback - figures
     @app.callback(
    dash.dependencies.Output('figures_container', 'children'),
    [dash.dependencies.Input('version1_dropdown', 'value'),
     dash.dependencies.Input('version2_dropdown', 'value'),
     dash.dependencies.Input('lang_dropdown', 'value')])
     def version_figures(value1, value2, lang_value):
        if(lang_value is None or value1 is None or value2 is None):
            return dash.no_update
        else:
            versions_stats = R.versions_stats
            if lang_value == 'Spanish':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[0]
                    df1 = R.instance_types_es_2016_10_01
                    
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[18]
                    df1 = R.instance_types_es_2020_10_01
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[36]
                    df1 = R.instance_types_es_2021_05_01
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[54]
                    df1 = R.instance_types_es_2021_06_01
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[0]
                    df2 = R.instance_types_es_2016_10_01
                    
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[18]
                    df2 = R.instance_types_es_2020_10_01
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[36]
                    df2 = R.instance_types_es_2021_05_01
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[54]
                    df2 = R.instance_types_es_2021_06_01
            
            if lang_value == 'English':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[72]
                    df1 = R.instance_types_en_2016_10_01
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[90]
                    df1 = R.instance_types_en_2020_10_01
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[108]
                    df1 = R.instance_types_en_2021_05_01
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[126]
                    df1 = R.instance_types_en_2021_06_01
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[72]
                    df2 = R.instance_types_en_2016_10_01
                    
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[90]
                    df2 = R.instance_types_en_2020_10_01
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[108]
                    df2 = R.instance_types_en_2021_05_01
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[126]
                    df2 = R.instance_types_en_2021_06_01
            
            bar_figure = F.get_version_bar_figure([value1, value2], [entities_version1, entities_version2])
            pie_figure = F.get_version_pie_figure([value1, value2], [entities_version1, entities_version2])
            bar_graph = dcc.Graph(id='versions_bar', figure=bar_figure, style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})
            pie_graph = dcc.Graph(id='versions_pie', figure=pie_figure, style={'height':'19.53125vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})
            title = html.H3(value1 + " VS " + value2)
            type_title = html.H3("DBpedia types comparison")
            types_container = html.Div([
                dcc.Graph(id='ontology_version', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
                dcc.Graph(id='instance_types_version', figure=F.get_versions_instance_types_figure([value1, value2], df1, df2), 
                                     style={'height':'26.041666666666668vw', 'width':'45.572916666666664vw', 'display': 'inline-block'})
                ]
                )
            return title, html.Br(), bar_graph, pie_graph, html.Br(), html.Br(),  type_title, types_container
        
       # Comparison instance types callback
     @app.callback(
            dash.dependencies.Output('instance_types_version', 'figure'),
            [dash.dependencies.Input('ontology_version', 'clickData'), 
             dash.dependencies.Input('version1_dropdown', 'value'),
             dash.dependencies.Input('version2_dropdown', 'value'),
             dash.dependencies.Input('lang_dropdown', 'value')]
            )
     def update_version_instance_types_bar(clicked_data, value1, value2, lang_value):
            selected_type = 'owlThing'
            if(lang_value is None or value1 is None or value2 is None):
                return dash.no_update
            else:
                if lang_value == 'Spanish':
                    if value1 == 'Oct 1st 2016':
                        df1 = R.instance_types_es_2016_10_01
                        
                    if value1 == 'Oct 1st 2020':
                        df1 = R.instance_types_es_2020_10_01
                        
                    if value1 == 'May 1st 2021':
                        df1 = R.instance_types_es_2021_05_01
                        
                    if value1 == 'June 1st 2021':
                        df1 = R.instance_types_es_2021_06_01
                        
                    if value2 == 'Oct 1st 2016':
                        df2 = R.instance_types_es_2016_10_01
                        
                    if value2 == 'Oct 1st 2020':
                        df2 = R.instance_types_es_2020_10_01
                        
                    if value2 == 'May 1st 2021':
                        df2 = R.instance_types_es_2021_05_01
                        
                    if value2 == 'June 1st 2021':
                        df2 = R.instance_types_es_2021_06_01
                
                if lang_value == 'English':
                    if value1 == 'Oct 1st 2016':
                        df1 = R.instance_types_en_2016_10_01
                    if value1 == 'Oct 1st 2020':
                        df1 = R.instance_types_en_2020_10_01
                        
                    if value1 == 'May 1st 2021':
                        df1 = R.instance_types_en_2021_05_01
                        
                    if value1 == 'June 1st 2021':
                        df1 = R.instance_types_en_2021_06_01
                        
                    if value2 == 'Oct 1st 2016':
                        df2 = R.instance_types_en_2016_10_01
                        
                    if value2 == 'Oct 1st 2020':
                        df2 = R.instance_types_en_2020_10_01
                        
                    if value2 == 'May 1st 2021':
                        df2 = R.instance_types_en_2021_05_01
                        
                    if value2 == 'June 1st 2021':
                        df2 = R.instance_types_en_2021_06_01
                        
            ontology_df = R.ontology_df
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df1 = df1[df1['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df1 = selected_all_instances_df1.sort_values(by='Nº entities', ascending=False)
            selected_all_instances_df2 = df2[df2['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df2 = selected_all_instances_df2.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df1.empty:
                selected_all_instances_df1.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            if selected_all_instances_df2.empty:
                selected_all_instances_df2.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure()    
            figure.add_trace(go.Bar(x = selected_all_instances_df1['Nº entities'], y = selected_all_instances_df1['DBpedia type'], orientation='h', marker_color='#A349A4', name = value1))
            figure.add_trace(go.Bar(x = selected_all_instances_df2['Nº entities'], y = selected_all_instances_df2['DBpedia type'], orientation='h', marker_color="#77C14C", name = value2))
            figure.update_layout(barmode='group', margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure

    # Spanish known types callback
     @app.callback(
            dash.dependencies.Output('es_known_types', 'figure'),
            [dash.dependencies.Input('ontology', 'clickData')]
            )
     def es_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_es_2021_05_01
            ontology_df = R.ontology_df
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
            figure.add_vline(x=float(R.es_stats[4]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.es_stats[5]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.es_stats[6]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.es_stats[4])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[4]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[5])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[5]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[6])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[6]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # Spanish instance types callback
     @app.callback(
            dash.dependencies.Output('es_instance_types', 'figure'),
            [dash.dependencies.Input('ontologyy', 'clickData')]
            )
     def es_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            mean = R.versions_stats[38]
            median = R.versions_stats[39]
            std_dev = R.versions_stats[40]
            types_count_df = R.instance_types_es_2021_05_01
            ontology_df = R.ontology_df
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = 'DBpedia type'))
            figure.add_vline(x=float(mean), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(median), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(std_dev), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
            go.Scatter(x=[float(mean)], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[mean], hoverinfo="text"),
            go.Scatter(x=[float(median)], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[median], hoverinfo="text"),
            go.Scatter(x=[float(std_dev)], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[std_dev], hoverinfo="text")
            ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure

# Spanish known types position measures callback
     @app.callback(
            dash.dependencies.Output('es_known_types_pos', 'figure'),
            [dash.dependencies.Input('ontology_pos', 'clickData')]
            )
     def es_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.known_types_es_2021_05_01["DBpedia type"].values:
                selected_row = R.known_types_es_2021_05_01[R.known_types_es_2021_05_01["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type", hovertext=["Nº entities: "+ str(selected_row.iloc[0]["Nº entities"])], hoverinfo="text"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.es_stats[10]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.es_stats[8]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.es_stats[14]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.es_stats[9]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.es_stats[18]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.es_stats[19]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.es_stats[10])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.es_stats[10]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[8])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[8]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[14])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.es_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[9])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.es_stats[9]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[18])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.es_stats[18]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[19])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.es_stats[19]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
            return fig
        
# Spanish uriCounts callback
     @app.callback(
    dash.dependencies.Output('uriCounts_container', 'children'),
    [dash.dependencies.Input('uriCounts_dropdown', 'value')])
     def uriCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.es_stats
            if value == 'Oct 1st 2016':
                dbpedia_entities = stats[42]
                mean = stats[43]
                median = 'dbpedia-es:Hinduismo'
                std_dev = stats[45]
                top_file = R.top_2016_uriCounts_es
            
            if value == 'Oct 1st 2020':
                dbpedia_entities = stats[82]
                mean = stats[83]
                median = 'dbpedia-es:Huiracocha_Inca'
                std_dev = stats[85]
                top_file = R.top_2020_uriCounts_es
    
            if value == 'May 25th 2021':
                dbpedia_entities = stats[22]
                mean = stats[23]
                median = 'dbpedia-es:III_milenio_a._C.'
                std_dev = stats[25]
                top_file = R.top_2021_05_uriCounts_es
                
            if value == 'Jun 25th 2021':
                dbpedia_entities = stats[62]
                mean = stats[63]
                median = 'dbpedia-es:ITunes_Store'
                std_dev = stats[65]
                top_file = R.top_2021_06_uriCounts_es
                
            mode = 'dbpedia-es:' + top_file['DBpedia entity'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia entities"), html.H4(dbpedia_entities)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº occurrences per DBpedia entity (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate DBpedia entity (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia entity that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="es_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '29.296875vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
    
        return cards_container, html.Br(), html.H4("Top 50 most frequent entities"), html.Br(), table_container  
        
# Spanish pairCounts callback
     @app.callback(
    dash.dependencies.Output('pairCounts_container', 'children'),
    [dash.dependencies.Input('pairCounts_dropdown', 'value')])
     def pairCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.es_stats
            if value == 'Oct 1st 2016':
                surface_forms = stats[46]
                mean = stats[47]
                median = '[hinduista - dbpedia-es:Hinduismo]'
                std_dev = stats[49]
                top_file = R.top_2016_pairCounts_es
    
            if value == 'Oct 1st 2020':
                surface_forms = stats[86]
                mean = stats[87]
                median = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
                std_dev = stats[89]
                top_file = R.top_2020_pairCounts_es
    
            if value == 'May 25th 2021':
                surface_forms = stats[26]
                mean = stats[27]
                median = '[ambiente - dbpedia-es:Hábitat]'
                std_dev = stats[29]
                top_file = R.top_2021_05_pairCounts_es
                
            if value == 'Jun 25th 2021':
                surface_forms = stats[66]
                mean = stats[67]
                median = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
                std_dev = stats[69]
                top_file = R.top_2021_06_pairCounts_es
                
            mode = "[" + top_file['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ top_file['DBpedia entity'].iloc[0] + "]"
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº [Surface form - DBpedia entity] pairs"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate pair (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                 dbc.Card(dbc.CardBody(
                        [html.H5("Pair that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="es_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '33.854166666666664vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container

# Spanish tokenCounts callback
     @app.callback(
    dash.dependencies.Output('tokenCounts_container', 'children'),
    [dash.dependencies.Input('tokenCounts_dropdown', 'value')])
     def tokenCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.es_stats
            if value == 'Oct 1st 2016':
                articles = stats[50]
                mean = stats[51]
                median = 'http://es.wikipedia.org/wiki/Imperio_almohade'
                std_dev = stats[52]
                top_file = R.top_2016_tokenCounts_es
                
            if value == 'Oct 1st 2020':
                articles = stats[70]
                mean = stats[71]
                median = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
                std_dev = stats[72]
                top_file = R.top_2020_tokenCounts_es
    
            if value == 'May 25th 2021':
                articles = stats[30]
                mean = stats[31]
                median = 'http://es.wikipedia.org/wiki/Impunidad'
                std_dev = stats[32]
                top_file = R.top_2021_05_tokenCounts_es
                
            if value == 'Jun 25th 2021':
                articles = stats[70]
                mean = stats[71]
                median = 'http://es.wikipedia.org/wiki/Invierno'
                std_dev = stats[72]
                top_file = R.top_2021_06_tokenCounts_es
                
            mode = 'http://es.wikipedia.org/wiki/'+ top_file['Wikipedia article'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº Wikipedia articles"), html.H4(articles)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº tokens per Wikipedia article (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate Wikipedia article (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Wikipedia article that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="es_tokenCounts_table",
           columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '30.924479166666668vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            return cards_container, html.Br(), html.H4("Top 50 Wikipedia articles with more tokens"), html.Br(), table_container

# Spanish sfAndTotalCounts callback
     @app.callback(
    dash.dependencies.Output('sfAndTotalCounts_container', 'children'),
    [dash.dependencies.Input('sfAndTotalCounts_dropdown', 'value')])
     def sfAndTotalCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.es_stats
            if value == 'Oct 1st 2016':
                surface_forms = stats[54]
                mean = stats[59]
                median = 'doris miller'
                std_dev = stats[61]
                top_file = R.top_2016_sfAndTotalCounts_es
                values = [stats[55], stats[56], stats[57], stats[58]]
                
            if value == 'Oct 1st 2020':
                surface_forms = stats[94]
                mean = stats[99]
                median = 'Ciudad del Vaticano'
                std_dev = stats[101]
                top_file = R.top_2020_sfAndTotalCounts_es
                values = [stats[95], stats[96], stats[97], stats[98]]
    
            if value == 'May 25th 2021':
                surface_forms = stats[34]
                mean = stats[39]
                median = 'pulmonar'
                std_dev = stats[41]
                top_file = R.top_2021_05_sfAndTotalCounts_es
                values = [stats[35], stats[36], stats[37], stats[38]]
                
            if value == 'Jun 25th 2021':
                surface_forms = stats[74]
                mean = stats[79]
                median = 'culebrera europea'
                std_dev = stats[81]
                top_file = R.top_2021_06_sfAndTotalCounts_es
                values = [stats[75], stats[76], stats[77], stats[78]]
                
            mode = top_file['Surface form'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº surface forms"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate surface form (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Surface form that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            
            figure_container = html.Div([
            html.H4("Surface forms"),
            dcc.Graph(id='es_pie', figure=F.get_sfpie_figure(values), style={'height':'19.53125vw', 'width':'45.572916666666664vw'})
            ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="es_sfAndTotalCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '32.552083333333336vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Br(), figure_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container                
        
# English known types callback
     @app.callback(
            dash.dependencies.Output('en_known_types', 'figure'),
            [dash.dependencies.Input('en_ontology', 'clickData')]
            )
     def en_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_en_2021_05_01
            ontology_df = R.ontology_df
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
            figure.add_vline(x=float(R.en_stats[4]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.en_stats[5]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.en_stats[6]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.en_stats[4])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[4]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[5])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[5]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[6])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[6]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # English instance types callback
     @app.callback(
            dash.dependencies.Output('en_instance_types', 'figure'),
            [dash.dependencies.Input('en_ontologyy', 'clickData')]
            )
     def en_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            mean = R.versions_stats[110]
            median = R.versions_stats[111]
            std_dev = R.versions_stats[112]
            types_count_df = R.instance_types_en_2021_05_01
            ontology_df = R.ontology_df
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = 'DBpedia type'))
            figure.add_vline(x=float(mean), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(median), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(std_dev), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
            go.Scatter(x=[float(mean)], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[mean], hoverinfo="text"),
            go.Scatter(x=[float(median)], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[median], hoverinfo="text"),
            go.Scatter(x=[float(std_dev)], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[std_dev], hoverinfo="text")
            ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
# English known types position measures callback
     @app.callback(
            dash.dependencies.Output('en_known_types_pos', 'figure'),
            [dash.dependencies.Input('en_ontology_pos', 'clickData')]
            )
     def en_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.known_types_en_2021_05_01["DBpedia type"].values:
                selected_row = R.known_types_en_2021_05_01[R.known_types_en_2021_05_01["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type", hovertext=["Nº entities: "+ str(selected_row.iloc[0]["Nº entities"])], hoverinfo="text"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.en_stats[10]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.en_stats[8]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.en_stats[14]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.en_stats[9]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.en_stats[18]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.en_stats[19]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.en_stats[10])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.en_stats[10]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[8])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[8]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[14])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.en_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[9])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.en_stats[9]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[18])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.en_stats[18]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[19])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.en_stats[19]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
            return fig
        
# English uriCounts callback
     @app.callback(
    dash.dependencies.Output('en_uriCounts_container', 'children'),
    [dash.dependencies.Input('en_uriCounts_dropdown', 'value')])
     def en_uriCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.en_stats
            if value == 'Oct 1st 2016':
                dbpedia_entities = stats[42]
                mean = stats[43]
                median = 'dbr:Latvian_constitutional_referendum,_2008'
                std_dev = stats[45]
                top_file = R.top_2016_uriCounts_en
            
            if value == 'Oct 1st 2020':
                dbpedia_entities = stats[82]
                mean = stats[83]
                median = 'dbr:Lamar_University'
                std_dev = stats[85]
                top_file = R.top_2020_uriCounts_en
    
            if value == 'May 25th 2021':
                dbpedia_entities = stats[22]
                mean = stats[23]
                median = 'dbr:Kyrgyzstan_national_football_team'
                std_dev = stats[25]
                top_file = R.top_2021_05_uriCounts_en
                
            if value == 'Jun 25th 2021':
                dbpedia_entities = stats[62]
                mean = stats[63]
                median = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
                std_dev = stats[65]
                top_file = R.top_2021_06_uriCounts_en
                
            mode = 'dbr:' + top_file['DBpedia entity'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia entities"), html.H4(dbpedia_entities)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H5("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº occurrences per DBpedia entity (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                 dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate DBpedia entity (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia entity that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="en_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '32.552083333333336vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
    
        return cards_container, html.Br(), html.H4("Top 50 most frequent entities"), html.Br(), table_container  
        
# English pairCounts callback
     @app.callback(
    dash.dependencies.Output('en_pairCounts_container', 'children'),
    [dash.dependencies.Input('en_pairCounts_dropdown', 'value')])
     def en_pairCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.en_stats
            if value == 'Oct 1st 2016':
                surface_forms = stats[46]
                mean = stats[47]
                median = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
                std_dev = stats[49]
                top_file = R.top_2016_pairCounts_en
    
            if value == 'Oct 1st 2020':
                surface_forms = stats[86]
                mean = stats[87]
                median = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
                std_dev = stats[89]
                top_file = R.top_2020_pairCounts_en
    
            if value == 'May 25th 2021':
                surface_forms = stats[26]
                mean = stats[27]
                median = '[Wallenpaupack -dbr:Lake_Wallenpaupack]'
                std_dev = stats[29]
                top_file = R.top_2021_05_pairCounts_en
                
            if value == 'Jun 25th 2021':
                surface_forms = stats[66]
                mean = stats[67]
                median = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
                std_dev = stats[69]
                top_file = R.top_2021_06_pairCounts_en
                
            mode = "[" + top_file['Surface form'].iloc[0] + " - " + "dbr:"+ top_file['DBpedia entity'].iloc[0] + "]"
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº [Surface form - DBpedia entity] pairs"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate pair (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                 dbc.Card(dbc.CardBody(
                        [html.H5("Pair that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="en_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '52.083333333333336vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container

# English tokenCounts callback
     @app.callback(
    dash.dependencies.Output('en_tokenCounts_container', 'children'),
    [dash.dependencies.Input('en_tokenCounts_dropdown', 'value')])
     def en_tokenCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.en_stats
            if value == 'Oct 1st 2016':
                articles = stats[50]
                mean = stats[51]
                median = 'http://en.wikipedia.org/wiki/Kushti'
                std_dev = stats[52]
                top_file = R.top_2016_tokenCounts_en
                
            if value == 'Oct 1st 2020':
                articles = stats[70]
                mean = stats[71]
                median = 'http://en.wikipedia.org/wiki/Klondike_Open'
                std_dev = stats[72]
                top_file = R.top_2020_tokenCounts_en
    
            if value == 'May 25th 2021':
                articles = stats[30]
                mean = stats[31]
                median = 'http://en.wikipedia.org/wiki/Klas_Lund'
                std_dev = stats[32]
                top_file = R.top_2021_05_tokenCounts_en
                
            if value == 'Jun 25th 2021':
                articles = stats[70]
                mean = stats[71]
                median = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
                std_dev = stats[72]
                top_file = R.top_2021_06_tokenCounts_en
                
            mode = top_file['Wikipedia article'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº Wikipedia articles"), html.H4(articles)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº tokens per Wikipedia article (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate Wikipedia article (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Wikipedia article that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="en_tokenCounts_table",
           columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '35.15625vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            return cards_container, html.Br(), html.H4("Top 50 Wikipedia articles with more tokens"), html.Br(), table_container

# English sfAndTotalCounts callback
     @app.callback(
    dash.dependencies.Output('en_sfAndTotalCounts_container', 'children'),
    [dash.dependencies.Input('en_sfAndTotalCounts_dropdown', 'value')])
     def en_sfAndTotalCounts(value):
        if(value is None):
            return dash.no_update
        else:
            stats = R.en_stats
            if value == 'Oct 1st 2016':
                surface_forms = stats[54]
                mean = stats[59]
                median = 'Deep Cove'
                std_dev = stats[61]
                top_file = R.top_2016_sfAndTotalCounts_en
                values = [stats[55], stats[56], stats[57], stats[58]]
                
            if value == 'Oct 1st 2020':
                surface_forms = stats[94]
                mean = stats[99]
                median = 'The Herald'
                std_dev = stats[101]
                top_file = R.top_2020_sfAndTotalCounts_en
                values = [stats[95], stats[96], stats[97], stats[98]]
    
            if value == 'May 25th 2021':
                surface_forms = stats[34]
                mean = stats[39]
                median = 'DC Comics'
                std_dev = stats[41]
                top_file = R.top_2021_05_sfAndTotalCounts_en
                values = [stats[35], stats[36], stats[37], stats[38]]
                
            if value == 'Jun 25th 2021':
                surface_forms = stats[74]
                mean = stats[79]
                median = 'Cyropaedia'
                std_dev = stats[81]
                top_file = R.top_2021_06_sfAndTotalCounts_en
                values = [stats[75], stats[76], stats[77], stats[78]]
                
            mode = top_file['Surface form'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº surface forms"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Intermediate surface form (median)"), html.H4(median)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("Surface form that appears the most (mode)"), html.H4(mode)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            
            figure_container = html.Div([
            html.H4("Surface forms"),
            dcc.Graph(id='es_pie', figure=F.get_sfpie_figure(values), style={'height':'19.53125vw', 'width':'45.572916666666664vw'})
            ])
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="en_sfAndTotalCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '44.270833333333336vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Br(), figure_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container        
        