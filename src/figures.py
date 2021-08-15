# -*- coding: utf-8 -*-
import plotly.graph_objects as go
import resources as R
import re

# Instance types tab figures
def get_language_statistics_figure(lang):
    if lang == 'es':
        image = "https://raw.githubusercontent.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_urls_impact.png"
    else:
        image = "https://raw.githubusercontent.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/en_urls_impact.png"

    # Constants
    img_width = 1666
    img_height = 445
    scale_factor = 0.55
    
    # Create figure
    fig = go.Figure()
    
    # Add invisible scatter trace.
    # This trace is added to help the autoresize logic work.
    fig.add_trace(
        go.Scatter(
            x=[0, img_width * scale_factor],
            y=[0, img_height * scale_factor],
            mode="markers",
            marker_opacity=0
        )
    )
    
    # Configure axes
    fig.update_xaxes(
        visible=False,
        range=[0, img_width * scale_factor]
    )
    
    fig.update_yaxes(
        visible=False,
        range=[0, img_height * scale_factor],
        # the scaleanchor attribute ensures that the aspect ratio stays constant
        scaleanchor="x"
    )
        # Add image
    fig.add_layout_image(
        dict(
            x=0,
            sizex=img_width * scale_factor,
            y=img_height * scale_factor,
            sizey=img_height * scale_factor,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch",
            source=image)
    )
    
    # Configure other layout
    fig.update_layout(
        width=img_width * scale_factor,
        height=img_height * scale_factor,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
        template = "simple_white"
    )
    
    return fig

def get_ontology_figure():
    ontology_df = R.ontology_df
    # Ontology treemap 
    fig2 =  go.Figure(go.Treemap(labels=ontology_df['labels'], parents=ontology_df['parents']))
    fig2.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0))
    return fig2


