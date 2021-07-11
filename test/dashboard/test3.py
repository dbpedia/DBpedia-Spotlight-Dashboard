import pandas as pd
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go


def get_uriCounts_figure(df):
    filtered_df = df[(df['Count'] >= 0) & (df['Count'] <= 100)].sample(n=20)	
    fig = go.Figure()
    fig.add_trace(go.Bar(x= filtered_df['Count'], y= filtered_df['DBpedia entity'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
    fig.add_vline(x=55.73, line_width=4, line_color="#77C14C") # Mean
    fig.add_vline(x=8, line_width=4, line_color="#1FAFEE") # Median
    fig.add_vline(x=999.80, line_width=4, line_color="#D53614") # Standard deviation
    fig.add_traces([
    go.Scatter(x=[100], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C")),
    go.Scatter(x=[100], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE")),
    go.Scatter(x=[100], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"))
    ])
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times appearing in Wikipedia dump", yaxis_title="DBpdedia entity")
    return fig

uriCounts_df = pd.read_csv("uriCounts", sep='\t',  names=["DBpedia entity", "Count"])
    

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Number of times each DBpedia entity is linked"),
        html.Br(),
        html.Div([
        dcc.RangeSlider(id='uriCounts_slider', min=0, max=1300, step=None, value=[0, 100],
        marks={
            0: '0',
            100: '100',
            200: '200',
            300: '300',
            400: '400',
		    500: '500',
		    600: '600',
		    700: '700',
		    800: '800',
		    900: '900',
		   1000:'1000',
           1100:'1100',
           1200:'1200',
           1300:'1300'
    }
    ),
        dcc.Graph(id="graph", style={'width': '1500px', 'height': '500px'},
                  figure= get_uriCounts_figure(uriCounts_df)), 
        ]
            )
        ])


# Callback for uriCounts
@app.callback(
    Output('graph', 'figure'),
    [Input('uriCounts_slider', 'value')])
def update_uriCounts_figure(value):
    filtered_df = uriCounts_df[(uriCounts_df['Count'] >= value[0]) & (uriCounts_df['Count'] <= value[1])].sample(n=20)	
    fig = go.Figure()
    fig.add_trace(go.Bar(x= filtered_df['Count'], y= filtered_df['DBpedia entity'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
    fig.add_vline(x=55.73, line_width=4, line_color="#77C14C") # Mean
    fig.add_vline(x=8, line_width=4, line_color="#1FAFEE") # Median
    fig.add_vline(x=999.80, line_width=4, line_color="#D53614") # Standard deviation
    fig.add_traces([
    go.Scatter(x=[100], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C")),
    go.Scatter(x=[100], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE")),
    go.Scatter(x=[100], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"))
    ])
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times appearing in Wikipedia dump", yaxis_title="DBpedia entity")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
    