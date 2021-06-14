import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R

def get_precision(language_directory):
    # Statistics -> Se cogen de validate.py teniendo en cuenta language_directory
    # For testing 
    if language_directory == "":
        precision = 0.9
    else:
        precision = 0.7
        
    return precision

def get_impact(language_directory):
    # Statistics -> Se cogen de validate.py teniendo en cuenta language_directory
    # For testing 
    if language_directory == "":
        impact = 0.4
    else:
        impact = 0.2
        
    return impact

def get_language_statistics_figure(language_directory):
    
    precision = get_precision(language_directory)
    impact = get_impact(language_directory)
    
    # Indicators for precision and impact
    fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'indicator'}, 
                                                  {'type' : 'indicator'}]])

    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = precision,
    title = {'text': "Precision of valid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)

    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = impact,
    title = {'text': "Impact of invalid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=2
)
    return fig
    

def get_ontology_df():
   # Load dataframe
   df = pd.read_csv("ontologies.csv")
   return  df

def get_valid_types_df(language_directory):
    # Load dataframe
    valid_types_df = R.tsv_to_df(language_directory + "valid_types.tsv")
    return valid_types_df

def get_invalid_types_df(language_directory):
    # Load dataframe
    invalid_types_df = R.tsv_to_df(language_directory + "invalid_types.tsv")
    return invalid_types_df

def get_ontology_figure():
    ontology_df = get_ontology_df()
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400)
    
    return fig2


def get_valid_types_figure(language_directory):
    valid_types_df = get_valid_types_df(language_directory)
    # Valid types Bar 
    fig3 = go.Figure(go.Bar(x = valid_types_df['Count'], y = valid_types_df['DBpedia Type'], orientation='h', marker_color='#A349A4'))
    
    fig3.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, yaxis=dict(showgrid=False))
    return fig3

def get_invalid_types_figure(language_directory):
    invalid_types_df = get_invalid_types_df(language_directory)
    # Invalid types Bar 
    fig4 = go.Figure(go.Bar(x = invalid_types_df['Count'], y = invalid_types_df['DBpedia Type'], orientation='h', marker_color='#A349A4'))
    
    fig4.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, yaxis=dict(showgrid=False))
    return fig4


def update_types_plot(df):
    # Updated types Bar 
    fig5 = go.Figure(go.Bar(x = df['Count'], y = df['DBpedia Type'], orientation='h', marker_color='#A349A4'))
    
    fig5.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, yaxis=dict(showgrid=False))
    return fig5


    

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='DBpedia Spotlight Dashboard'),
    html.Br(),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Spanish', children = [html.Div(
           dcc.Graph(
           id='es_statistics',
           figure=get_language_statistics_figure(""))
       ),html.Div(children=[html.H3("Valid types"),
           dcc.Graph(
           id='ontology',
           figure=get_ontology_figure(), 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='es_valid_types',
           figure=get_valid_types_figure(""), 
           style={'display': 'inline-block'})  
       ]),html.Div(children=[html.H3("Invalid types"),
           dcc.Graph(
           id='ontology2',
           figure=get_ontology_figure(), 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='es_invalid_types',
           figure=get_invalid_types_figure(""), 
           style={'display': 'inline-block'}) 
    ])]),
        dcc.Tab(label='English', children=[html.Div(
           dcc.Graph(
           id='en_statistics',
           figure=get_language_statistics_figure("dcdccdd")
    )),html.Div(children = [html.H3("Valid types"),
           dcc.Graph(
           id='ontology3',
           figure=get_ontology_figure(), 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='en_valid_types',
           figure=get_valid_types_figure(""), 
           style={'display': 'inline-block'})  
       ]),html.Div(children = [html.H3("Invalid types"),
           dcc.Graph(
           id='ontology4',
           figure=get_ontology_figure(), 
           style={'display': 'inline-block'}),
           dcc.Graph(
           id='en_invalid_types',
           figure=get_invalid_types_figure(""), 
           style={'display': 'inline-block'}) 
     ])]),
        dcc.Tab(label='Comparison', value='comparison-tab', children = [html.Div(children=[
            html.H3('Choose metric to compare:'),
            dcc.Dropdown(id='dropdown',options=[
            {'label': 'Precision', 'value': 'Precision'},
            {'label': 'Impact', 'value': 'Impact'}
        ], value = 'Precision'),
             dcc.Graph(id='metric', figure={})
    ])])
])])

# Comparison callback
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
    value = get_precision(""),
    title = {'text': "Precision of Spanish valid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)
        fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = get_precision("efeffefee"),
    title = {'text': "Precision of English valid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=2
)
        
    elif value == 'Impact':
         fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = get_impact(""),
    title = {'text': "Impact of Spanish invalid types"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)
         fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = get_impact("efeffefee"),
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
        ontology_df = get_ontology_df()
        types_count_df = get_valid_types_df("")
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
    
# Spanish invalid types callback
@app.callback(
        dash.dependencies.Output('es_invalid_types', 'figure'),
        [dash.dependencies.Input('ontology2', 'clickData')]
    )
def es_update_invalid_types_bar(clicked_data):
        selected_type = 'owlThing'
        ontology_df = get_ontology_df()
        types_count_df = get_valid_types_df("")
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
        ontology_df = get_ontology_df()
        types_count_df = get_valid_types_df("")
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

# English invalid types callback
@app.callback(
        dash.dependencies.Output('en_invalid_types', 'figure'),
        [dash.dependencies.Input('ontology4', 'clickData')]
    )
def en_update_invalid_types_bar(clicked_data):
        selected_type = 'owlThing'
        ontology_df = get_ontology_df()
        types_count_df = get_valid_types_df("")
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