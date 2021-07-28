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
     '''
        # Spanish Tab callback
         @app.callback(dash.dependencies.Output('subtabs', 'value'),
              [dash.dependencies.Input('tabs', 'value')])
         def es_switch_tab(value):
             global es_ntimes
             if value == "spanish":
                 return "es_uricounts"
             else:
                 return dash.no_update
             
        # English Tab callback
         @app.callback(dash.dependencies.Output('en-subtabs', 'value'),
              [dash.dependencies.Input('tabs', 'value')])
         def en_switch_tab(value):
             global en_ntimes
             if value == "english":
                 return "en_uricounts"
             else:
                 return dash.no_update
     '''
         
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
                    entities_version1 = versions_stats[2]
                    types_version1 = versions_stats[3]
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[6]
                    types_version1 = versions_stats[7]
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[10]
                    types_version1 = versions_stats[11]
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[14]
                    types_version1 = versions_stats[15]
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[2]
                    types_version2 = versions_stats[3]
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[6]
                    types_version2 = versions_stats[7]
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[10]
                    types_version2 = versions_stats[11]
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[14]
                    types_version2 = versions_stats[15]
            
            if lang_value == 'English':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[18]
                    types_version1 = versions_stats[19]
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[22]
                    types_version1 = versions_stats[23]
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[26]
                    types_version1 = versions_stats[27]
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[30]
                    types_version1 = versions_stats[31]
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[18]
                    types_version2 = versions_stats[19]
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[22]
                    types_version2 = versions_stats[23]
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[26]
                    types_version2 = versions_stats[27]
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[30]
                    types_version2 = versions_stats[31]
                
            entity_growth = abs(int(entities_version1) - int(entities_version2))
            type_growth = abs(int(types_version1) - int(types_version2))
            version1_container = html.Div(id='entity_container', children = [
                html.H4(value1),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia entities"), html.H4(entities_version1)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia types"), html.H4(types_version1)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                )
                ])
                
            version2_container = html.Div(id='type_container', children = [
                html.H4(value2),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia entities"), html.H4(entities_version2)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia types"), html.H4(types_version2)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                )
                ])
            
            growth_container = html.Div(id='growth_container', children = [
            html.H4("Growth between versions"),
            dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Entity growth"), html.H4(str(entity_growth))])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
            dbc.Card(dbc.CardBody(
                html.Div([html.H4("Type growth"), html.H4(str(type_growth))])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                )
                ])
            title = html.H3("Version comparison")
            
            return title, html.Br(), version1_container, html.Br(), version2_container, html.Br(), growth_container
    
    
    
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
                    entities_version1 = versions_stats[2]
                    df1 = R.instance_types_es_2016_10_01
                    
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[6]
                    df1 = R.instance_types_es_2020_10_01
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[10]
                    df1 = R.instance_types_es_2021_05_01
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[14]
                    df1 = R.instance_types_es_2021_06_01
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[2]
                    df2 = R.instance_types_es_2016_10_01
                    
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[6]
                    df2 = R.instance_types_es_2020_10_01
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[10]
                    df2 = R.instance_types_es_2021_05_01
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[14]
                    df2 = R.instance_types_es_2021_06_01
            
            if lang_value == 'English':
                if value1 == 'Oct 1st 2016':
                    entities_version1 = versions_stats[18]
                    df1 = R.instance_types_en_2016_10_01
                if value1 == 'Oct 1st 2020':
                    entities_version1 = versions_stats[22]
                    df1 = R.instance_types_en_2020_10_01
                    
                if value1 == 'May 1st 2021':
                    entities_version1 = versions_stats[26]
                    df1 = R.instance_types_en_2021_05_01
                    
                if value1 == 'June 1st 2021':
                    entities_version1 = versions_stats[30]
                    df1 = R.instance_types_en_2021_06_01
                    
                if value2 == 'Oct 1st 2016':
                    entities_version2 = versions_stats[18]
                    df2 = R.instance_types_en_2016_10_01
                    
                if value2 == 'Oct 1st 2020':
                    entities_version2 = versions_stats[22]
                    df2 = R.instance_types_en_2020_10_01
                    
                if value2 == 'May 1st 2021':
                    entities_version2 = versions_stats[26]
                    df2 = R.instance_types_en_2021_05_01
                    
                if value2 == 'June 1st 2021':
                    entities_version2 = versions_stats[30]
                    df2 = R.instance_types_en_2021_06_01
            
            bar_figure = F.get_version_bar_figure([value1, value2], [entities_version1, entities_version2])
            pie_figure = F.get_version_pie_figure([value1, value2], [entities_version1, entities_version2])
            bar_graph = dcc.Graph(id='versions_bar', figure=bar_figure, style={'display': 'inline-block'})
            pie_graph = dcc.Graph(id='versions_pie', figure=pie_figure, style={'display': 'inline-block'})
            title = html.H3(value1 + " VS " + value2)
            type_title = html.H3("DBpedia types comparison")
            types_container = html.Div([
                dcc.Graph(id='ontology_version', figure=F.ontology_figure, style={'display': 'inline-block'}),
                dcc.Graph(id='instance_types_version', figure=F.get_versions_instance_types_figure([value1, value2], df1, df2), 
                                     style={'display': 'inline-block'})
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
            figure.update_layout(barmode='group', margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure

    # Spanish known types callback
     @app.callback(
            dash.dependencies.Output('es_known_types', 'figure'),
            [dash.dependencies.Input('ontology', 'clickData')]
            )
     def es_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_es
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
            figure.add_vline(x=float(R.es_stats[6]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.es_stats[7]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.es_stats[9]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.es_stats[6])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.es_stats[6]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[7])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[7]], hoverinfo="text"),
                go.Scatter(x=[float(R.es_stats[9])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.es_stats[9]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # Spanish instance types callback
     @app.callback(
            dash.dependencies.Output('es_instance_types', 'figure'),
            [dash.dependencies.Input('ontologyy', 'clickData')]
            )
     def es_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.instance_types_es
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
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
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
            if selected_type in R.known_types_es["DBpedia type"].values:
                selected_row = R.known_types_es[R.known_types_es["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.es_stats[14]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.es_stats[11]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.es_stats[22]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.es_stats[12]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.es_stats[30]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.es_stats[32]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.es_stats[14])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.es_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[11])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.es_stats[11]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[22])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.es_stats[22]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[12])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.es_stats[12]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[30])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.es_stats[30]], hoverinfo="text"),
            go.Scatter(x=[int(R.es_stats[32])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.es_stats[32]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
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
                dbpedia_entities = stats[63]
                mean = stats[64]
                median = 'dbpedia-es:Hinduismo'
                std_dev = stats[67]
                top_file = R.top_2016_uriCounts_es
    
            if value == 'May 25th 2021':
                dbpedia_entities = stats[36]
                mean = stats[37]
                median = 'dbpedia-es:III_milenio_a._C.'
                std_dev = stats[40]
                top_file = R.top_uriCounts_es
                
            mode = 'dbpedia-es:' + top_file['DBpedia entity'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia entities"), html.H4(dbpedia_entities)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº occurrences per DBpedia entity (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate DBpedia entity (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("DBpedia entity that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="es_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 450, 'margin-left': '10px'
                         }
        )])])
    
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
                surface_forms = stats[69]
                mean = stats[70]
                median = '[hinduista - dbpedia-es:Hinduismo]'
                std_dev = stats[73]
                top_file = R.top_2016_pairCounts_es
    
            if value == 'May 25th 2021':
                surface_forms = stats[42]
                mean = stats[43]
                median = '[ambiente - dbpedia-es:Hábitat]'
                std_dev = stats[46]
                top_file = R.top_pairCounts_es
                
            mode = "[" + top_file['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ top_file['DBpedia entity'].iloc[0] + "]"
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº [Surface form - DBpedia entity] pairs"), html.H4(surface_forms)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate pair (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                 dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Pair that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="es_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 520, 'margin-left': '10px'
                         }
        )])])
            
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
                articles = stats[75]
                mean = stats[76]
                median = 'http://es.wikipedia.org/wiki/Imperio_almohade'
                std_dev = stats[78]
                top_file = R.top_2016_tokenCounts_es
    
            if value == 'May 25th 2021':
                articles = stats[48]
                mean = stats[49]
                median = 'http://es.wikipedia.org/wiki/Impunidad'
                std_dev = stats[51]
                top_file = R.top_tokenCounts_es
                
            mode = 'http://es.wikipedia.org/wiki/'+ top_file['Wikipedia article'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº Wikipedia articles"), html.H4(articles)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº tokens per Wikipedia article (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate Wikipedia article (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Wikipedia article that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="es_tokenCounts_table",
           columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 475, 'margin-left': '10px'
                         }
        )])])
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
                surface_forms = stats[80]
                mean = stats[85]
                median = 'doris miller'
                std_dev = stats[88]
                top_file = R.top_2016_sfAndTotalCounts_es
                values = [stats[81], stats[82], stats[83], stats[84]]
    
            if value == 'May 25th 2021':
                surface_forms = stats[53]
                mean = stats[58]
                median = 'pulmonar'
                std_dev = stats[61]
                top_file = R.top_sfAndTotalCounts_es
                values = [stats[54], stats[55], stats[56], stats[57]]
                
            mode = top_file['Surface form'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº surface forms"), html.H4(surface_forms)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate surface form (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Surface form that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            
            figure_container = html.Div([
            html.H4("Surface forms"),
            dcc.Graph(id='es_pie', figure=F.get_sfpie_figure(values))
            ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="es_sfAndTotalCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 400, 'margin-left': '10px'
                         }
        )])])
            
            return cards_container, html.Br(), figure_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container                
        
