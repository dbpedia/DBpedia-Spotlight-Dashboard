# Search invalid URLs in file
def is_url_invalid(url):
    with open(es_invalid_urls_file) as f:
        if url in f.read():
            return True
        else:
            return False


# Draft function due to technical problems
def get_stats(df,file):
    url_column = df["URI"]
    count_column = df["Count"]
    stats=[]
    valid_unique_links = 0
    total_invalid_links = 0
    total_unique_links = len(df)
    total_links = count_column.sum()
    
    # Iterating over URI column
    for url in url_column.values:
        count_value = int(df.loc[url_column == url, count_column].iloc[1])
        if(is_url_invalid(url,file)):
            total_invalid_links += count_value
        else:
            valid_unique_links += 1
            
    precision = valid_unique_links / total_unique_links
    impact = total_invalid_links / total_links
    stats.append(precision,impact)
    
    return stats

            
# Assuming we get these files from get_resources.sh script 
es_invalid_urls_file = "resources/es/dashboard_data/invalid_urls"
en_invalid_urls_file = "resources/en/dashboard_data/invalid_urls"

if __name__ == '__main__':

    print('Getting precision and impact for Spanish language')
    es_precision = get_stats('uri_df from resources.py',es_invalid_urls_file)[0]
    es_impact = get_stats('uri_df from resources.py',es_invalid_urls_file)[1]

    print('Getting precision and impact for English language')
    en_precision = get_stats('uri_df from resources.py',en_invalid_urls_file)[0]
    en_impact = get_stats('uri_df from resources.py',en_invalid_urls_file)[1]
    