import resources as R

# Count lines of a file
def size_file(file):
    num_lines = sum(1 for line in open(file, encoding="utf-8"))
    return num_lines

# Get precision and impact of URLs
def get_stats(valid_file,invalid_file):
    valid_urls = size_file(valid_file)
    invalid_urls = size_file(invalid_file)
    total_urls = valid_urls + invalid_urls
    stats=[]
    precision = round(valid_urls / total_urls, 3)
    impact = round(invalid_urls / total_urls, 3)
    stats.append(precision)
    stats.append(impact)
    return stats
    

es_invalid_urls_file = R.es_dashboard_directory + "invalid_urls"
es_valid_urls_file = R.es_dashboard_directory + "valid_urls"
en_invalid_urls_file = R.en_dashboard_directory + "invalid_urls"
en_valid_urls_file = R.en_dashboard_directory + "valid_urls"

if __name__ == '__main__':
    es_stats_file = open(R.es_dashboard_directory + "stats.txt", "w+")
    print('Getting precision and impact')
    es_stats = get_stats(es_valid_urls_file, es_invalid_urls_file)
    es_precision = es_stats[0]
    es_impact = es_stats[1]
    es_stats_file.write("Precision: " + str(es_precision) + "\n" + "Impact: " + str(es_impact) + "\n" )
    es_stats_file.close()
    en_stats_file = open(R.en_dashboard_directory + "stats.txt", "w+")
    en_stats = get_stats(en_valid_urls_file, en_invalid_urls_file)
    en_precision = en_stats[0]
    en_impact = en_stats[1]
    en_stats_file.write("Precision: " + str( en_precision) + "\n" + "Impact: " + str(en_impact) + "\n" )
    en_stats_file.close()
    print('Done')
    