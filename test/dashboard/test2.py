import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc



def get_ontology_df():
   # Load dataframe
   df = pd.read_csv("ontologies.csv")
   return  df

def get_valid_types_df():
    # Load dataframe
    valid_types_df = pd.read_csv("valid_types.tsv", sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    return valid_types_df

def get_ontology_figure():
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), )
    return fig2


def get_init_bar_figure_pos(df):
    # For displaying positional measures
    first_row=df.iloc[0]
    fig = go.Figure(go.Bar(x = [first_row[2]], y = [first_row[0]], width=[0.05] , orientation='h', marker_color='#A349A4', name = "DBpedia type"))
    
    fig.add_vline(x=1, line_width=3, line_color="green")
    fig.add_vline(x=3, line_width=3, line_color="blue")
    
    fig.add_traces([
    go.Scatter(x=[0],y=[0],mode='lines', visible='legendonly', name='10th percentile', line=dict(color='green')),
    go.Scatter(x=[0],y=[0],mode='lines', visible='legendonly', name='1st quartile', line=dict(color='blue'))
    ])
    
    fig.update_layout(xaxis={'range': [0,65]}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=800)
    return fig



ontology_df = get_ontology_df()
valid_types = get_valid_types_df()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  #marker_color='#FFC300' marker_color='#C7FF33' marker_color='#33E6FF' marker_color='#FF33E6' marker_color='#A390A1' marker_color='#D2D715'  
app.layout = html.Div(
    [
        html.H4("Positional measures"),
        html.Div([
         dcc.Graph(id='ontology_pos', figure=get_ontology_figure(), style={'display': 'inline-block'}),
         dcc.Graph(id='es_valid_types_pos', figure=get_init_bar_figure_pos(get_valid_types_df()), 
                                 style={'display': 'inline-block'})
        ]) 
    ]
    )


# Spanish valid types position measures callback
@app.callback(
            dash.dependencies.Output('es_valid_types_pos', 'figure'),
            [dash.dependencies.Input('ontology_pos', 'clickData')]
            )
def es_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in valid_types["DBpedia type"].values:
                selected_row = valid_types[valid_types["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.05] , orientation='h', marker_color='#A349A4', name = "DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.05] , orientation='h', marker_color='#A349A4', name = "DBpedia type"))
            fig.add_vline(x=1, line_width=3, line_color="green")
            fig.add_vline(x=3, line_width=3, line_color="blue")
            fig.add_traces([
                go.Scatter(x=[0],y=[0],mode='lines', visible='legendonly', name='10th percentile', line=dict(color='green')),
                go.Scatter(x=[0],y=[0],mode='lines', visible='legendonly', name='1st quartile', line=dict(color='blue'))
                ])
    
            fig.update_layout(xaxis={'range': [0,65]}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=800)
            return fig


if __name__ == "__main__":
    app.run_server(debug=True)
   