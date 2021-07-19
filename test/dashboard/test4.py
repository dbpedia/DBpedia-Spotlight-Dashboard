import dash
import pandas as pd
import re
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go



def get_version_statistics():
    file = open("versions_statistics.txt", 'r')
    file = file.read()
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    return numbers

# TSV to dataframe
def tsv_to_df(path):
    if "uriCounts" in path: 
        df = pd.read_csv(path, sep='\t',  names=["DBpedia entity", "Count"])
    elif "known_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "known_types_top50" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "instance_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities"])
    elif "pairCounts" in path:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "DBpedia entity", "Times linked"])
    elif "token" in path:
        df = pd.read_csv(path, sep=' ',  names=["Wikipedia article", " ", "Nº tokens"])
    elif "ontologies" in path:
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "Times linked", "Times as plain text"])
    return df

def get_version_bar_figure(labels, values):
    fig = go.Figure()
    fig.add_trace(go.Bar(x= [int(values[0])], orientation='h', marker_color='#A349A4', name = labels[0], width = 1, hovertext=[values[0]], hoverinfo="text"))
    fig.add_trace(go.Bar(x= [int(values[1])], orientation='h', marker_color="#77C14C", name = labels[1], width = 0.5, hovertext=[values[1]], hoverinfo="text"))
    
    fig.update_layout(yaxis={'ticks':'', 'showticklabels':False}, barmode='overlay', margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia version")
    return fig
    
def get_version_pie_figure(labels,values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=300, width=700)
    return fig

def get_ontology_figure():
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700)
    return fig2

