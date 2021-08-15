# -*- coding: utf-8 -*-
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_table import DataTable
import resources as R
import figures as F


def initialize_callbacks(app):
     # Details Tab callback
     @app.callback(dash.dependencies.Output('subtabs', 'value'),
              [dash.dependencies.Input('tabs', 'value')])
     def switch_tab(value):
             if value == "details":
                 return "summary"
             else:
                 return dash.no_update
             
     # Comparison callback - table
     @app.callback(
    dash.dependencies.Output('data_container', 'children'),
    [dash.dependencies.Input('version1_dropdown', 'value'),
     dash.dependencies.Input('version2_dropdown', 'value'),
     dash.dependencies.Input('lang_dropdown', 'value')])
     def version_data(value1, value2, lang_value):
        if lang_value is None or value1 is None or value2 is None:
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
            
            if entities_version1 < entities_version2:
                ent_sign = '+'
           
            elif entities_version1 == entities_version2:
                ent_sign = ''
            else:
                ent_sign = '-'
           
            if types_version1 < types_version2:
                typ_sign = '+'
            elif types_version1 == types_version2:
                typ_sign = ''
            else:
                typ_sign = '-'
                
            entity_growth_text = ' (' + ent_sign + str(entity_growth) + ')'
            type_growth_text = ' (' + typ_sign + str(type_growth) + ')'
            entity_growth_text = F.color_brackets(entity_growth_text)
            type_growth_text = F.color_brackets(type_growth_text)
            
            version_container=  html.Div(id='version_container', children = [
               DataTable(
            id="comparison_table",
            columns=[{"name": "Version", "id": "Version"},
                     {"name": "Nº entities", "id": "Nº entities", "presentation": "markdown"},
                      {"name": "Nº types", "id": "Nº types", "presentation": "markdown"}
                      ],
            css=[dict(selector="p", rule="margin: 0px; text-align: left;")],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
           style_cell={'text-align': 'center'},
            data=[
        {
            "Version": value1,
            "Nº entities": entities_version1,
            "Nº types": types_version1,
            
        },
        {
            "Version": value2,
            "Nº entities": entities_version2 + entity_growth_text ,
            "Nº types": types_version2 + type_growth_text,
        }
        ],
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '8.138020833333334vw', 'width': '97.65625vw', 'margin-left': '0.6510416666666666vw'
                         },
             markdown_options={"html": True}
        ),
                ]
                )
            
            title = html.H3("Version comparison")
            return title, version_container
    
    
