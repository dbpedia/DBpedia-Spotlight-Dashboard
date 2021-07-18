import dash
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

versions_stats = get_version_statistics()

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
                
            if value1 == 'Oct 1st 2020':
                entities_version1 = versions_stats[6]
                
            if value1 == 'May 1st 2021':
                entities_version1 = versions_stats[10]
                
            if value1 == 'June 1st 2021':
                entities_version1 = versions_stats[14]
                
            if value2 == 'Oct 1st 2016':
                entities_version2 = versions_stats[2]
            if value2 == 'Oct 1st 2020':
                entities_version2 = versions_stats[6]
                
            if value2 == 'May 1st 2021':
                entities_version2 = versions_stats[10]
                
            if value2 == 'June 1st 2021':
                entities_version2 = versions_stats[14]
        
        if lang_value == 'English':
            if value1 == 'Oct 1st 2016':
                entities_version1 = versions_stats[18]
            if value1 == 'Oct 1st 2020':
                entities_version1 = versions_stats[22]
                
            if value1 == 'May 1st 2021':
                entities_version1 = versions_stats[26]
                
            if value1 == 'June 1st 2021':
                entities_version1 = versions_stats[30]
                
            if value2 == 'Oct 1st 2016':
                entities_version2 = versions_stats[18]
            if value2 == 'Oct 1st 2020':
                entities_version2 = versions_stats[22]
                
            if value2 == 'May 1st 2021':
                entities_version2 = versions_stats[26]
                
            if value2 == 'June 1st 2021':
                entities_version2 = versions_stats[30]
        
        bar_figure = get_version_bar_figure([value1, value2], [entities_version1, entities_version2])
        pie_figure = get_version_pie_figure([value1, value2], [entities_version1, entities_version2])
        bar_graph = dcc.Graph(id='versions_bar', figure=bar_figure, style={'display': 'inline-block'})
        pie_graph = dcc.Graph(id='versions_pie', figure=pie_figure, style={'display': 'inline-block'})
        title = html.H3(value1 + " VS " + value2)
        return title, html.Br(), bar_graph, pie_graph
    
if __name__ == "__main__":
    app.run_server(debug=False)
