# -*- coding: utf-8 -*-
import pandas as pd
import os
import re

# Auxiliary function for processing TSV files

# TSV to dataframe
def tsv_to_df(path):
    if "uriCounts" in path: 
        df = pd.read_csv(path, sep='\t',  names=["DBpedia entity", "Count"])
    elif "known_types_without_repetitions" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Cumulative total"])
    elif "known_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "known_types_top50" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "instance_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities"])
    elif "pairCounts" in path:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "DBpedia entity", "Times linked"])
    elif "token" in path:
        df = pd.read_csv(path, sep=' ',  names=["Wikipedia article", " ", "Nº tokens"])
    elif "ontologies" in path:
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "Times linked", "Times as plain text"])
    return df

# End of auxiliary function for processing TSV files

# Getting statistics

def get_statistics(dashboard_directory):
    if(es_dashboard_directory == dashboard_directory):
        file = open(es_dashboard_directory + "stats.txt", 'r')
        file = file.read()
        numbers = re.findall(r"(?<=: )\d*\.?\d+", file)
    else:
        file = open(en_dashboard_directory + "stats.txt", 'r')
        file = file.read()
        numbers = re.findall(r"(?<=: )\d*\.?\d+", file)
    return numbers

def get_version_statistics(resources_directory):
    file = open(resources_directory + "versions_statistics.txt", 'r')
    file = file.read()
    numbers = re.findall(r"(?<=: )\d*\.?\d+", file)
    return numbers


src_path = os.path.dirname(os.path.realpath(__file__))
root_path = src_path.replace("src","")
es_dashboard_directory = root_path + "resources/es/dashboard_data/"
en_dashboard_directory = root_path + "resources/en/dashboard_data/"
versions_directory =  root_path + "resources/versions/"
# Known types files
known_types_file = "known_types"
top_known_types_file = "known_types_top50"
known_types_without_repetitions_file = "known_types_without_repetitions"
# Ontology dataframe
ontology_df = tsv_to_df(root_path + "resources/ontologies.csv")
# Known types dataframes
known_types_es_2021_05_01 = tsv_to_df(es_dashboard_directory + known_types_file)
known_types_en_2021_05_01 = tsv_to_df(en_dashboard_directory + known_types_file)
top_known_types_2021_05_es = tsv_to_df(es_dashboard_directory + top_known_types_file)
top_known_types_2021_05_en = tsv_to_df(en_dashboard_directory + top_known_types_file)
# Known types without repetitions
known_types_es_2021_05_01_without_repetitions = tsv_to_df(es_dashboard_directory + known_types_without_repetitions_file)
known_types_en_2021_05_01_without_repetitions = tsv_to_df(en_dashboard_directory + known_types_without_repetitions_file)
# Instance types 2016 dataframes
instance_types_es_2016_10_01 = tsv_to_df(versions_directory + "instance_types_es_2016.10.01")
instance_types_en_2016_10_01 = tsv_to_df(versions_directory + "instance_types_en_2016.10.01")
# Instance types 2020 dataframes
instance_types_es_2020_10_01 = tsv_to_df(versions_directory + "instance_types_es_2020.10.01")
instance_types_en_2020_10_01 = tsv_to_df(versions_directory + "instance_types_en_2020.10.01")
# Instance types May 2021 dataframes
instance_types_es_2021_05_01 = tsv_to_df(versions_directory + "instance_types_es_2021.05.01")
instance_types_en_2021_05_01 = tsv_to_df(versions_directory + "instance_types_en_2021.05.01")
# Instance types June 2021 dataframes
instance_types_es_2021_06_01 = tsv_to_df(versions_directory + "instance_types_es_2021.06.01")
instance_types_en_2021_06_01 = tsv_to_df(versions_directory + "instance_types_en_2021.06.01")
# Wikistats 2016 files
top_2016_uriCounts_file = "uriCounts_2016_top50"
top_2016_pairCounts_file = "pairCounts_2016_top50"
top_2016_sfAndTotalCounts_file = "sfAndTotalCounts_2016_top50"
top_2016_tokenCounts_file = "tokenCounts_2016_top50"
# Wikistats 2020 files
top_2020_uriCounts_file = "uriCounts_2020_top50"
top_2020_pairCounts_file = "pairCounts_2020_top50"
top_2020_sfAndTotalCounts_file = "sfAndTotalCounts_2020_top50"
top_2020_tokenCounts_file = "tokenCounts_2020_top50"
# Wikistats May 2021 files
top_2021_05_uriCounts_file = "uriCounts_2021_may_top50"
top_2021_05_pairCounts_file = "pairCounts_2021_may_top50"
top_2021_05_sfAndTotalCounts_file = "sfAndTotalCounts_2021_may_top50"
top_2021_05_tokenCounts_file = "tokenCounts_2021_may_top50"
# Wikistats June 2021 files
top_2021_06_uriCounts_file = "uriCounts_2021_june_top50"
top_2021_06_pairCounts_file = "pairCounts_2021_june_top50"
top_2021_06_sfAndTotalCounts_file = "sfAndTotalCounts_2021_june_top50"
top_2021_06_tokenCounts_file = "tokenCounts_2021_june_top50"
# Wikistats 2016 dataframes
top_2016_uriCounts_es = tsv_to_df(es_dashboard_directory + top_2016_uriCounts_file)
top_2016_pairCounts_es = tsv_to_df(es_dashboard_directory + top_2016_pairCounts_file)
top_2016_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_2016_sfAndTotalCounts_file)
top_2016_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_2016_tokenCounts_file)
top_2016_uriCounts_en = tsv_to_df(en_dashboard_directory +top_2016_uriCounts_file)
top_2016_pairCounts_en = tsv_to_df(en_dashboard_directory + top_2016_pairCounts_file)
top_2016_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_2016_sfAndTotalCounts_file)
top_2016_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_2016_tokenCounts_file)
# Wikistats 2020 dataframes
top_2020_uriCounts_es = tsv_to_df(es_dashboard_directory + top_2020_uriCounts_file)
top_2020_pairCounts_es = tsv_to_df(es_dashboard_directory + top_2020_pairCounts_file)
top_2020_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_2020_sfAndTotalCounts_file)
top_2020_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_2020_tokenCounts_file)
top_2020_uriCounts_en = tsv_to_df(en_dashboard_directory + top_2020_uriCounts_file)
top_2020_pairCounts_en = tsv_to_df(en_dashboard_directory + top_2020_pairCounts_file)
top_2020_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_2020_sfAndTotalCounts_file)
top_2020_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_2020_tokenCounts_file)
# Wikistats May 2021 dataframes
top_2021_05_uriCounts_es = tsv_to_df(es_dashboard_directory + top_2021_05_uriCounts_file)
top_2021_05_pairCounts_es = tsv_to_df(es_dashboard_directory + top_2021_05_pairCounts_file)
top_2021_05_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_2021_05_sfAndTotalCounts_file)
top_2021_05_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_2021_05_tokenCounts_file)
top_2021_05_uriCounts_en = tsv_to_df(en_dashboard_directory + top_2021_05_uriCounts_file)
top_2021_05_pairCounts_en = tsv_to_df(en_dashboard_directory + top_2021_05_pairCounts_file)
top_2021_05_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_2021_05_sfAndTotalCounts_file)
top_2021_05_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_2021_05_tokenCounts_file)
# Wikistats June 2021 dataframes
top_2021_06_uriCounts_es = tsv_to_df(es_dashboard_directory + top_2021_06_uriCounts_file)
top_2021_06_pairCounts_es = tsv_to_df(es_dashboard_directory + top_2021_06_pairCounts_file)
top_2021_06_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_2021_06_sfAndTotalCounts_file)
top_2021_06_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_2021_06_tokenCounts_file)
top_2021_06_uriCounts_en = tsv_to_df(en_dashboard_directory + top_2021_06_uriCounts_file)
top_2021_06_pairCounts_en = tsv_to_df(en_dashboard_directory + top_2021_06_pairCounts_file)
top_2021_06_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_2021_06_sfAndTotalCounts_file)
top_2021_06_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_2021_06_tokenCounts_file)
# Stats lists
es_stats = get_statistics(es_dashboard_directory)
en_stats = get_statistics(en_dashboard_directory)
versions_stats = get_version_statistics(root_path + "resources/versions/")

