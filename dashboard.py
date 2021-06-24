import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R
import figures as F

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='DBpedia Spotlight Dashboard'),
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Spanish', children = [html.Div(
           dcc.Graph(
           id='es_statistics',
           figure=F.es_statistics_figure
       )),html.Div(children=[html.H3("Valid types"),
           dcc.Graph(
           id='ontology',
           figure=F.ontology_figure, 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='es_valid_types',
           figure=F.es_valid_types_figure, 
           style={'display': 'inline-block'})  
       ])]),
        dcc.Tab(label='English', children=[html.Div(
           dcc.Graph(
           id='en_statistics',
          # figure=F.en_statistics_figure
    )),html.Div(children = [html.H3("Valid types"),
           dcc.Graph(
           id='ontology3',
           figure=F.ontology_figure, 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='en_valid_types',
           #figure=F.en_valid_types_figure, 
           style={'display': 'inline-block'})  
       ])]),
        # To be modified                    
        dcc.Tab(label='Comparison', value='comparison-tab', children = [html.Div(children=[
            html.H3('Choose metric to compare:'),
            dcc.Dropdown(id='dropdown',options=[
            {'label': 'Precision', 'value': 'Precision'},
            {'label': 'Impact', 'value': 'Impact'}
        ], value = 'Precision'),
             dcc.Graph(id='metric', figure={})
    ])])
])])
                            
def update_types_plot(df):
    # Updated types Bar 
    fig4 = go.Figure(go.Bar(x = df['Count'], y = df['DBpedia Type'], orientation='h', marker_color='#A349A4'))
    
    fig4.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, yaxis=dict(showgrid=False))
    return fig4                            

# Comparison callback -> To be modified
@app.callback(
    dash.dependencies.Output('metric', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_metrics(value):
    fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'indicator'}, 
                                                {'type' : 'indicator'}]])
    if value == 'Precision':
        fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(R.es_stats[0]),
    title = {'text': "Precision of Spanish valid URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)
        fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(R.en_stats[0]),
    title = {'text': "Precision of English valid URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=2
)
        
    elif value == 'Impact':
         fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(R.es_stats[1]),
    title = {'text': "Impact of Spanish invalid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)
         fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(R.en_stats[1]),
    title = {'text': "Impact of English invalid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=2
)
    return fig

# Spanish valid types callback
@app.callback(
        dash.dependencies.Output('es_valid_types', 'figure'),
        [dash.dependencies.Input('ontology', 'clickData')]
    )
def es_update_valid_types_bar(clicked_data):
        selected_type = 'owlThing'
        types_count_df = R.get_valid_types_df(R.es_dashboard_directory)
        ontology_df = R.get_ontology_df()
        if clicked_data is not None:
            if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                selected_type = clicked_data['points'][0]['parent']
            else:
                selected_type = clicked_data['points'][0]['label']
        selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
        if selected_ontology_df_labels.empty:
            selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            
        selected_all_instances_df = types_count_df[types_count_df['DBpedia Type'].isin(selected_ontology_df_labels)]
        selected_all_instances_df = selected_all_instances_df.sort_values(by='Count', ascending=False)
        if selected_all_instances_df.empty:
            selected_all_instances_df.append({'DBpedia Type': selected_type, 'Count': 0}, ignore_index=True)
        figure = update_types_plot(selected_all_instances_df)
        return figure

# English valid types callback
@app.callback(
        dash.dependencies.Output('en_valid_types', 'figure'),
        [dash.dependencies.Input('ontology3', 'clickData')]
    )
def en_update_valid_types_bar(clicked_data):
        selected_type = 'owlThing'
        ontology_df = R.get_ontology_df()
        types_count_df = R.get_valid_types_df(R.en_dashboard_directory)
        if clicked_data is not None:
            if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                selected_type = clicked_data['points'][0]['parent']
            else:
                selected_type = clicked_data['points'][0]['label']
        selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
        if selected_ontology_df_labels.empty:
            selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            
        selected_all_instances_df = types_count_df[types_count_df['DBpedia Type'].isin(selected_ontology_df_labels)]
        selected_all_instances_df = selected_all_instances_df.sort_values(by='Count', ascending=False)
        if selected_all_instances_df.empty:
            selected_all_instances_df.append({'DBpedia Type': selected_type, 'Count': 0}, ignore_index=True)
        figure = update_types_plot(selected_all_instances_df)
        return figure

if __name__ == '__main__':
    app.run_server(debug=True)
    