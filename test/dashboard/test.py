import pandas as pd
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_table import DataTable
import plotly.graph_objects as go


def get_init_bar(df):
    first_row=df.iloc[0]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[first_row[0]], y=[1400], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia entity",
            text=str(first_row[1]), textposition='outside',
                         ))
    fig.add_trace(go.Bar(x=["Mean"], y=[55], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text='55', textposition='outside'
                         ))
    fig.add_trace(go.Bar(x=["Median"], y=[8], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text='8', textposition='outside'))
    fig.add_trace(go.Bar(x=["Standard deviation"], y=[998], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text='998', textposition='outside'))
    fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
    return fig

uriCounts_df = pd.read_csv("uriCounts_top50", sep='\t',  names=["DBpedia entity", "Count"])
    

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H5("Top 50 entities most times linked"),
        html.Br(),
        html.Div([
        html.Div([
        DataTable(
            id="table",
            columns=[{"name": "DBpedia entity", "id": "DBpedia entity"}],
            data=uriCounts_df.to_dict("records"),
            fill_width=False,
            style_table={
                'overflowY': 'scroll', 'height': 400, 'width': 325
                         }
        )], style={'flex-grow': '0.15'}
            ),
        dcc.Graph(id="graph", style={'width': '800px', 'height': '400px'},
                  figure= get_init_bar(uriCounts_df))], style={'display': 'flex'})
        
        ])


# Callback for uriCounts

@app.callback(
    Output("graph", "figure"), 
    Input("table", "active_cell"), 
    prevent_initial_call=True
)
def update_output_div(active_cell):
    selected_row = active_cell["row"]
    label = uriCounts_df["DBpedia entity"].iloc[selected_row]
    value = uriCounts_df["Count"].iloc[selected_row]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[label], y=[1400], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia entity",
                         text=str(value), textposition='outside'))
    fig.add_trace(go.Bar(x=["Mean"], y=[55], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text='55', textposition='outside'))
    fig.add_trace(go.Bar(x=["Median"], y=[8], width=[0.5], marker_color='#C7FF33', name = "Median",
                         text='8', textposition='outside'))
    fig.add_trace(go.Bar(x=["Standard deviation"], y=[998], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                         text='998', textposition='outside'))
    fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)