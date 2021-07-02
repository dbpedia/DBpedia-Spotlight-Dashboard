import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R
     

def get_language_statistics_figure(language_directory):
    if(language_directory == R.es_dashboard_directory):
        stats = R.es_stats
    else:
        stats = R.en_stats
        
    # Indicators for precision and impact
    fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'indicator'}, 
                                                  {'type' : 'indicator'}]])
    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(stats[0]),
    title = {'text': "Precision of DBpedia types URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)

    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(stats[1]),
    title = {'text': "Impact of unknown types URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
),
 
   row=1, col=2
)
    return fig
def get_ontology_figure():
    ontology_df = R.ontology_df
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=800)
    
    return fig2


def get_valid_types_figure(language_directory):
    if(language_directory == R.es_dashboard_directory):
        valid_types_df = R.valid_types_es
    else:
        valid_types_df = R.valid_types_en
    # Valid types Bar 
    fig3 = go.Figure(go.Bar(x = valid_types_df['Count'], y = valid_types_df['DBpedia Type'], orientation='h', marker_color='#A349A4'))
    fig3.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=800, yaxis=dict(showgrid=False))
    return fig3

es_statistics_figure = get_language_statistics_figure(R.es_dashboard_directory)
en_statistics_figure = get_language_statistics_figure(R.en_dashboard_directory)
ontology_figure = get_ontology_figure()
es_valid_types_figure = get_valid_types_figure(R.es_dashboard_directory)
en_valid_types_figure = get_valid_types_figure(R.en_dashboard_directory)
     