# Comparison callback - figures
     @app.callback(
    dash.dependencies.Output('figures_container', 'children'),
    [dash.dependencies.Input('version1_dropdown', 'value'),
     dash.dependencies.Input('version2_dropdown', 'value'),
     dash.dependencies.Input('lang_dropdown', 'value')])
     def version_figures(value1, value2, lang_value):
        if lang_value is None or value1 is None or value2 is None:
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
            return title, html.Br(), bar_graph, pie_graph, html.Hr(), type_title, types_container 

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
            if lang_value is None or value1 is None or value2 is None:
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
             
    # Summary callback
     @app.callback(
    dash.dependencies.Output('summary_container', 'children'),
    [dash.dependencies.Input('summary_language_dropdown', 'value'),
     dash.dependencies.Input('summary_version_dropdown', 'value')])
     def summary(languaje, version):
        if languaje is None or version is None:
            return dash.no_update
        else:
            versions_stats = R.versions_stats
            if languaje == 'Spanish':
                stats = R.es_stats
                if version == 'Oct 2016':
                   it_elements = versions_stats[1]
                   it_mean = versions_stats[2]
                   #it_median = 'dbo:Insect'
                   it_mode = 'dbo:Location'
                   it_std_dev = versions_stats[4]
                   uri_elements = stats[42]
                   uri_mean = stats[43]
                  # uri_median = 'dbpedia-es:Hinduismo'
                   uri_mode = 'dbpedia-es:' + R.top_2016_uriCounts_es['DBpedia entity'].iloc[0]
                   uri_std_dev = stats[45]
                   pair_elements = stats[46]
                   pair_mean = stats[47]
                   #pair_median = '[hinduista - dbpedia-es:Hinduismo]'
                   pair_mode =  "[" + R.top_2016_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2016_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                   pair_std_dev = stats[49]
                   token_elements = stats[50]
                   token_mean = stats[51]
                   #token_median = 'http://es.wikipedia.org/wiki/Imperio_almohade'
                   token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_es['Wikipedia article'].iloc[0]
                   token_std_dev = stats[52]
                   sf_elements = stats[54]
                   sf_mean = stats[59]
                   #sf_median = 'doris miller'
                   sf_mode =  R.top_2016_sfAndTotalCounts_es['Surface form'].iloc[0]
                   sf_std_dev = stats[61]
                
                if version == 'Oct 2020':
                    it_elements = versions_stats[19]
                    it_mean = versions_stats[20]
                    it_std_dev = versions_stats[22]
                    it_mode = 'dbo:Location'
                    #it_median = 'dbo:Person'
                    uri_elements = stats[82]
                    uri_mean = stats[83]
                    #uri_median = 'dbpedia-es:Huiracocha_Inca'
                    uri_mode = 'dbpedia-es:' + R.top_2020_uriCounts_es['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[85]
                    pair_elements = stats[86]
                    pair_mean = stats[87]
                    #pair_median = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
                    pair_mode =  "[" + R.top_2020_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2020_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[89]
                    token_elements = stats[90]
                    token_mean = stats[91]
                    #token_median = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
                    token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_es['Wikipedia article'].iloc[0]
                    token_std_dev = stats[92]
                    sf_elements = stats[94]
                    sf_mean = stats[99]
                    #sf_median = 'Ciudad del Vaticano'
                    sf_mode =  R.top_2020_sfAndTotalCounts_es['Surface form'].iloc[0]
                    sf_std_dev = stats[101]
                   
        
                if version == 'May 2021':
                    it_elements = versions_stats[37]
                    it_mean = versions_stats[38]
                    it_std_dev = versions_stats[40]
                    it_mode = 'dbo:Location'
                   # it_median = 'dbo:Person'
                    uri_elements = stats[22]
                    uri_mean = stats[23]
                    #uri_median = 'dbpedia-es:III_milenio_a._C.'
                    uri_mode = 'dbpedia-es:' + R.top_2021_05_uriCounts_es['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[25]
                    pair_elements = stats[26]
                    pair_mean = stats[27]
                   # pair_median = '[ambiente - dbpedia-es:Hábitat]'
                    pair_mode =  "[" + R.top_2021_05_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_05_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[29]
                    token_elements = stats[30]
                    token_mean = stats[31]
                    #token_median = 'http://es.wikipedia.org/wiki/Impunidad'
                    token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_es['Wikipedia article'].iloc[0]
                    token_std_dev = stats[32]
                    sf_elements = stats[34]
                    sf_mean = stats[39]
                   #sf_median = 'pulmonar'
                    sf_mode =  R.top_2021_05_sfAndTotalCounts_es['Surface form'].iloc[0]
                    sf_std_dev = stats[41]
                   
                if version == 'Jun 2021':
                    it_elements = versions_stats[55]
                    it_mean = versions_stats[56]
                    it_std_dev = versions_stats[58]
                    it_mode = 'dbo:Location'
                    #it_median = 'dbo:Person'
                    uri_elements = stats[62]
                    uri_mean = stats[63]
                   # uri_median = 'dbpedia-es:ITunes_Store'
                    uri_mode = 'dbpedia-es:' + R.top_2021_06_uriCounts_es['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[65]
                    pair_elements = stats[66]
                    pair_mean = stats[67]
                    #pair_median = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
                    pair_mode =  "[" + R.top_2021_06_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_06_pairCounts_es['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[69]
                    token_elements = stats[70]
                    token_mean = stats[71]
                   # token_median = 'http://es.wikipedia.org/wiki/Invierno'
                    token_mode = 'http://es.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_es['Wikipedia article'].iloc[0]
                    token_std_dev = stats[72]
                    sf_elements = stats[74]
                    sf_mean = stats[79]
                   # sf_median = 'culebrera europea'
                    sf_mode =  R.top_2021_06_sfAndTotalCounts_es['Surface form'].iloc[0]
                    sf_std_dev = stats[81]
            
            if languaje == 'English':
                stats = R.en_stats
                if version == 'Oct 2016':
                   it_elements = versions_stats[73]
                   it_mean = versions_stats[74]
                   #it_median = 'dbo:PersonFunction'
                   it_mode = 'dbo:CareerStation'
                   it_std_dev = versions_stats[76] 
                   uri_elements = stats[42]
                   uri_mean = stats[43]
                   #uri_median = 'dbr:Latvian_constitutional_referendum,_2008'
                   uri_mode = 'dbr:' + R.top_2016_uriCounts_en['DBpedia entity'].iloc[0]
                   uri_std_dev = stats[45]
                   pair_elements = stats[46]
                   pair_mean = stats[47]
                   #pair_median = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
                   pair_mode =  "[" + R.top_2016_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2016_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                   pair_std_dev = stats[49]
                   token_elements = stats[50]
                   token_mean = stats[51]
                   #token_median = 'http://en.wikipedia.org/wiki/Kushti'
                   token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_en['Wikipedia article'].iloc[0]
                   token_std_dev = stats[52]
                   sf_elements = stats[54]
                   sf_mean = stats[59]
                   #sf_median = 'Deep Cove'
                   sf_mode =  R.top_2016_sfAndTotalCounts_en['Surface form'].iloc[0]
                   sf_std_dev = stats[61]
                
                if version == 'Oct 2020':
                    it_elements = versions_stats[91]
                    it_mean = versions_stats[92]
                    it_std_dev = versions_stats[94]
                    #it_median = 'dbo:Person'
                    it_mode = 'dbo:CareerStation'
                    uri_elements = stats[82]
                    uri_mean = stats[83]
                    #uri_median = 'dbr:Lamar_University'
                    uri_mode = 'dbr:' + R.top_2020_uriCounts_en['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[85]
                    pair_elements = stats[86]
                    pair_mean = stats[87]
                    #pair_median = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
                    pair_mode =  "[" + R.top_2020_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2020_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[89]
                    token_elements = stats[90]
                    token_mean = stats[91]
                    #token_median = 'http://en.wikipedia.org/wiki/Klondike_Open'
                    token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_en['Wikipedia article'].iloc[0]
                    token_std_dev = stats[92]
                    sf_elements = stats[94]
                    sf_mean = stats[99]
                    #sf_median = 'The Herald'
                    sf_mode =  R.top_2020_sfAndTotalCounts_en['Surface form'].iloc[0]
                    sf_std_dev = stats[101]
                   
        
                if version == 'May 2021':
                    it_elements = versions_stats[109]
                    it_mean = versions_stats[110]
                    it_std_dev = versions_stats[112]
                    #it_median = 'dbo:Person'
                    it_mode = 'dbo:CareerStation'
                    uri_elements = stats[22]
                    uri_mean = stats[23]
                   # uri_median = 'dbr:Kyrgyzstan_national_football_team'
                    uri_mode = 'dbr:' + R.top_2021_05_uriCounts_en['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[25]
                    pair_elements = stats[26]
                    pair_mean = stats[27]
                    #pair_median = '[Wallenpaupack - dbr:Lake_Wallenpaupack]'
                    pair_mode =  "[" + R.top_2021_05_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_05_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[29]
                    token_elements = stats[30]
                    token_mean = stats[31]
                    #token_median = 'http://en.wikipedia.org/wiki/Klas_Lund'
                    token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_en['Wikipedia article'].iloc[0]
                    token_std_dev = stats[32]
                    sf_elements = stats[34]
                    sf_mean = stats[39]
                    #sf_median = 'DC Comics'
                    sf_mode =  R.top_2021_05_sfAndTotalCounts_en['Surface form'].iloc[0]
                    sf_std_dev = stats[41]
                   
                if version == 'Jun 2021':
                    it_elements = versions_stats[127]
                    it_mean = versions_stats[128]
                    it_std_dev = versions_stats[130]
                    #it_median = 'dbo:PersonFunction'
                    it_mode = 'dbo:CareerStation'
                    uri_elements = stats[62]
                    uri_mean = stats[63]
                    #uri_median = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
                    uri_mode = 'dbr:' + R.top_2021_06_uriCounts_en['DBpedia entity'].iloc[0]
                    uri_std_dev = stats[65]
                    pair_elements = stats[66]
                    pair_mean = stats[67]
                    #pair_median = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
                    pair_mode =  "[" + R.top_2021_06_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_06_pairCounts_en['DBpedia entity'].iloc[0] + "]"
                    pair_std_dev = stats[69]
                    token_elements = stats[70]
                    token_mean = stats[71]
                    #token_median = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
                    token_mode = 'http://en.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_en['Wikipedia article'].iloc[0]
                    token_std_dev = stats[72]
                    sf_elements = stats[74]
                    sf_mean = stats[79]
                    #sf_median = 'Cyropaedia'
                    sf_mode =  R.top_2021_06_sfAndTotalCounts_en['Surface form'].iloc[0]
                    sf_std_dev = stats[81]
                
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="summary_table",
           columns=[
        {"name": ["", "File"], "id": "file"},
        {"name": ["", "Nº elements"], "id": "elements"},
        {"name": ["Measures of central tendency", "Mean"], "id": "mean"},
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
            "file": "Instance-types",
            "elements": it_elements,
            "mean": it_mean,
            "mode":it_mode,
            "std_dev": it_std_dev,
        },
        {
            "file": "uriCounts",
            "elements": uri_elements,
            "mean": uri_mean,
            "mode": uri_mode,
            "std_dev": uri_std_dev,
        },
        {
            "file": "pairCounts",
            "elements": pair_elements,
            "mean": pair_mean,
            "mode": pair_mode,
            "std_dev": pair_std_dev,
        },
        {
            "file": "tokenCounts",
            "elements": token_elements,
            "mean": token_mean,
            "mode": token_mode,
            "std_dev": token_std_dev,
        },
        {
            "file": "sfAndTotalCounts",
            "elements": sf_elements,
            "mean": sf_mean,
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
    
      # Instance-types callback
     @app.callback(
    dash.dependencies.Output('types_container', 'children'),
    [dash.dependencies.Input('types_language_dropdown', 'value')])
     def instance_types(language):
         if language is None:
             return dash.no_update
         if language == 'Spanish':
             types_container = html.Div([html.Div(children=[
        dcc.Markdown('''
    In this tab are displayed:
    
     1. Calculated measures from instance-types, redirects and disambiguations datasets obtained from the `DBpedia Extraction Framework`
     2. Calculated measures from the instance-types that `DBpedia Spotlight` actually uses (`known types`) after the entity validation process (check the `Information` tab for more details about entity validation)
   
   `NOTE`: All the statistics have been calculated for non-cumulative data, that is, for the leaves of the branches of the DBpedia class hierarchy [http://mappings.dbpedia.org/server/ontology/classes/]
   
   `NOTE`: Only `May 2021` version is available for instance-types since the entity validation process takes a considerable amount of time and it has not been possible to do it for the other versions.
            
                         '''),
        html.Hr(),                 
        html.H3(html.B("DBpedia Extraction Framework"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),
        html.Br(),
        html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia entities"), html.H4(R.versions_stats[36])]
                                         ),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia types"), html.H4(R.versions_stats[37])] 
                                         ), style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
         html.Br(),
         html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº redirects"), html.H4(R.es_stats[0])] 
                                         ),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.H5("Nº disambiguations"), html.H4(R.es_stats[1])] 
                                         ),style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
          html.Hr(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.versions_stats[38])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Location')]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(R.versions_stats[40])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Hr(),
          html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontologyy', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='instance_types', figure=F.es_instance_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'52.083333333333336vw', 'display': 'inline-block'})]
            )]),
         html.Hr(),
         html.Div([html.H3(html.B("DBpedia Spotlight"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),      
         html.Br(),
         html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia entities"), html.H4(R.es_stats[2])] 
                                         ),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia types"), html.H4(R.es_stats[3])]),
                  style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5')]),
         html.Hr(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.es_stats[4])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Location')]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(R.es_stats[6])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Hr(),
          dcc.Graph(id='statistics', figure=F.es_statistics_figure),
          html.Hr(),
        html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontology', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='known_types', figure=F.es_known_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'52.083333333333336vw', 'display': 'inline-block'})]
            ),
        html.Hr(),
        html.H4("Position measures for DBpedia types"),
         dcc.Markdown('''
              The following chart presents the quartile and percentile information about 
              the instance-types, ordered from highest to lowest number of entities and 
              considering leaf nodes from the hierarchy [http://mappings.dbpedia.org/server/ontology/classes/] 
              (internal nodes are considered only for those cases in which the instance has not assigned a leaf node). 
              According to the chart, quartile 1 contains the most representative instances (instances with high frequency), 
              as the instances move away from the origin they will have less representativeness (the instance frequency decreased).
                         '''),
        dcc.Graph(id='known_types_pos', figure=F.es_pos_known_types_figure, 
             style={'height':'32.552083333333336vw', 'width':'65.10416666666667vw'}),
        html.Hr(),
        html.H4("Top 50 DBpedia types with more entities"),
        dcc.Markdown('''
    The following list is based on the `Entities by DBpedia Types` information.
            
                         '''),
        DataTable(
            id="top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
             css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=R.top_known_types_2021_05_es.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '27.669270833333332vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
             
         if language == 'English':
              types_container = html.Div([         
        dcc.Markdown('''
    In this tab are displayed:
    
     1. Calculated measures from instance-types, redirects and disambiguations datasets obtained from the `DBpedia Extraction Framework`
     2. Calculated measures from the instance-types that `DBpedia Spotlight` actually uses (`known types`) after the entity validation process (check the `Information` tab for more details about entity validation)
   
   `NOTE`: All the statistics have been calculated for non-cumulative data, that is, for the leaves of the branches of the DBpedia class hierarchy [http://mappings.dbpedia.org/server/ontology/classes/]
   
   `NOTE`: Only `May 2021` version is available for instance-types since the entity validation process takes a considerable amount of time and it has not been possible to do it for the other versions.
            
                         '''),
        html.Hr(),
        html.Div(children=[html.H3(html.B("DBpedia Extraction Framework"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),
        html.Br(),
        html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia entities"), html.H4(R.versions_stats[108])]
                                         ),style={'display': 'inline-block'}, color="#F5F5F5"),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia types"), html.H4(R.versions_stats[109])] 
                                         ), style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),  
          html.Br(),
          html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº redirects"), html.H4(R.en_stats[0])] 
                                         ),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.H5("Nº disambiguations"), html.H4(R.en_stats[1])] 
                                         ),style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5'),
          html.Hr(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.versions_stats[110])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Location')]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(R.versions_stats[112])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Hr(),
          html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontologyy', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='instance_types', figure=F.en_instance_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'52.083333333333336vw', 'display': 'inline-block'})]
            )]),
         html.Hr(),
         html.Div([html.H3(html.B("DBpedia Spotlight"), style={'display': 'inline-block', "border-bottom":"0.13020833333333334vw black solid", 'width': 'auto'}),      
         html.Br(),        
         html.Br(),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia entities"), html.H4(R.en_stats[2])] 
                                         ),style={'display': 'inline-block'}, color='#F5F5F5'),
         dbc.Card(dbc.CardBody([html.H5("Nº DBpedia types"), html.H4(R.en_stats[3])]),
                  style={'display': 'inline-block', "margin-left": "1.953125vw"}, color='#F5F5F5')]),
          html.Hr(),
          html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       [html.H5("Nº entities per DBpedia type (mean)"), html.H4(R.en_stats[4])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        [html.H5("DBpedia type that appears the most (mode)"), html.H4('dbo:Location')]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(R.en_stats[6])]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
          html.Hr(),
          dcc.Graph(id='statistics', figure=F.en_statistics_figure),
          html.Hr(),
        html.Div(children=[html.H4("Entities by DBpedia types"),
           dcc.Graph(id='ontology', figure=F.ontology_figure, style={'height':'26.041666666666668vw', 'width':'39.0625vw', 'display': 'inline-block'}),
           dcc.Graph(id='known_types', figure=F.en_known_types_figure, 
                                   style={'height':'26.041666666666668vw', 'width':'52.083333333333336vw', 'display': 'inline-block'})]
            ),
        html.Hr(),
        html.H4("Position measures for DBpedia types"),
        dcc.Markdown('''
              The following chart presents the quartile and percentile information about 
              the instance-types, ordered from highest to lowest number of entities and 
              considering leaf nodes from the hierarchy [http://mappings.dbpedia.org/server/ontology/classes/] 
              (internal nodes are considered only for those cases in which the instance has not assigned a leaf node). 
              According to the chart, quartile 1 contains the most representative instances (instances with high frequency), 
              as the instances move away from the origin they will have less representativeness (the instance frequency decreased).
                         '''),
         dcc.Graph(id='known_types_pos', figure=F.en_pos_known_types_figure, 
           style={'height':'32.552083333333336vw', 'width':'65.10416666666667vw'}),
        html.Hr(),
        html.H4("Top 50 DBpedia types with more entities"),
        dcc.Markdown('''
    The following list is based on the `Entities by DBpedia Types` information.
            
                         '''),
        DataTable(
            id="top_known_types_table",
            columns=[{"name": "DBpedia type", "id": "DBpedia type"},
                     {"name": "Nº entities", "id": "Nº entities"}],
             css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=R.top_known_types_2021_05_en.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': '24.4140625vw', 'margin-left': '0.6510416666666666vw'
                         }
        )])
         return types_container
        
    # Known types bar callback
     @app.callback(
            dash.dependencies.Output('known_types', 'figure'),
            [dash.dependencies.Input('ontology', 'clickData'),
             dash.dependencies.Input('types_language_dropdown', 'value')]
            )
     def update_known_types_bar(clicked_data, language):
            selected_type = 'owlThing'
            if language == 'Spanish':
                types_count_df = R.known_types_es_2021_05_01
            if language == 'English':
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
            figure.add_vline(x=float(R.es_stats[4]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.es_stats[6]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.es_stats[4])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[4]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[6])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[6]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # Instance types bar callback
     @app.callback(
            dash.dependencies.Output('instance_types', 'figure'),
            [dash.dependencies.Input('ontologyy', 'clickData'),
             dash.dependencies.Input('types_language_dropdown', 'value')]
            )
     def update_instance_types_bar(clicked_data, language):
            selected_type = 'owlThing'
            if language == 'Spanish':
                mean = R.versions_stats[38]
                std_dev = R.versions_stats[40]
                types_count_df = R.instance_types_es_2021_05_01
            if language == 'English':
                mean = R.versions_stats[110]
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
            figure.add_vline(x=float(std_dev), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
            go.Scatter(x=[float(mean)], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[mean], hoverinfo="text"),
            go.Scatter(x=[float(std_dev)], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[std_dev], hoverinfo="text")
            ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
# uriCounts callback
     @app.callback(
    dash.dependencies.Output('uriCounts_container', 'children'),
    [dash.dependencies.Input('uriCounts_language_dropdown', 'value'),
     dash.dependencies.Input('uriCounts_version_dropdown', 'value')])
     def uriCounts(language, version):
        if version is None or language is None:
            return dash.no_update
        else:
            if language == 'Spanish':
                stats = R.es_stats
                width = '29.296875vw'
                prefix = 'dbpedia-es:'
                if version == 'Oct 2016':
                    dbpedia_entities = stats[42]
                    mean = stats[43]
                    median = 'dbpedia-es:Hinduismo'
                    std_dev = stats[45]
                    top_file = R.top_2016_uriCounts_es
                
                if version == 'Oct 2020':
                    dbpedia_entities = stats[82]
                    mean = stats[83]
                    median = 'dbpedia-es:Huiracocha_Inca'
                    std_dev = stats[85]
                    top_file = R.top_2020_uriCounts_es
        
                if version == 'May 2021':
                    dbpedia_entities = stats[22]
                    mean = stats[23]
                    median = 'dbpedia-es:III_milenio_a._C.'
                    std_dev = stats[25]
                    top_file = R.top_2021_05_uriCounts_es
                    
                if version == 'Jun 2021':
                    dbpedia_entities = stats[62]
                    mean = stats[63]
                    median = 'dbpedia-es:ITunes_Store'
                    std_dev = stats[65]
                    top_file = R.top_2021_06_uriCounts_es
               
            if language == 'English':
                stats = R.en_stats
                width = '32.552083333333336vw'
                prefix = 'dbr:'
                if version == 'Oct 2016':
                    dbpedia_entities = stats[42]
                    mean = stats[43]
                    median = 'dbr:Latvian_constitutional_referendum,_2008'
                    std_dev = stats[45]
                    top_file = R.top_2016_uriCounts_en
                
                if version == 'Oct 2020':
                    dbpedia_entities = stats[82]
                    mean = stats[83]
                    median = 'dbr:Lamar_University'
                    std_dev = stats[85]
                    top_file = R.top_2020_uriCounts_en
        
                if version == 'May 2021':
                    dbpedia_entities = stats[22]
                    mean = stats[23]
                    median = 'dbr:Kyrgyzstan_national_football_team'
                    std_dev = stats[25]
                    top_file = R.top_2021_05_uriCounts_en
                    
                if version == 'Jun 2021':
                    dbpedia_entities = stats[62]
                    mean = stats[63]
                    median = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
                    std_dev = stats[65]
                    top_file = R.top_2021_06_uriCounts_en
                
            mode = prefix + top_file['DBpedia entity'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº DBpedia entities"), html.H4(dbpedia_entities)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
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
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
        
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }
        ],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': width, 'margin-left': '0.6510416666666666vw'
                         }
        )])
    
        return cards_container, html.Hr(), html.H4("Top 50 most frequent entities"), table_container  
        
