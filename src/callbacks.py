# -*- coding: utf-8 -*-
import dash
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import resources as R

def initialize_callbacks(app):                                                 
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
                    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
                    ),
                row=1, col=1
                )
            fig.add_trace(
                go.Indicator(
                    mode = "gauge+number",
                    value = float(R.en_stats[1]),
                    title = {'text': "Impact of English invalid types"},
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    gauge = {'axis': {'range': [0, 1]}, 'bar': {'color': "red"}}
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
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
            return figure
        
 # Spanish instance types callback
     @app.callback(
            dash.dependencies.Output('es_instance_types', 'figure'),
            [dash.dependencies.Input('ontologyy', 'clickData')]
            )
     def es_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.get_instance_types_df(R.es_dashboard_directory)
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
            return figure
        
 # Spanish top 50 valid types callback       
     @app.callback(
    dash.dependencies.Output("es_valid_types_stats", "figure"), 
    dash.dependencies.Input("es_top_valid_types_table", "active_cell"), 
    prevent_initial_call=True
)
     def update_valid_types_stats(active_cell):
        selected_row = active_cell["row"]
        label = R.top_valid_types_es["DBpedia type"].iloc[selected_row]
        value = R.top_valid_types_es["Nº entities"].iloc[selected_row]
        mean = float(R.es_stats[6])
        median = float(R.es_stats[7])
        std_dv = float(R.es_stats[9])
        fig = go.Figure() 
        fig.add_trace(go.Bar(x=[label], y = [value], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia type",
            text=str(value), textposition='outside',
                         ))
        
        fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
        fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
        fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
        fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,315000], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
        return fig

# Spanish top uriCounts callback       
     @app.callback(
    dash.dependencies.Output("es_uriCounts_stats", "figure"), 
    dash.dependencies.Input("es_uriCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def update_uriCounts_stats(active_cell):
        selected_row = active_cell["row"]
        label = R.uriCounts_es["DBpedia entity"].iloc[selected_row]
        value = R.uriCounts_es["Count"].iloc[selected_row]
        mean = float(R.es_stats[35])
        median = float(R.es_stats[36])
        std_dv = float(R.es_stats[38])
        fig = go.Figure() 
        fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia entity",
            text=str(value), textposition='outside',
                         ))
        
        fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
        fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
        fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
        fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
        return fig

# Spanish top pairCounts callback       
     @app.callback(
    dash.dependencies.Output("es_pairCounts_stats", "figure"), 
    dash.dependencies.Input("es_pairCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def update_pairCounts_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.pairCounts_es["Surface form"].iloc[selected_row]
         value = R.pairCounts_es["Count"].iloc[selected_row]
         mean = float(R.es_stats[39])
         median = float(R.es_stats[40])
         std_dv = float(R.es_stats[42])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected surface form",
            text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# Spanish top sfAndTotalCounts callback       
     @app.callback(
    dash.dependencies.Output("es_sfAndTotalCounts_stats", "figure"), 
    dash.dependencies.Input("es_sfAndTotalCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def update_sfAndTotalCounts_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.sfAndTotalCounts_es["Surface form"].iloc[selected_row]
         value = R.sfAndTotalCounts_es["Times linked"].iloc[selected_row]
         mean = float(R.es_stats[50])
         median = float(R.es_stats[51])
         std_dv = float(R.es_stats[53])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected surface form",
                         text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# Spanish valid types position measures callback
     @app.callback(
            dash.dependencies.Output('es_valid_types_pos', 'figure'),
            [dash.dependencies.Input('ontology_pos', 'clickData')]
            )
     def es_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.valid_types_es["DBpedia type"].values:
                selected_row = R.valid_types_es[R.valid_types_es["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.es_stats[14]), line_width=3, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.es_stats[11]), line_width=3, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.es_stats[22]), line_width=3, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.es_stats[12]), line_width=3, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.es_stats[30]), line_width=3, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.es_stats[32]), line_width=3, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[100], y= [1], mode='lines', name='10th percentile', line=dict(color="#77C14C")),
            go.Scatter(x=[100], y= [1], mode='lines', name='1st quartile', line=dict(color="#1FAFEE")),
            go.Scatter(x=[100], y= [1], mode='lines', name='50th percentile', line=dict(color="#D53614")),
            go.Scatter(x=[100], y= [1], mode='lines', name='3rd quartile', line=dict(color="#D59D14")),
            go.Scatter(x=[100], y= [1], mode='lines', name='90th percentile', line=dict(color="#FFA4F5")),
            go.Scatter(x=[100], y= [1], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"))
            ])
    
            fig.update_layout(xaxis={'range': [0,65]}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700)
            return fig
        
# English valid types callback
     @app.callback(
            dash.dependencies.Output('en_valid_types', 'figure'),
            [dash.dependencies.Input('en_ontology', 'clickData')]
            )
     def en_update_valid_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.get_valid_types_df(R.en_dashboard_directory)
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
            return figure
        
 # English instance types callback
     @app.callback(
            dash.dependencies.Output('en_instance_types', 'figure'),
            [dash.dependencies.Input('en_ontologyy', 'clickData')]
            )
     def en_update_instance_types_bar(clicked_data):
            selected_type = 'owlThing'
            types_count_df = R.get_instance_types_df(R.en_dashboard_directory)
            ontology_df = R.get_ontology_df()
            if clicked_data is not None:
                if 'entry' not in clicked_data['points'][0].keys() or clicked_data['points'][0]['label'] == clicked_data['points'][0]['entry']:
                    selected_type = clicked_data['points'][0]['parent']
                else:
                    selected_type = clicked_data['points'][0]['label']
            selected_ontology_df_labels = ontology_df[ontology_df['parents'] == selected_type]['labels']
            if selected_ontology_df_labels.empty:
                selected_ontology_df_labels = ontology_df[ontology_df['labels'] == selected_type]['labels']
            selected_all_instances_df = types_count_df[types_count_df['DBpedia type'].isin(selected_ontology_df_labels)]
            selected_all_instances_df = selected_all_instances_df.sort_values(by='Nº entities', ascending=False)
            if selected_all_instances_df.empty:
                selected_all_instances_df.append({'DBpedia type': selected_type, 'Nº entities': 0}, ignore_index=True)
            figure = go.Figure(go.Bar(x = selected_all_instances_df['Nº entities'], y = selected_all_instances_df['DBpedia type'], orientation='h', marker_color='#A349A4'))
            figure.update_layout(margin=dict(t=0, b=0, r=0, l=0, pad=0), height=400, width=700, yaxis=dict(showgrid=False), template = "simple_white")
            return figure
        
 # English top 50 valid types callback       
     @app.callback(
    dash.dependencies.Output("en_valid_types_stats", "figure"), 
    dash.dependencies.Input("en_top_valid_types_table", "active_cell"), 
    prevent_initial_call=True
)
     def en_update_valid_types_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.top_valid_types_en["DBpedia type"].iloc[selected_row]
         value = R.top_valid_types_en["Nº entities"].iloc[selected_row]
         mean = float(R.en_stats[6])
         median = float(R.en_stats[7])
         std_dv = float(R.en_stats[9])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [value], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia type",
            text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1360000], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# English top uriCounts callback       
     @app.callback(
    dash.dependencies.Output("en_uriCounts_stats", "figure"), 
    dash.dependencies.Input("en_uriCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def en_update_uriCounts_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.uriCounts_en["DBpedia entity"].iloc[selected_row]
         value = R.uriCounts_en["Count"].iloc[selected_row]
         mean = float(R.en_stats[35])
         median = float(R.en_stats[36])
         std_dv = float(R.en_stats[38])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected DBpedia entity",
            text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# English top pairCounts callback       
     @app.callback(
    dash.dependencies.Output("en_pairCounts_stats", "figure"), 
    dash.dependencies.Input("en_pairCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def en_update_pairCounts_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.pairCounts_en["Surface form"].iloc[selected_row]
         value = R.pairCounts_en["Count"].iloc[selected_row]
         mean = float(R.en_stats[39])
         median = float(R.en_stats[40])
         std_dv = float(R.en_stats[42])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected surface form",
            text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# English top sfAndTotalCounts callback       
     @app.callback(
    dash.dependencies.Output("en_sfAndTotalCounts_stats", "figure"), 
    dash.dependencies.Input("en_sfAndTotalCounts_table", "active_cell"), 
    prevent_initial_call=True
)
     def en_update_sfAndTotalCounts_stats(active_cell):
         selected_row = active_cell["row"]
         label = R.sfAndTotalCounts_en["Surface form"].iloc[selected_row]
         value = R.sfAndTotalCounts_en["Times linked"].iloc[selected_row]
         mean = float(R.en_stats[50])
         median = float(R.en_stats[51])
         std_dv = float(R.en_stats[53])
         fig = go.Figure() 
         fig.add_trace(go.Bar(x=[label], y = [1400], width=[0.5], marker_color='#A349A4', name = "Selected surface form",
            text=str(value), textposition='outside',
                         ))
        
         fig.add_trace(go.Bar(x=["Mean"], y=[mean], width=[0.5], marker_color='#FFC300', name = "Mean",
                         text=str(mean), textposition='outside'
                         ))
         fig.add_trace(go.Bar(x=["Median"], y=[median], width=[0.5], marker_color='#C7FF33', name = "Median",
                  text=str(median), textposition='outside'))
         fig.add_trace(go.Bar(x=["Standard deviation"], y=[std_dv], width=[0.5], marker_color='#33E6FF', name = "Standar deviation",
                  text=str(std_dv), textposition='outside'))    
           
         fig.update_layout(yaxis={'visible': False}, yaxis_range=[0,1500], margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white")
         return fig

# English valid types position measures callback
     @app.callback(
            dash.dependencies.Output('en_valid_types_pos', 'figure'),
            [dash.dependencies.Input('en_ontology_pos', 'clickData')]
            )
     def en_update_inits_bar_pos(clicked_data):
            if clicked_data is None:
                return dash.no_update
            selected_type = clicked_data['points'][0]['label'] 
            if selected_type in R.valid_types_en["DBpedia type"].values:
                selected_row = R.valid_types_en[R.valid_types_en["DBpedia type"] == selected_type]
                fig = go.Figure(go.Bar(x = [selected_row.iloc[0]['Pos']], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            else:
                fig = go.Figure(go.Bar(x = [0], y = [selected_type], width=[0.1] , orientation='h', marker_color='#A349A4', name = "Selected DBpedia type"))
            
            fig.add_vline(x=int(R.en_stats[14]), line_width=3, line_color="#77C14C") # 10th percentile
            fig.add_vline(x=int(R.en_stats[11]), line_width=3, line_color="#1FAFEE") # 1st quartile
            fig.add_vline(x=int(R.en_stats[22]), line_width=3, line_color="#D53614") # 50th percentile
            fig.add_vline(x=int(R.en_stats[12]), line_width=3, line_color="#D59D14") # 3rd quartile
            fig.add_vline(x=int(R.en_stats[30]), line_width=3, line_color="#FFA4F5") # 90th percentile
            fig.add_vline(x=int(R.en_stats[32]), line_width=3, line_color="#FFFB0B") # 95th percentile
    
            fig.add_traces([
            go.Scatter(x=[100], y= [1], mode='lines', name='10th percentile', line=dict(color="#77C14C")),
            go.Scatter(x=[100], y= [1], mode='lines', name='1st quartile', line=dict(color="#1FAFEE")),
            go.Scatter(x=[100], y= [1], mode='lines', name='50th percentile', line=dict(color="#D53614")),
            go.Scatter(x=[100], y= [1], mode='lines', name='3rd quartile', line=dict(color="#D59D14")),
            go.Scatter(x=[100], y= [1], mode='lines', name='90th percentile', line=dict(color="#FFA4F5")),
            go.Scatter(x=[100], y= [1], mode='lines', name='95th percentile', line=dict(color="#FFFB0B"))
            ])
    
            fig.update_layout(xaxis={'range': [0,130]}, margin=dict(t=0, b=0, r=0, l=0, pad=0), template = "simple_white", height=400, width=700)
            return fig
        