# English known types callback
     @app.callback(
            dash.dependencies.Output('en_known_types', 'figure'),
            [dash.dependencies.Input('en_ontology', 'clickData')]
            )
     def en_update_known_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.known_types_en
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
            figure.add_vline(x=float(R.en_stats[6]), line_width=4, line_color="#77C14C") # Mean
            figure.add_vline(x=float(R.en_stats[7]), line_width=4, line_color="#1FAFEE") # Median
            figure.add_vline(x=float(R.en_stats[9]), line_width=4, line_color="#D53614") # Standard deviation
            figure.add_traces([
                go.Scatter(x=[float(R.en_stats[6])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[R.en_stats[6]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[7])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[7]], hoverinfo="text"),
                go.Scatter(x=[float(R.en_stats[9])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[R.en_stats[9]], hoverinfo="text")
                ])
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
            return figure
        
 # English instance types callback
     @app.callback(
            dash.dependencies.Output('en_instance_types', 'figure'),
            [dash.dependencies.Input('en_ontologyy', 'clickData')]
            )
     def en_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.instance_types_en
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
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
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
            if selected_type in R.known_types_en["DBpedia type"].values:
                selected_row = R.known_types_en[R.known_types_en["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.en_stats[14]), line_width=4, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.en_stats[11]), line_width=4, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.en_stats[22]), line_width=4, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.en_stats[12]), line_width=4, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.en_stats[30]), line_width=4, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.en_stats[32]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[int(R.en_stats[14])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[R.en_stats[14]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[11])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[R.en_stats[11]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[22])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[R.en_stats[22]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[12])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[R.en_stats[12]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[30])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[R.en_stats[30]], hoverinfo="text"),
            go.Scatter(x=[int(R.en_stats[32])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[R.en_stats[32]], hoverinfo="text")
            ])
    
            fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
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
                dbpedia_entities = stats[63]
                mean = stats[64]
                median = 'dbr:Latvian_constitutional_referendum,_2008'
                std_dev = stats[67]
                top_file = R.top_2016_uriCounts_en
    
            if value == 'May 25th 2021':
                dbpedia_entities = stats[36]
                mean = stats[37]
                median = 'dbr:Kyrgyzstan_national_football_team'
                std_dev = stats[40]
                top_file = R.top_uriCounts_en
                
            mode = 'dbr:' + top_file['DBpedia entity'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº DBpedia entities"), html.H4(dbpedia_entities)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº occurrences per DBpedia entity (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                 dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate DBpedia entity (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("DBpedia entity that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="en_uriCounts_table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Count", "id": "Count"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 500, 'margin-left': '10px'
                         }
        )])])
    
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
                surface_forms = stats[69]
                mean = stats[70]
                median = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
                std_dev = stats[73]
                top_file = R.top_2016_pairCounts_en
    
            if value == 'May 25th 2021':
                surface_forms = stats[42]
                mean = stats[43]
                median = '[Wallenpaupack - dbr:Lake_Wallenpaupack]'
                std_dev = stats[46]
                top_file = R.top_pairCounts_en
                
            mode = "[" + top_file['Surface form'].iloc[0] + " - " + "dbr:"+ top_file['DBpedia entity'].iloc[0] + "]"
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº [Surface form - DBpedia entity] pairs"), html.H4(surface_forms)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate pair (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                 dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Pair that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="en_pairCounts_table",
            columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "DBpedia entity", "id": "DBpedia entity"},
                     {"name": "Times linked", "id": "Times linked"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 780, 'margin-left': '10px'
                         }
        )])])
            
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
                articles = stats[75]
                mean = stats[76]
                median = 'http://en.wikipedia.org/wiki/Kushti'
                std_dev = stats[78]
                top_file = R.top_2016_tokenCounts_en
    
            if value == 'May 25th 2021':
                articles = stats[48]
                mean = stats[49]
                median = 'http://en.wikipedia.org/wiki/Klas_Lund'
                std_dev = stats[51]
                top_file = R.top_tokenCounts_en
                
            mode = top_file['Wikipedia article'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº Wikipedia articles"), html.H4(articles)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº tokens per Wikipedia article (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate Wikipedia article (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Wikipedia article that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="en_tokenCounts_table",
           columns=[{"name": "Wikipedia article", "id": "Wikipedia article"},
                     {"name": "Nº tokens", "id": "Nº tokens"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 500, 'margin-left': '10px'
                         }
        )])])
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
                surface_forms = stats[80]
                mean = stats[85]
                median = 'Deep Cove'
                std_dev = stats[88]
                top_file = R.top_2016_sfAndTotalCounts_en
                values = [stats[81], stats[82], stats[83], stats[84]]
    
            if value == 'May 25th 2021':
                surface_forms = stats[53]
                mean = stats[58]
                median = 'DC Comics'
                std_dev = stats[61]
                top_file = R.top_sfAndTotalCounts_en
                values = [stats[54], stats[55], stats[56], stats[57]]
                
            mode = top_file['Surface form'].iloc[0]
            cards_container = html.Div(id='cards_container', children = [
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Nº surface forms"), html.H4(surface_forms)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of central tendency"),
                dbc.Card(dbc.CardBody(
                       html.Div([html.H4("Nº DBpedia entity links per surface form (mean)"), html.H4(mean)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Intermediate surface form (median)"), html.H4(median)])
                ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
                ),
                html.Br(),
                html.Br(),
                dbc.Card(dbc.CardBody(
                        html.Div([html.H4("Surface form that appears the most (mode)"), html.H4(mode)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                ),
                html.Br(),
                html.Br(),
                html.H4("Measures of dispersion"),
                dbc.Card(dbc.CardBody(
                         html.Div([html.H4("Standard deviation"), html.H4(std_dev)])
                ), color="#F5F5F5", style={'display': 'inline-block'}
                )
                ])
            
            figure_container = html.Div([
            html.H4("Surface forms"),
            dcc.Graph(id='es_pie', figure=F.get_sfpie_figure(values))
            ])
                
            table_container = html.Div(id='table_container', children = [
        html.Div([
        DataTable(
            id="en_sfAndTotalCounts_table",
           columns=[{"name": "Surface form", "id": "Surface form"},
                     {"name": "Times linked", "id": "Times linked"},
                     {"name": "Times as plain text", "id": "Times as plain text"}],
            data=top_file.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 625, 'margin-left': '10px'
                         }
        )])])
            
            return cards_container, html.Br(), figure_container, html.Br(), html.H4("Top 50 most linked surface forms"), html.Br(), table_container        
        