# pairCounts callback
     @app.callback(
    dash.dependencies.Output('pairCounts_container', 'children'),
    [dash.dependencies.Input('pairCounts_language_dropdown', 'value')
     ,dash.dependencies.Input('pairCounts_version_dropdown', 'value')])
     def pairCounts(language, version):
        if version is None or language is None:
            return dash.no_update
        else:
            if language == 'Spanish':
                stats = R.es_stats
                width = '33.854166666666664vw'
                prefix = 'dbpedia-es:'
                if version == 'Oct 2016':
                    surface_forms = stats[46]
                    mean = stats[47]
                    median = '[hinduista - dbpedia-es:Hinduismo]'
                    std_dev = stats[49]
                    top_file = R.top_2016_pairCounts_es
        
                if version == 'Oct 2020':
                    surface_forms = stats[86]
                    mean = stats[87]
                    median = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
                    std_dev = stats[89]
                    top_file = R.top_2020_pairCounts_es
        
                if version == 'May 2021':
                    surface_forms = stats[26]
                    mean = stats[27]
                    median = '[ambiente - dbpedia-es:Hábitat]'
                    std_dev = stats[29]
                    top_file = R.top_2021_05_pairCounts_es
                    
                if version == 'Jun 2021':
                    surface_forms = stats[66]
                    mean = stats[67]
                    median = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
                    std_dev = stats[69]
                    top_file = R.top_2021_06_pairCounts_es
            if language == 'English':
                stats = R.en_stats
                prefix = 'dbr:'
                width = '52.083333333333336vw'
                if version == 'Oct 2016':
                    surface_forms = stats[46]
                    mean = stats[47]
                    median = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
                    std_dev = stats[49]
                    top_file = R.top_2016_pairCounts_en
        
                if version == 'Oct 2020':
                    surface_forms = stats[86]
                    mean = stats[87]
                    median = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
                    std_dev = stats[89]
                    top_file = R.top_2020_pairCounts_en
        
                if version == 'May 2021':
                    surface_forms = stats[26]
                    mean = stats[27]
                    median = '[Wallenpaupack -dbr:Lake_Wallenpaupack]'
                    std_dev = stats[29]
                    top_file = R.top_2021_05_pairCounts_en
                    
                if version == 'Jun 2021':
                    surface_forms = stats[66]
                    mean = stats[67]
                    median = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
                    std_dev = stats[69]
                    top_file = R.top_2021_06_pairCounts_en
                
            mode = "[" + top_file['Surface form'].iloc[0] + " - " + prefix + top_file['DBpedia entity'].iloc[0] + "]"
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº [Surface form - DBpedia entity] pairs"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
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
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
             css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }],
            style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': width , 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Hr(), html.H4("Top 50 most linked surface forms"), table_container

