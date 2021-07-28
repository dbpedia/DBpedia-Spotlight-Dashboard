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
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    else:
        file = open(en_dashboard_directory + "stats.txt", 'r')
        file = file.read()
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    return numbers

def get_version_statistics(resources_directory):
    file = open(resources_directory + "versions_statistics.txt", 'r')
    file = file.read()
    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
    return numbers


src_path = os.path.dirname(os.path.realpath(__file__))
root_path = src_path.replace("src","")
instance_types_file = "instance_types"
known_types_file = "known_types"
top_2016_uriCounts_file = "uriCounts_2016_top50"
top_2016_pairCounts_file = "pairCounts_2016_top50"
top_2016_sfAndTotalCounts_file = "sfAndTotalCounts_2016_top50"
top_2016_tokenCounts_file = "tokenCounts_2016_top50"
top_uriCounts_file = "uriCounts_top50"
top_pairCounts_file = "pairCounts_top50"
top_sfAndTotalCounts_file = "sfAndTotalCounts_top50"
top_tokenCounts_file = "tokenCounts_top50"
top_known_types_file = "known_types_top50"
es_dashboard_directory = root_path + "resources/es/dashboard_data/"
en_dashboard_directory = root_path + "resources/en/dashboard_data/"
versions_directory =  root_path + "resources/versions/"
ontology_df = tsv_to_df(root_path + "resources/ontologies.csv")
instance_types_es = tsv_to_df(es_dashboard_directory + instance_types_file)
known_types_es = tsv_to_df(es_dashboard_directory + known_types_file)
top_2016_uriCounts_es = tsv_to_df(es_dashboard_directory + top_2016_uriCounts_file)
top_2016_pairCounts_es = tsv_to_df(es_dashboard_directory + top_2016_pairCounts_file)
top_2016_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_2016_sfAndTotalCounts_file)
top_2016_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_2016_tokenCounts_file)
top_uriCounts_es = tsv_to_df(es_dashboard_directory + top_uriCounts_file)
top_pairCounts_es = tsv_to_df(es_dashboard_directory + top_pairCounts_file)
top_sfAndTotalCounts_es = tsv_to_df(es_dashboard_directory + top_sfAndTotalCounts_file)
top_tokenCounts_es = tsv_to_df(es_dashboard_directory + top_tokenCounts_file)
top_known_types_es = tsv_to_df(es_dashboard_directory + top_known_types_file)
es_stats = get_statistics(es_dashboard_directory)
instance_types_en = tsv_to_df(en_dashboard_directory + instance_types_file)
known_types_en = tsv_to_df(en_dashboard_directory + known_types_file)
top_2016_uriCounts_en = tsv_to_df(en_dashboard_directory +top_2016_uriCounts_file)
top_2016_pairCounts_en = tsv_to_df(en_dashboard_directory + top_2016_pairCounts_file)
top_2016_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_2016_sfAndTotalCounts_file)
top_2016_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_2016_tokenCounts_file)
top_uriCounts_en = tsv_to_df(en_dashboard_directory +top_uriCounts_file)
top_pairCounts_en = tsv_to_df(en_dashboard_directory + top_pairCounts_file)
top_sfAndTotalCounts_en = tsv_to_df(en_dashboard_directory + top_sfAndTotalCounts_file)
top_tokenCounts_en = tsv_to_df(en_dashboard_directory + top_tokenCounts_file)
top_known_types_en = tsv_to_df(en_dashboard_directory + top_known_types_file)
en_stats = get_statistics(en_dashboard_directory)
versions_stats = get_version_statistics(root_path + "resources/versions/")
instance_types_es_2016_10_01 = tsv_to_df(versions_directory + "instance_types_es_2016.10.01")
instance_types_es_2020_10_01 = tsv_to_df(versions_directory + "instance_types_es_2020.10.01")
instance_types_es_2021_05_01 = tsv_to_df(versions_directory + "instance_types_es_2021.05.01")
instance_types_es_2021_06_01 = tsv_to_df(versions_directory + "instance_types_es_2021.06.01")
instance_types_en_2016_10_01 = tsv_to_df(versions_directory + "instance_types_en_2016.10.01")
instance_types_en_2020_10_01 = tsv_to_df(versions_directory + "instance_types_en_2020.10.01")
instance_types_en_2021_05_01 = tsv_to_df(versions_directory + "instance_types_en_2021.05.01")
instance_types_en_2021_06_01 = tsv_to_df(versions_directory + "instance_types_en_2021.06.01")
