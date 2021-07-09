# -*- coding: utf-8 -*-
import pandas as pd
import os
import re

# Auxiliary function for processing TSV files

# TSV to dataframe
def tsv_to_df(path):
    if "uriCounts" in path: 
        df = pd.read_csv(path, sep='\t',  names=["DBpedia entity", "Count"])
    elif "known_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "known_types_top50" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities", "Pos"])
    elif "instance_types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia type", "Nº entities"])
    elif "pairCounts" in path:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "DBpedia entity", "Count"])
    else:
        df = pd.read_csv(path, sep='\t',  names=["Surface form", "Times linked", "Times as plain text"])
    return df

# End of auxiliary function for processing TSV files

# Getting dataframes

def get_ontology_df():
   # Load dataframe
   df = pd.read_csv(root_path + "resources/ontologies.csv")
   return  df


def get_instance_types_df(language_directory):
    # Load dataframe
    instance_types_df = tsv_to_df(language_directory + "instance_types")
    return instance_types_df

def get_known_types_df(language_directory):
    # Load dataframe
    known_types_df = tsv_to_df(language_directory + "known_types")
    return known_types_df

def get_statistics(dashboard_directory):
    if(es_dashboard_directory == dashboard_directory):
        file = open(es_dashboard_directory + "stats.txt", 'r')
        file = file.read()
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    else:
        file = open(en_dashboard_directory + "stats.txt", 'r')
        file = file.read()
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    return numbers


src_path = os.path.dirname(os.path.realpath(__file__))
root_path = src_path.replace("src","")
instance_types_file = "instance_types"
known_types_file = "known_types"
uriCounts_file = "uriCounts_top50"
pairCounts_file = "pairCounts_top50"
sfAndTotalCounts_file = "sfAndTotalCounts_top50"
top_known_types_file = "known_types_top50"
es_dashboard_directory = root_path + "resources/es/dashboard_data/"
en_dashboard_directory = root_path + "resources/en/dashboard_data/"
ontology_df = get_ontology_df()
instance_types_es = tsv_to_df(es_dashboard_directory + instance_types_file)
known_types_es = tsv_to_df(es_dashboard_directory + known_types_file)
uriCounts_es = tsv_to_df(es_dashboard_directory + uriCounts_file)
pairCounts_es = tsv_to_df(es_dashboard_directory + pairCounts_file)
sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + sfAndTotalCounts_file)
top_known_types_es = tsv_to_df(es_dashboard_directory + top_known_types_file)
es_stats = get_statistics(es_dashboard_directory)
instance_types_en = tsv_to_df(en_dashboard_directory + instance_types_file)
known_types_en = tsv_to_df(en_dashboard_directory + known_types_file)
uriCounts_en = tsv_to_df(en_dashboard_directory + uriCounts_file)
pairCounts_en = tsv_to_df(en_dashboard_directory + pairCounts_file)
sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + sfAndTotalCounts_file)
top_known_types_en = tsv_to_df(en_dashboard_directory + top_known_types_file)
en_stats = get_statistics(en_dashboard_directory)