# tokenCounts callback
     @app.callback(
    dash.dependencies.Output('tokenCounts_container', 'children'),
    [dash.dependencies.Input('tokenCounts_language_dropdown', 'value'),
     dash.dependencies.Input('tokenCounts_version_dropdown', 'value')])
     def tokenCounts(language, version):
        if version is None or language is None:
            return dash.no_update
        else:
            if language == 'Spanish':
                stats = R.es_stats
                width = '30.924479166666668vw'   
                prefix = 'http://es.wikipedia.org/wiki/'
                if version == 'Oct 2016':
                    articles = stats[50]
                    mean = stats[51]
                    median = 'http://es.wikipedia.org/wiki/Imperio_almohade'
                    std_dev = stats[52]
                    top_file = R.top_2016_tokenCounts_es
                    
                if version == 'Oct 2020':
                    articles = stats[70]
                    mean = stats[71]
                    median = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
                    std_dev = stats[72]
                    top_file = R.top_2020_tokenCounts_es
        
                if version == 'May 2021':
                    articles = stats[30]
                    mean = stats[31]
                    median = 'http://es.wikipedia.org/wiki/Impunidad'
                    std_dev = stats[32]
                    top_file = R.top_2021_05_tokenCounts_es
                    
                if version == 'Jun 2021':
                    articles = stats[70]
                    mean = stats[71]
                    median = 'http://es.wikipedia.org/wiki/Invierno'
                    std_dev = stats[72]
                    top_file = R.top_2021_06_tokenCounts_es
            
            if language == 'English':
                stats = R.en_stats
                width = '35.15625vw'   
                prefix = 'http://en.wikipedia.org/wiki/'
                if version == 'Oct 2016':
                    articles = stats[50]
                    mean = stats[51]
                    median = 'http://en.wikipedia.org/wiki/Kushti'
                    std_dev = stats[52]
                    top_file = R.top_2016_tokenCounts_en
                    
                if version == 'Oct 2020':
                    articles = stats[70]
                    mean = stats[71]
                    median = 'http://en.wikipedia.org/wiki/Klondike_Open'
                    std_dev = stats[72]
                    top_file = R.top_2020_tokenCounts_en
        
                if version == 'May 2021':
                    articles = stats[30]
                    mean = stats[31]
                    median = 'http://en.wikipedia.org/wiki/Klas_Lund'
                    std_dev = stats[32]
                    top_file = R.top_2021_05_tokenCounts_en
                    
                if version == 'Jun 2021':
                    articles = stats[70]
                    mean = stats[71]
                    median = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
                    std_dev = stats[72]
                    top_file = R.top_2021_06_tokenCounts_en
                
            mode = prefix + top_file['Wikipedia article'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº Wikipedia articles"), html.H4(articles)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
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
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="tokenCounts_table",
           columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
            css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': width, 'margin-left': '0.6510416666666666vw'
                         }
        )])
            return cards_container, html.Hr(), html.H4("Top 50 Wikipedia articles with more tokens"), table_container