def get_instance_types_figure(language_directory, instance_types_df):
    if language_directory == R.es_dashboard_directory:
        mean = R.versions_stats[38]
        std_dev = R.versions_stats[40]
    else:
        mean = R.versions_stats[110]
        std_dev = R.versions_stats[112]
    # Instance types Bar 
    fig3 = go.Figure(go.Bar(x = instance_types_df['Nº entities'], y = instance_types_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia type"))
    fig3.add_vline(x=float(mean), line_width=4, line_color="#77C14C") # Mean
    fig3.add_vline(x=float(std_dev), line_width=4, line_color="#D53614") # Standard deviation
    fig3.add_traces([
    go.Scatter(x=[float(mean)], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[mean], hoverinfo="text"),
    go.Scatter(x=[float(std_dev)], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[std_dev], hoverinfo="text")
    ])
    fig3.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig3


def get_known_types_figure(language_directory, known_types_df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
    else:
        stats = R.en_stats
        
    # Valid types Bar 
    fig4 = go.Figure(go.Bar(x = known_types_df['Nº entities'], y = known_types_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = "DBpedia entity"))
    fig4.add_vline(x=float(stats[4]), line_width=4, line_color="#77C14C") # Mean
    fig4.add_vline(x=float(stats[6]), line_width=4, line_color="#D53614") # Standard deviation
    fig4.add_traces([
    go.Scatter(x=[float(stats[4])], y= [" "], mode='lines', name='Mean', line=dict(color="#77C14C"), hovertext=[stats[4]], hoverinfo="text"),
    go.Scatter(x=[float(stats[6])], y= [" "], mode='lines', name='Standard deviation', line=dict(color="#D53614"), hovertext=[stats[6]], hoverinfo="text")
    ])
    fig4.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig4

def get_sfpie_figure(values):
    # sfAndTotalCounts pie chart
    labels = ['Without associated link','Not appearing as text','Not appearing as text without associated link','Rest']
    fig5 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig5.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0))
    return fig5


def get_init_bar_figure_pos(language_directory,df):
    if language_directory == R.es_dashboard_directory:
        stats = R.es_stats
        known_types = R.known_types_es_2021_05_01_without_repetitions
    else:
        known_types = R.known_types_en_2021_05_01_without_repetitions
        stats = R.en_stats
        
    x = known_types["DBpedia type"].tolist()
    cumulative = known_types["Cumulative total"].tolist()
    n_entities = known_types["Nº entities"].tolist()
    quartile1 = list()
    quartile1_text = list()
    quartile2 = list()
    quartile2_text = list()
    quartile3 = list()
    quartile3_text = list()
    quartile4 = list()
    quartile4_text = list()
    p90 = list()
    p90_text = list()
    p95 = list()
    p95_text = list()
    i = 0
    for value in cumulative:
        if value <= float(stats[8]): # 1st quartile
            quartile1.append(n_entities[i])
            quartile1_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        if value <= float(stats[14]): # 2nd quartile
            quartile2.append(n_entities[i])
            quartile2_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        if value <= float(stats[9]): # 3rd quartile
            quartile3.append(n_entities[i])
            quartile3_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        if value <= float(stats[18]): # 90th percentile
            p90.append(n_entities[i])
            p90_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        if value <= float(stats[19]): # 95th percentile
            p95.append(n_entities[i])
            p95_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        # 4th quartile
        quartile4.append(n_entities[i])
        quartile4_text.append("("+ x[i]+", " + str(n_entities[i])+")")
        i+=1
        
    # For displaying positional measures
    fig = go.Figure()
    
     # 1st quartile
    fig.add_trace(go.Scatter(
        x=x, y=quartile1,
        name='Quartile 1',
        hoverinfo="text",
        hovertext=quartile1_text,
        mode='lines',
        line=dict(width=0.5, color="#1FAFEE"),
        stackgroup='one',
        groupnorm='percent'
    ))
     # 2nd quartile
    fig.add_trace(go.Scatter(
        x=x, y=quartile2,
        name='Quartile 2',
        mode='lines',
        hoverinfo="text",
        hovertext=quartile2_text,
        line=dict(width=0.5, color="#D53614"),
        stackgroup='one' # define stack group
    ))
      # 3rd quartile
    fig.add_trace(go.Scatter(
        x=x, y=quartile3,
        name='Quartile 3',
        hoverinfo="text",
        hovertext=quartile3_text,
        mode='lines',
        line=dict(width=0.5, color="#D59D14"),
        stackgroup='one' # define stack group
    ))
    
          # 90th percentile
    fig.add_trace(go.Scatter(
        x=x, y=p90,
        name='Percentile 90',
        mode='lines',
        hoverinfo="text",
        hovertext=p90_text,
        line=dict(width=0.5, color="#FFA4F5"),
        stackgroup='one' # define stack group
    ))
    
           # 95th percentile
    fig.add_trace(go.Scatter(
        x=x, y=p95,
        name='Percentile 95',
        mode='lines',
        hoverinfo="text",
        hovertext=p95_text,
        line=dict(width=0.5, color="#FFFB0B"),
        stackgroup='one' # define stack group
    ))
    
         # 4th quartile
    fig.add_trace(go.Scatter(
        x=x, y=quartile4,
        name='Quartile 4',
        hoverinfo="text",
        hovertext=quartile4_text,
        mode='lines',
        line=dict(width=0.5, color='rgb(184, 247, 212)'),
        stackgroup='one' # define stack group
    ))
    
    fig.update_layout(
    showlegend=True,
    margin=dict(t=0, b=0, r=0, l=0, pad=0),
    template = "simple_white",
    xaxis_type='category',
    yaxis=dict(
        type='linear',
        tickmode = 'array',
        tickvals = [0, 17, 33, 50, 67, 83, 100],
        ticktext = ['0%', '25%', '50%', '75%', '90%', '95%', '100%']
        ),
    xaxis_title="DBpedia type", yaxis_title="Percent of information per instance")

    return fig

# Comparison tab figures

def get_version_bar_figure(labels, values):
    fig = go.Figure()
    fig.add_trace(go.Bar(x= [int(values[0])], orientation='h', marker_color='#A349A4', name = labels[0], hovertext=[values[0]], hoverinfo="text"))
    fig.add_trace(go.Bar(x= [int(values[1])], orientation='h', marker_color="#77C14C", name = labels[1], hovertext=[values[1]], hoverinfo="text"))
    
    fig.update_layout(yaxis={'ticks':'', 'showticklabels':False}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia version")
    return fig
    
def get_version_pie_figure(labels,values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0))
    return fig

def get_versions_instance_types_figure(labels, version1_df, version2_df):
    fig = go.Figure()
    # Instance types Bar
    fig.add_trace(go.Bar(x = version1_df['Nº entities'], y = version1_df['DBpedia type'], orientation='h', marker_color='#A349A4', name = labels[0]))
    fig.add_trace(go.Bar(x = version2_df['Nº entities'], y = version2_df['DBpedia type'], orientation='h', marker_color="#77C14C", name = labels[1]))
    
    fig.update_layout(barmode='group', margin=dict(t=0, b=0, r=0, l=0, pad=0), yaxis=dict(showgrid=False), template = "simple_white", xaxis_title="Number of DBpedia entities", yaxis_title="DBpedia type")
    return fig

pattern = re.compile("(\(.*?)\)")


def color_brackets(value):
    found = re.search(pattern, value)

    if found:
        if found.group()[1] == "+":
            color = "green"
        elif found.group()[1] == "-":
            color = "red"
        else:
            color = "black"
            
        substituted = pattern.sub(
            f"<span style='color: {color};'>{found.group()}</span>", value
        )
        return substituted

    return value

es_statistics_figure = get_language_statistics_figure("es")
en_statistics_figure = get_language_statistics_figure("en")
ontology_figure = get_ontology_figure()
es_instance_types_figure = get_instance_types_figure(R.es_dashboard_directory, R.instance_types_es_2021_05_01)
en_instance_types_figure = get_instance_types_figure(R.en_dashboard_directory, R.instance_types_en_2021_05_01)
es_known_types_figure = get_known_types_figure(R.es_dashboard_directory, R.known_types_es_2021_05_01)
en_known_types_figure = get_known_types_figure(R.en_dashboard_directory, R.known_types_en_2021_05_01)
es_pos_known_types_figure =  get_init_bar_figure_pos(R.es_dashboard_directory, R.known_types_es_2021_05_01)
en_pos_known_types_figure =  get_init_bar_figure_pos(R.en_dashboard_directory, R.known_types_en_2021_05_01)