# Delete repeated entities

def del_entities(file):
    df = tsv_to_df(file)
    df2 = df.copy()
    types = df["DBpedia type"].tolist()
    parents = ontology_df["parents"].tolist()
    for tipo in types:
        updated_parent_value = 0
        children = ontology_df.loc[ontology_df['parents'] == tipo, 'labels'].values
        for sub_tipo in children:
            if tipo in parents and sub_tipo in df["DBpedia type"].values :
                if(updated_parent_value == 0):
                    parent_value =  df.loc[df["DBpedia type"] == tipo, 'Nº entities'].iloc[0]
                else:
                    parent_value = updated_parent_value
                child_value = df.loc[df["DBpedia type"] == sub_tipo, 'Nº entities'].iloc[0]
                updated_parent_value = parent_value - child_value
                df2.loc[df2['DBpedia type'] == tipo, 'Nº entities'] = updated_parent_value
    df2 = df2[df2['Nº entities'] > 0]
    df2 = df2.sort_values(by=['Nº entities'], ascending=False)
    if 'Pos' in df2.columns:
        df2 = df2.drop('Pos', 1)
    df2['Cumulative total'] = df2['Nº entities'].cumsum()
    df2.to_csv(file + "_without_repetitions", sep=' ', index=False, header=None)
    
del_entities(es_dashboard_directory + known_types_file)
del_entities(en_dashboard_directory + known_types_file)
del_entities(versions_directory + "instance_types_es_2016.10.01")
del_entities(versions_directory + "instance_types_en_2016.10.01")
del_entities(versions_directory + "instance_types_es_2020.10.01")
del_entities(versions_directory + "instance_types_en_2020.10.01")
del_entities(versions_directory + "instance_types_es_2021.05.01")
del_entities(versions_directory + "instance_types_en_2021.05.01")
del_entities(versions_directory + "instance_types_es_2021.06.01")
del_entities(versions_directory + "instance_types_en_2021.06.01")
