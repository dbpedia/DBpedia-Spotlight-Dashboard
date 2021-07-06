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
    fig3.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
    return fig3


def get_valid_types_figure(valid_types_df):
    # Valid types Bar 
    fig4 = go.Figure(go.Bar(x = valid_types_df['Nº entities'], y = valid_types_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
    fig4.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
    return fig4

def get_sfpie_figure(language_directory):
    # sfAndTotalCounts pie chart
    labels = ['Without associated link','Not appearing as text','Not appearing as text without associated link','Rest']
    if(language_directory == R.es_dashboard_directory):
        values = [R.es_stats[46], R.es_stats[47], R.es_stats[48], R.es_stats[49]]
    else:
        values = [R.en_stats[46], R.en_stats[47], R.en_stats[48], R.en_stats[49]]
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig5.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=300, width=700)
    return fig5

def get_init_bar_figure(language_directory, df):
    # For displaying dispersion measures
    first_row=df.iloc[0]
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
        
    measures = [float(stats[35]), float(stats[36]), float(stats[38]), float(stats[39]), float(stats[40]), float(stats[42]), float(stats[50]), float(stats[51]), float(stats[53]), float(stats[6]), float(stats[7]), float(stats[9])]
    y = [1400]
    yaxis_range=[0,1500]
    text = first_row[1]
    
    if(df.equals(R.uriCounts_es) or df.equals(R.uriCounts_en)):
        mean = measures[0]
        median = measures[1]
        std_dv = measures[2]
        name = "Selected DBpedia entity"
    elif(df.equals(R.pairCounts_es) or df.equals(R.pairCounts_en)):
        mean = measures[3]
        median = measures[4]
        std_dv =  measures[5]
        name = "Selected surface form"
        text = first_row[2]
    elif(df.equals(R.sfAndTotalCounts_es) or df.equals(R.sfAndTotalCounts_en)):
        mean = measures[6]
        median = measures[7]
        std_dv = measures[8]
        name = "Selected surface form"
    else:
        mean = measures[9]
        median = measures[10]
        std_dv = measures[11]
        name = "Selected DBpedia type"
        y = [first_row[1]]
        if language_directory == R.es_dashboard_directory:
            yaxis_range=[0,315000]
        else:
            yaxis_range=[0,1360000]
    
    fig6 = go.Figure() 
    fig6.add_trace(go.Bar(x=[first_row[0]], y=y, width=[0.5], marker_color='#A349A4', name = name,
            text=str(text), textposition='outside',
                         ))
        
    fig6.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
    fig6.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
    fig6.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
    fig6.update_layout(yaxis={'visible': False}, yaxis_range=yaxis_range, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
    return fig6

def get_init_bar_figure_pos(language_directory,df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
        limit = 65
    else:
        stats = R.en_stats
        limit = 130
    
    # For displaying positional measures
    first_row=df.iloc[0]
    fig = go.Figure(go.Bar(x = [first_row[2]], y = [first_row[0]], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
    
    fig.add_vline(x=int(stats[14]), line_width=3, line_color="#77C14C") # 10th percentile
    fig.add_vline(x=int(stats[11]), line_width=3, line_color="#1FAFEE") # 1st quartile
    fig.add_vline(x=int(stats[22]), line_width=3, line_color="#D53614") # 50th percentile
    fig.add_vline(x=int(stats[12]), line_width=3, line_color="#D59D14") # 3rd quartile
    fig.add_vline(x=int(stats[30]), line_width=3, line_color="#FFA4F5") # 90th percentile
    fig.add_vline(x=int(stats[32]), line_width=3, line_color="#FFFB0B") # 95th percentile
    
    fig.add_traces([
    go.Scatter(x=[100], y= [1], mode='lines', name='10th percentile', line=dict(color="#77C14C")),
    go.Scatter(x=[100], y= [1], mode='lines', name='1st quartile', line=dict(color="#1FAFEE")),
    go.Scatter(x=[100], y= [1], mode='lines', name='50th percentile', line=dict(color="#D53614")),
    go.Scatter(x=[100], y= [1], mode='lines', name='3rd quartile', line=dict(color="#D59D14")),
    go.Scatter(x=[100], y= [1], mode='lines', name='90th percentile', line=dict(color="#FFA4F5")),
    go.Scatter(x=[100], y= [1], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"))
    ])
    
    fig.update_layout(xaxis={'range': [0,limit]}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700)
    return fig

es_statistics_figure = get_language_statistics_figure(R.es_stats)
en_statistics_figure = get_language_statistics_figure(R.en_stats)
ontology_figure = get_ontology_figure()
es_instance_types_figure = get_instance_types_figure(R.instance_types_es)
en_instance_types_figure = get_instance_types_figure(R.instance_types_en)
es_valid_types_figure = get_valid_types_figure(R.valid_types_es)
en_valid_types_figure = get_valid_types_figure(R.valid_types_en)
es_sfpie_figure = get_sfpie_figure(R.es_dashboard_directory)
en_sfpie_figure = get_sfpie_figure(R.en_dashboard_directory)
es_uriCounts_figure = get_init_bar_figure(R.es_dashboard_directory, R.uriCounts_es)
es_pairCounts_figure = get_init_bar_figure(R.es_dashboard_directory, R.pairCounts_es)
es_sfAndTotalCounts_figure = get_init_bar_figure(R.es_dashboard_directory, R.sfAndTotalCounts_es)
es_top_valid_types_figure =  get_init_bar_figure(R.es_dashboard_directory, R.top_valid_types_es)
en_uriCounts_figure = get_init_bar_figure(R.en_dashboard_directory, R.uriCounts_en)
en_pairCounts_figure = get_init_bar_figure(R.en_dashboard_directory, R.pairCounts_en)
en_sfAndTotalCounts_figure = get_init_bar_figure(R.en_dashboard_directory, R.sfAndTotalCounts_en)
en_top_valid_types_figure =  get_init_bar_figure(R.en_dashboard_directory, R.top_valid_types_en)
es_pos_valid_types_figure =  get_init_bar_figure_pos(R.es_dashboard_directory, R.valid_types_es)
en_pos_valid_types_figure =  get_init_bar_figure_pos(R.en_dashboard_directory, R.valid_types_en)
