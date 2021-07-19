# -*- coding: utf-8 -*-
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R
     

def get_language_statistics_figure(stats):
   
    # Indicators for precision and impact
    fig = make_subplots(rows=1, cols=2, specs=[[{'type' : 'indicator'}, 
                                                  {'type' : 'indicator'}]])
    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(stats[33]),
    title = {'text': "Precision of DBpedia types URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}}
),
    row=1, col=1
)

    fig.add_trace(
    go.Indicator(
    mode = "gauge+number",
    value = float(stats[34]),
    title = {'text': "Impact of unknown types URLs"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
),
 
   row=1, col=2
)
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=1400)
    return fig

def get_ontology_figure():
    ontology_df = R.ontology_df
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700)
    return fig2


def get_instance_types_figure(instance_types_df):
    # Instance types Bar 
    fig3 = go.Figure(go.Bar(x = instance_types_df['Nº entities'], y = instance_types_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
    fig3.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig3


def get_known_types_figure(language_directory, known_types_df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
        
    # Valid types Bar 
    fig4 = go.Figure(go.Bar(x = known_types_df['Nº entities'], y = known_types_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
    fig4.add_vline(x=float(stats[6]), line_width=4, line_color="#77C14C") # Mean
    fig4.add_vline(x=float(stats[7]), line_width=4, line_color="#1FAFEE") # Median
    fig4.add_vline(x=float(stats[9]), line_width=4, line_color="#D53614") # Standard deviation
    fig4.add_traces([
    go.Scatter(x=[float(stats[6])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[6]], hoverinfo="text"),
    go.Scatter(x=[float(stats[7])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[stats[7]], hoverinfo="text"),
    go.Scatter(x=[float(stats[9])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[9]], hoverinfo="text")
    ])
    fig4.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig4

def get_sfpie_figure(language_directory):
    # sfAndTotalCounts pie chart
    labels = ['Without associated link','Not appearing as text','Not appearing as text without associated link','Rest']
    if(language_directory == R.es_dashboard_directory):
        values = [R.es_stats[48], R.es_stats[49], R.es_stats[50], R.es_stats[51]]
    else:
        values = [R.en_stats[48], R.en_stats[49], R.en_stats[50], R.en_stats[51]]
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig5.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=300, width=700)
    return fig5

def get_uriCounts_figure(language_directory, df):
     if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
     else:
        stats = R.en_stats
     filtered_df = df[(df['Count'] >= 0) & (df['Count'] <= 100)].sample(n=20)	
     fig6 = go.Figure()
     fig6.add_trace(go.Bar(x= filtered_df['Count'], y= filtered_df['DBpedia entity'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
     fig6.add_vline(x=float(stats[35]), line_width=4, line_color="#77C14C") # Mean
     fig6.add_vline(x=float(stats[36]), line_width=4, line_color="#1FAFEE") # Median
     fig6.add_vline(x=float(stats[38]), line_width=4, line_color="#D53614") # Standard deviation
     fig6.add_traces([
     go.Scatter(x=[float(stats[35])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[35]], hoverinfo="text"),
    go.Scatter(x=[float(stats[36])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[stats[36]], hoverinfo="text"),
    go.Scatter(x=[float(stats[38])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[38]], hoverinfo="text")
     ])
     fig6.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times appearing in Wikipedia dump", yaxis_title="DBpedia entity")
     return fig6

def get_pairCounts_figure(language_directory, df):
     if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
     else:
        stats = R.en_stats
     filtered_df = df[(df['Times linked'] >= 0) & (df['Times linked'] <= 100)].sample(n=20)	
     fig7 = go.Figure()
     fig7.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
     fig7.add_vline(x=float(stats[39]), line_width=4, line_color="#77C14C") # Mean
     fig7.add_vline(x=float(stats[40]), line_width=4, line_color="#1FAFEE") # Median
     fig7.add_vline(x=float(stats[42]), line_width=4, line_color="#D53614") # Standard deviation
     fig7.add_traces([
      go.Scatter(x=[float(stats[39])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[39]], hoverinfo="text"),
    go.Scatter(x=[float(stats[40])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[stats[40]], hoverinfo="text"),
    go.Scatter(x=[float(stats[42])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[42]], hoverinfo="text")
     ])
     fig7.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
     return fig7

def get_sfAndTotalCounts_figure(language_directory, df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
    filtered_df = df[(df['Times linked'] >= 0) & (df['Times linked'] <= 100)].sample(n=20)	
    fig8 = go.Figure()
    fig8.add_trace(go.Bar(x= filtered_df['Times linked'], y= filtered_df['Surface form'], orientation='h', marker_color='#A349A4', name = "Surface form"))
    fig8.add_vline(x=float(stats[52]), line_width=4, line_color="#77C14C") # Mean
    fig8.add_vline(x=float(stats[53]), line_width=4, line_color="#1FAFEE") # Median
    fig8.add_vline(x=float(stats[55]), line_width=4, line_color="#D53614") # Standard deviation
    fig8.add_traces([
     go.Scatter(x=[float(stats[52])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[52]], hoverinfo="text"),
    go.Scatter(x=[float(stats[53])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[stats[53]], hoverinfo="text"),
    go.Scatter(x=[float(stats[55])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[55]], hoverinfo="text")
     ])
    fig8.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Times linked to a DBpedia entity", yaxis_title="Surface form")
    return fig8

def get_tokenCounts_figure(language_directory, df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
    filtered_df = df[(df['Nº tokens'] >= 0) & (df['Nº tokens'] <= 100)].sample(n=20)	
    fig8 = go.Figure()
    fig8.add_trace(go.Bar(x= filtered_df['Nº tokens'], y= filtered_df['Wikipedia article'], orientation='h', marker_color='#A349A4', name = "Wikipedia article"))
    fig8.add_vline(x=float(stats[44]), line_width=4, line_color="#77C14C") # Mean
    fig8.add_vline(x=float(stats[45]), line_width=4, line_color="#1FAFEE") # Median
    fig8.add_vline(x=float(stats[46]), line_width=4, line_color="#D53614") # Standard deviation
    fig8.add_traces([
      go.Scatter(x=[float(stats[44])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[44]], hoverinfo="text"),
    go.Scatter(x=[float(stats[45])], y= [" "], mode='lines', name='Median', line=dict(color="#1FAFEE"), hovertext=[stats[45]], hoverinfo="text"),
    go.Scatter(x=[float(stats[46])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[46]], hoverinfo="text")
     ])
    fig8.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of tokens", yaxis_title="Wikipedia article")
    return fig8

def get_init_bar_figure_pos(language_directory,df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
    
    # For displaying positional measures
    first_row=df.iloc[0]
    fig = go.Figure(go.Bar(x = [first_row[2]], y = [first_row[0]], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
    
    fig.add_vline(x=int(stats[14]), line_width=4, line_color="#77C14C") # 10th percentile
    fig.add_vline(x=int(stats[11]), line_width=4, line_color="#1FAFEE") # 1st quartile
    fig.add_vline(x=int(stats[22]), line_width=4, line_color="#D53614") # 50th percentile
    fig.add_vline(x=int(stats[12]), line_width=4, line_color="#D59D14") # 3rd quartile
    fig.add_vline(x=int(stats[30]), line_width=4, line_color="#FFA4F5") # 90th percentile
    fig.add_vline(x=int(stats[32]), line_width=4, line_color="#FFFB0B") # 95th percentile
    
    fig.add_traces([
    go.Scatter(x=[int(stats[14])], y= [" "], mode='lines', name='10th percentile', line=dict(color="#77C14C"), hovertext=[stats[14]], hoverinfo="text"),
    go.Scatter(x=[int(stats[11])], y= [" "], mode='lines', name='1st quartile', line=dict(color="#1FAFEE"), hovertext=[stats[11]], hoverinfo="text"),
    go.Scatter(x=[int(stats[22])], y= [" "], mode='lines', name='50th percentile', line=dict(color="#D53614"), hovertext=[stats[22]], hoverinfo="text"),
    go.Scatter(x=[int(stats[12])], y= [" "], mode='lines', name='3rd quartile', line=dict(color="#D59D14"), hovertext=[stats[12]], hoverinfo="text"),
    go.Scatter(x=[int(stats[30])], y= [" "], mode='lines', name='90th percentile', line=dict(color="#FFA4F5"), hovertext=[stats[30]], hoverinfo="text"),
    go.Scatter(x=[int(stats[32])], y= [" "], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"), hovertext=[stats[32]], hoverinfo="text")
    ])
    
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700, xaxis_title="Number of DBpedia types", yaxis_title="DBpedia type")
    return fig

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

def get_versions_instance_types_figure(labels, version1_df, version2_df):
    fig = go.Figure()
    # Instance types Bar
    fig.add_trace(go.Bar(x = version1_df['Nº entities'], y = version1_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = labels[0]))
    fig.add_trace(go.Bar(x = version2_df['Nº entities'], y = version2_df['DBpedia type'], orientation='h', marker_color="#77C14C", name = labels[1]))
    
    fig.update_layout(barmode='group', margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig

es_statistics_figure = get_language_statistics_figure(R.es_stats)
en_statistics_figure = get_language_statistics_figure(R.en_stats)
ontology_figure = get_ontology_figure()
es_instance_types_figure = get_instance_types_figure(R.instance_types_es)
en_instance_types_figure = get_instance_types_figure(R.instance_types_en)
es_known_types_figure = get_known_types_figure(R.es_dashboard_directory, R.known_types_es)
en_known_types_figure = get_known_types_figure(R.en_dashboard_directory, R.known_types_en)
es_sfpie_figure = get_sfpie_figure(R.es_dashboard_directory)
en_sfpie_figure = get_sfpie_figure(R.en_dashboard_directory)
es_uriCounts_figure = get_uriCounts_figure(R.es_dashboard_directory, R.uriCounts_es)
es_pairCounts_figure = get_pairCounts_figure(R.es_dashboard_directory, R.pairCounts_es)
es_sfAndTotalCounts_figure = get_sfAndTotalCounts_figure(R.es_dashboard_directory, R.sfAndTotalCounts_es)
en_uriCounts_figure = get_uriCounts_figure(R.en_dashboard_directory, R.uriCounts_en)
en_pairCounts_figure = get_pairCounts_figure(R.en_dashboard_directory, R.pairCounts_en)
en_sfAndTotalCounts_figure = get_sfAndTotalCounts_figure(R.en_dashboard_directory, R.sfAndTotalCounts_en)
es_pos_known_types_figure =  get_init_bar_figure_pos(R.es_dashboard_directory, R.known_types_es)
en_pos_known_types_figure =  get_init_bar_figure_pos(R.en_dashboard_directory, R.known_types_en)