# sfAndTotalCounts callback
     @app.callback(
    dash.dependencies.Output('sfAndTotalCounts_container', 'children'),
    [dash.dependencies.Input('sfAndTotalCounts_language_dropdown', 'value'),
     dash.dependencies.Input('sfAndTotalCounts_version_dropdown', 'value')])
     def sfAndTotalCounts(language, version):
        if version is None or language is None:
            return dash.no_update
        else:
            if language == 'Spanish':
                stats = R.es_stats
                width = '32.552083333333336vw' 
                if version == 'Oct 2016':
                    surface_forms = stats[54]
                    mean = stats[59]
                    median = 'doris miller'
                    std_dev = stats[61]
                    top_file = R.top_2016_sfAndTotalCounts_es
                    versions = [stats[55], stats[56], stats[57], stats[58]]
                    
                if version == 'Oct 2020':
                    surface_forms = stats[94]
                    mean = stats[99]
                    median = 'Ciudad del Vaticano'
                    std_dev = stats[101]
                    top_file = R.top_2020_sfAndTotalCounts_es
                    versions = [stats[95], stats[96], stats[97], stats[98]]
        
                if version == 'May 2021':
                    surface_forms = stats[34]
                    mean = stats[39]
                    median = 'pulmonar'
                    std_dev = stats[41]
                    top_file = R.top_2021_05_sfAndTotalCounts_es
                    versions = [stats[35], stats[36], stats[37], stats[38]]
                    
                if version == 'Jun 2021':
                    surface_forms = stats[74]
                    mean = stats[79]
                    median = 'culebrera europea'
                    std_dev = stats[81]
                    top_file = R.top_2021_06_sfAndTotalCounts_es
                    versions = [stats[75], stats[76], stats[77], stats[78]]
            
            if language == 'English':
                    stats = R.en_stats
                    width = '44.270833333333336vw' 
                    if version == 'Oct 2016':
                        surface_forms = stats[54]
                        mean = stats[59]
                        median = 'Deep Cove'
                        std_dev = stats[61]
                        top_file = R.top_2016_sfAndTotalCounts_en
                        versions = [stats[55], stats[56], stats[57], stats[58]]
                        
                    if version == 'Oct 2020':
                        surface_forms = stats[94]
                        mean = stats[99]
                        median = 'The Herald'
                        std_dev = stats[101]
                        top_file = R.top_2020_sfAndTotalCounts_en
                        versions = [stats[95], stats[96], stats[97], stats[98]]
            
                    if version == 'May 2021':
                        surface_forms = stats[34]
                        mean = stats[39]
                        median = 'DC Comics'
                        std_dev = stats[41]
                        top_file = R.top_2021_05_sfAndTotalCounts_en
                        versions = [stats[35], stats[36], stats[37], stats[38]]
                        
                    if version == 'Jun 2021':
                        surface_forms = stats[74]
                        mean = stats[79]
                        median = 'Cyropaedia'
                        std_dev = stats[81]
                        top_file = R.top_2021_06_sfAndTotalCounts_en
                        versions = [stats[75], stats[76], stats[77], stats[78]]
                
            mode = top_file['Surface form'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        [html.H5("Nº surface forms"), html.H4(surface_forms)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Hr(),
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
                html.Hr(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         [html.H5("Standard deviation"), html.H4(std_dev)]
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            
            figure_container = html.Div([
            html.H4("Surface forms"),
            dcc.Graph(id='pie', figure=F.get_sfpie_figure(versions), style={'height':'19.53125vw', 'width':'45.572916666666664vw'})
            ])   
            table_container = html.Div(id='table_container', children = [
        DataTable(
            id="sfAndTotalCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            css=[
            {
                'selector': 'table',
                'rule': 'width: 100%;'
            }],
           style_header=
           {
              'fontWeight': 'bold',
              'font-size': '1.1067708333333333vw',
              'text-align': 'center'
           },
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': '26.041666666666668vw', 'width': width, 'margin-left': '0.6510416666666666vw'
                         }
        )])
            
            return cards_container, html.Hr(), figure_container, html.Hr(), html.H4("Top 50 most linked surface forms"), table_container
     
     # Language dropdowns sync   
     @app.callback(
        [dash.dependencies.Output('summary_language_dropdown', 'value'),
        dash.dependencies.Output('types_language_dropdown', 'value'), 
        dash.dependencies.Output('uriCounts_language_dropdown', 'value'), 
        dash.dependencies.Output('pairCounts_language_dropdown', 'value'),
        dash.dependencies.Output('tokenCounts_language_dropdown', 'value'), 
        dash.dependencies.Output('sfAndTotalCounts_language_dropdown', 'value')
        ],
        [dash.dependencies.Input('summary_language_dropdown', 'value'),
        dash.dependencies.Input('types_language_dropdown', 'value'), 
        dash.dependencies.Input('uriCounts_language_dropdown', 'value'), 
        dash.dependencies.Input('pairCounts_language_dropdown', 'value'),
        dash.dependencies.Input('tokenCounts_language_dropdown', 'value'), 
        dash.dependencies.Input('sfAndTotalCounts_language_dropdown', 'value')]
    )
     def sync_language_dropdowns(sum_lang, types_lang,
                                 uri_lang, pair_lang, token_lang, sf_lang):
        ctx = dash.callback_context
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if input_id == 'summary_language_dropdown':
            return dash.no_update, sum_lang, sum_lang, sum_lang, sum_lang, sum_lang
        elif input_id == 'types_language_dropdown':
            return types_lang, dash.no_update, types_lang, types_lang, types_lang, types_lang
        elif input_id == 'uriCounts_language_dropdown':
            return uri_lang, uri_lang, dash.no_update, uri_lang, uri_lang, uri_lang
        elif input_id == 'pairCounts_language_dropdown':
            return pair_lang, pair_lang, pair_lang, dash.no_update, pair_lang, pair_lang
        elif input_id == 'tokenCounts_language_dropdown':
            return token_lang, token_lang, token_lang, token_lang, dash.no_update, token_lang
        else:
           return sf_lang, sf_lang, sf_lang, sf_lang, sf_lang, dash.no_update
     
       # Version dropdowns sync  
     @app.callback(
        [dash.dependencies.Output('summary_version_dropdown', 'value'),
        dash.dependencies.Output('uriCounts_version_dropdown', 'value'), 
        dash.dependencies.Output('pairCounts_version_dropdown', 'value'),
        dash.dependencies.Output('tokenCounts_version_dropdown', 'value'), 
        dash.dependencies.Output('sfAndTotalCounts_version_dropdown', 'value')
        ],
        [dash.dependencies.Input('summary_version_dropdown', 'value'),
        dash.dependencies.Input('uriCounts_version_dropdown', 'value'), 
        dash.dependencies.Input('pairCounts_version_dropdown', 'value'),
        dash.dependencies.Input('tokenCounts_version_dropdown', 'value'), 
        dash.dependencies.Input('sfAndTotalCounts_version_dropdown', 'value')]
    )
     def sync_version_dropdowns(sum_vers,
                                 uri_vers, pair_vers, token_vers, sf_vers):
        ctx = dash.callback_context
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if input_id == 'summary_version_dropdown':
            return dash.no_update, sum_vers, sum_vers, sum_vers, sum_vers
        elif input_id == 'uriCounts_version_dropdown':
            return uri_vers, dash.no_update, uri_vers, uri_vers, uri_vers
        elif input_id == 'pairCounts_version_dropdown':
            return pair_vers, pair_vers, dash.no_update, pair_vers, pair_vers
        elif input_id == 'tokenCounts_version_dropdown':
            return token_vers,token_vers, token_vers, dash.no_update, token_vers
        else:
           return sf_vers, sf_vers, sf_vers, sf_vers, dash.no_update                  
        