def get_versions_instance_types_figure(labels, version1_df, version2_df):
    fig = go.Figure()
    # Instance types Bar
    fig.add_trace(go.Bar(x = version1_df['Nº entities'], y = version1_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = labels[0]))
    fig.add_trace(go.Bar(x = version2_df['Nº entities'], y = version2_df['DBpedia type'], orientation='h', marker_color="#77C14C", name = labels[1]))
    
    fig.update_layout(barmode='group', margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig

versions_stats = get_version_statistics()
instance_types_es_2016_10_01 = tsv_to_df("instance_types_es_2016.10.01")
instance_types_es_2020_10_01 = tsv_to_df("instance_types_es_2020.10.01")
instance_types_es_2021_05_01 = tsv_to_df("instance_types_es_2021.05.01")
instance_types_es_2021_06_01 = tsv_to_df("instance_types_es_2021.06.01")
instance_types_en_2016_10_01 = tsv_to_df("instance_types_en_2016.10.01")
instance_types_en_2020_10_01 = tsv_to_df("instance_types_en_2020.10.01")
instance_types_en_2021_05_01 = tsv_to_df("instance_types_en_2021.05.01")
instance_types_en_2021_06_01 = tsv_to_df("instance_types_en_2021.06.01")
ontology_df = tsv_to_df("ontologies.csv")

app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(
    [
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
        ])
    
# Comparison callback - cards
@app.callback(
    Output('data_container', 'children'),
    [Input('version1_dropdown', 'value'),
     Input('version2_dropdown', 'value'),
     Input('lang_dropdown', 'value')])
def version_data(value1, value2, lang_value):
    if(lang_value is None or value1 is None or value2 is None):
        return dash.no_update
    else:
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
                    html.H4("Nº DBpedia entities: " + entities_version1)
            ), color="#F5F5F5", style={'display': 'inline-block'}
            ),
            dbc.Card(dbc.CardBody(
                    html.H4("Nº DBpedia types: " + types_version1)
            ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
            )
            ])
            
        version2_container = html.Div(id='type_container', children = [
            html.H4(value2),
            dbc.Card(dbc.CardBody(
                    html.H4("Nº DBpedia entities: " + entities_version2)
            ), color="#F5F5F5", style={'display': 'inline-block'}
            ),
            dbc.Card(dbc.CardBody(
                    html.H4("Nº DBpedia types: " + types_version2)
            ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
            )
            ])
        
        growth_container = html.Div(id='growth_container', children = [
        html.H4("Growth between versions"),
        dbc.Card(dbc.CardBody(
                    html.H4("Entity growth: " + str(entity_growth))
            ), color="#F5F5F5", style={'display': 'inline-block'}
            ),
        dbc.Card(dbc.CardBody(
            html.H4("Type growth: " + str(type_growth))
            ), color="#F5F5F5", style={'display': 'inline-block', "margin-left": "25px"}
            )
            ])
        title = html.H3("Version comparison")
        
        return title, html.Br(), version1_container, html.Br(), version2_container, html.Br(), growth_container
    
    
    
# Comparison callback - figures
@app.callback(
    Output('figures_container', 'children'),
    [Input('version1_dropdown', 'value'),
     Input('version2_dropdown', 'value'),
     Input('lang_dropdown', 'value')])
def version_figures(value1, value2, lang_value):
    if(lang_value is None or value1 is None or value2 is None):
        return dash.no_update
    else:
        if lang_value == 'Spanish':
            if value1 == 'Oct 1st 2016':
                entities_version1 = versions_stats[2]
                df1 = instance_types_es_2016_10_01
                
            if value1 == 'Oct 1st 2020':
                entities_version1 = versions_stats[6]
                df1 = instance_types_es_2020_10_01
                
            if value1 == 'May 1st 2021':
                entities_version1 = versions_stats[10]
                df1 = instance_types_es_2021_05_01
                
            if value1 == 'June 1st 2021':
                entities_version1 = versions_stats[14]
                df1 = instance_types_es_2021_06_01
                
            if value2 == 'Oct 1st 2016':
                entities_version2 = versions_stats[2]
                df2 = instance_types_es_2016_10_01
                
            if value2 == 'Oct 1st 2020':
                entities_version2 = versions_stats[6]
                df2 = instance_types_es_2020_10_01
                
            if value2 == 'May 1st 2021':
                entities_version2 = versions_stats[10]
                df2 = instance_types_es_2021_05_01
                
            if value2 == 'June 1st 2021':
                entities_version2 = versions_stats[14]
                df2 = instance_types_es_2021_06_01
        
        if lang_value == 'English':
            if value1 == 'Oct 1st 2016':
                entities_version1 = versions_stats[18]
                df1 = instance_types_en_2016_10_01
            if value1 == 'Oct 1st 2020':
                entities_version1 = versions_stats[22]
                df1 = instance_types_en_2020_10_01
                
            if value1 == 'May 1st 2021':
                entities_version1 = versions_stats[26]
                df1 = instance_types_en_2021_05_01
                
            if value1 == 'June 1st 2021':
                entities_version1 = versions_stats[30]
                df1 = instance_types_en_2021_06_01
                
            if value2 == 'Oct 1st 2016':
                entities_version2 = versions_stats[18]
                df2 = instance_types_en_2016_10_01
                
            if value2 == 'Oct 1st 2020':
                entities_version2 = versions_stats[22]
                df2 = instance_types_en_2020_10_01
                
            if value2 == 'May 1st 2021':
                entities_version2 = versions_stats[26]
                df2 = instance_types_en_2021_05_01
                
            if value2 == 'June 1st 2021':
                entities_version2 = versions_stats[30]
                df2 = instance_types_en_2021_06_01
        
        bar_figure = get_version_bar_figure([value1, value2], [entities_version1, entities_version2])
        pie_figure = get_version_pie_figure([value1, value2], [entities_version1, entities_version2])
        bar_graph = dcc.Graph(id='versions_bar', figure=bar_figure, style={'display': 'inline-block'})
        pie_graph = dcc.Graph(id='versions_pie', figure=pie_figure, style={'display': 'inline-block'})
        title = html.H3(value1 + " VS " + value2)
        type_title = html.H3("DBpedia types comparison")
        types_container = html.Div([
            dcc.Graph(id='ontology_version', figure=get_ontology_figure(), style={'display': 'inline-block'}),
            dcc.Graph(id='instance_types_version', figure=get_versions_instance_types_figure([value1, value2], df1, df2), 
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
                        df1 = instance_types_es_2016_10_01
                        
                    if value1 == 'Oct 1st 2020':
                        df1 = instance_types_es_2020_10_01
                        
                    if value1 == 'May 1st 2021':
                        df1 = instance_types_es_2021_05_01
                        
                    if value1 == 'June 1st 2021':
                        df1 = instance_types_es_2021_06_01
                        
                    if value2 == 'Oct 1st 2016':
                        df2 = instance_types_es_2016_10_01
                        
                    if value2 == 'Oct 1st 2020':
                        df2 = instance_types_es_2020_10_01
                        
                    if value2 == 'May 1st 2021':
                        df2 = instance_types_es_2021_05_01
                        
                    if value2 == 'June 1st 2021':
                        df2 = instance_types_es_2021_06_01
                
                if lang_value == 'English':
                    if value1 == 'Oct 1st 2016':
                        df1 = instance_types_en_2016_10_01
                    if value1 == 'Oct 1st 2020':
                        df1 = instance_types_en_2020_10_01
                        
                    if value1 == 'May 1st 2021':
                        df1 = instance_types_en_2021_05_01
                        
                    if value1 == 'June 1st 2021':
                        df1 = instance_types_en_2021_06_01
                        
                    if value2 == 'Oct 1st 2016':
                        df2 = instance_types_en_2016_10_01
                        
                    if value2 == 'Oct 1st 2020':
                        df2 = instance_types_en_2020_10_01
                        
                    if value2 == 'May 1st 2021':
                        df2 = instance_types_en_2021_05_01
                        
                    if value2 == 'June 1st 2021':
                        df2 = instance_types_en_2021_06_01
                        
            ontology_df = tsv_to_df("ontologies.csv")
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
    
if __name__ == "__main__":
    app.run_server(debug=False)
