import pandas as pd
import time
import os


# Auxiliary functions for processing TSV files

# TSV to dataframe
def tsv_to_df(path):
    if "uriCounts" in path: 
        df = pd.read_csv(path, sep='\t',  names=["URI", "Count"])
    elif "types" in path:
        df = pd.read_csv(path, sep=' ',  names=["DBpedia Type", "Count"])
    
    return df

# Join partial dataframes
def join_tsv_df(df,lang_directory):
    start = time.time()
    for filename in os.listdir(lang_directory):
        if "uriCounts" in filename and filename != uriCounts_first_file:
            print('Parsing TSV file: ' + filename)
            df = pd.concat([df,tsv_to_df(lang_directory + filename)])
            print("Joining dataframes")
    end = time.time()
    print('Done in ' + str(end-start) +' seconds')
    return df

# End of auxiliary functions for processing wikistats (TSV files)

types_file = "types.tsv"
uriCounts_first_file = "uriCounts_aa"

es_dashboard_directory = "resources/es/dashboard_data/"
en_dashboard_directory = "resources/en/dashboard_data/"


print('Processing Spanish instance-types')
instance_types_es = tsv_to_df(es_dashboard_directory + types_file)
print('Done')


print('Processing English instance-types')
instance_types_en = tsv_to_df(en_dashboard_directory + types_file)
print('Done')


'''
print('Processing Spanish uriCounts')
uriCounts_es = join_tsv_df(tsv_to_df(es_dashboard_directory + uriCounts_first_file), es_dashboard_directory)
print('Done')


print('Processing English uriCounts')
uriCounts_en = join_tsv_df(tsv_to_df(en_dashboard_directory + uriCounts_first_file), en_dashboard_directory)
print('Done')
'''

