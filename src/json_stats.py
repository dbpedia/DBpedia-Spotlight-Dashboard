# -*- coding: utf-8 -*-
import os
import resources as R
import json

src_path = os.path.dirname(os.path.realpath(__file__))
root_path = src_path.replace("src","")
resources_directory = root_path + "resources/"
es_stats= R.es_stats
en_stats= R.en_stats
versions_stats = R.versions_stats

es= {}
# instanceTypes
es["instanceTypes"] = {}
es["instanceTypes"]["2016.10.01"] = {}
es["instanceTypes"]["2016.10.01"]["nElements"] = versions_stats[1]
es["instanceTypes"]["2016.10.01"]["mean"] = versions_stats[2]
es["instanceTypes"]["2016.10.01"]["median"] = versions_stats[3]
es["instanceTypes"]["2016.10.01"]["medianLabel"] = 'dbo:Athlete'
es["instanceTypes"]["2016.10.01"]["mode"] = '363756'
es["instanceTypes"]["2016.10.01"]["modeLabel"] = 'dbo:Agent'
es["instanceTypes"]["2016.10.01"]["standardDeviation"] = versions_stats[4]
es["instanceTypes"]["2016.10.01"]["q1"] = versions_stats[6]
es["instanceTypes"]["2016.10.01"]["q1Label"] = 'dbo:Place'
es["instanceTypes"]["2016.10.01"]["q3"] = versions_stats[7]
es["instanceTypes"]["2016.10.01"]["q3Label"] = 'dbo:ArchitecturalStructure'
es["instanceTypes"]["2016.10.01"]["perc10"] = versions_stats[8]
es["instanceTypes"]["2016.10.01"]["perc10Label"] = 'dbo:Agent'
es["instanceTypes"]["2016.10.01"]["perc50"] = versions_stats[12]
es["instanceTypes"]["2016.10.01"]["perc50Label"] = 'dbo:Athlete'
es["instanceTypes"]["2016.10.01"]["perc90"] = versions_stats[16]
es["instanceTypes"]["2016.10.01"]["perc90Label"] = 'dbo:Single'
es["instanceTypes"]["2016.10.01"]["perc95"] = versions_stats[17]
es["instanceTypes"]["2016.10.01"]["perc95Label"] = 'dbo:VideoGame'
es["instanceTypes"]["2020.10.01"] = {}
es["instanceTypes"]["2020.10.01"]["nElements"] = versions_stats[19]
es["instanceTypes"]["2020.10.01"]["mean"] = versions_stats[20]
es["instanceTypes"]["2020.10.01"]["median"] = versions_stats[21]
es["instanceTypes"]["2020.10.01"]["medianLabel"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2020.10.01"]["mode"] = '535166'
es["instanceTypes"]["2020.10.01"]["modeLabel"] = 'dbo:Agent'
es["instanceTypes"]["2020.10.01"]["standardDeviation"] = versions_stats[22]
es["instanceTypes"]["2020.10.01"]["q1"] = versions_stats[24]
es["instanceTypes"]["2020.10.01"]["q1Label"] = 'dbo:Place'
es["instanceTypes"]["2020.10.01"]["q3"] = versions_stats[25]
es["instanceTypes"]["2020.10.01"]["q3Label"] = 'dbo:ArchitecturalStructure'
es["instanceTypes"]["2020.10.01"]["perc10"] = versions_stats[26]
es["instanceTypes"]["2020.10.01"]["perc10Label"] = 'dbo:Agent'
es["instanceTypes"]["2020.10.01"]["perc50"] = versions_stats[30]
es["instanceTypes"]["2020.10.01"]["perc50Label"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2020.10.01"]["perc90"] = versions_stats[34]
es["instanceTypes"]["2020.10.01"]["perc90Label"] = 'dbo:NaturalPlace'
es["instanceTypes"]["2020.10.01"]["perc95"] = versions_stats[35]
es["instanceTypes"]["2020.10.01"]["perc95Label"] = 'dbo:RouteOfTransportation'
es["instanceTypes"]["2021.05.01"] = {}
es["instanceTypes"]["2021.05.01"]["nElements"] = versions_stats[37]
es["instanceTypes"]["2021.05.01"]["mean"] = versions_stats[38]
es["instanceTypes"]["2021.05.01"]["median"] = versions_stats[39]
es["instanceTypes"]["2021.05.01"]["medianLabel"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2021.05.01"]["mode"] = '561008'
es["instanceTypes"]["2021.05.01"]["modeLabel"] = 'dbo:Agent'
es["instanceTypes"]["2021.05.01"]["standardDeviation"] = versions_stats[40]
es["instanceTypes"]["2021.05.01"]["q1"] = versions_stats[42]
es["instanceTypes"]["2021.05.01"]["q1Label"] = 'dbo:Place'
es["instanceTypes"]["2021.05.01"]["q3"] = versions_stats[43]
es["instanceTypes"]["2021.05.01"]["q3Label"] = 'dbo:ArchitecturalStructure'
es["instanceTypes"]["2021.05.01"]["perc10"] = versions_stats[44]
es["instanceTypes"]["2021.05.01"]["perc10Label"] = 'dbo:Agent'
es["instanceTypes"]["2021.05.01"]["perc50"] = versions_stats[48]
es["instanceTypes"]["2021.05.01"]["perc50Label"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2021.05.01"]["perc90"] = versions_stats[52]
es["instanceTypes"]["2021.05.01"]["perc90Label"] = 'dbo:NaturalPlace'
es["instanceTypes"]["2021.05.01"]["perc95"] = versions_stats[53]
es["instanceTypes"]["2021.05.01"]["perc95Label"] = 'dbo:RouteOfTransportation'
es["instanceTypes"]["2021.06.01"] = {}
es["instanceTypes"]["2021.06.01"]["nElements"] = versions_stats[55]
es["instanceTypes"]["2021.06.01"]["mean"] = versions_stats[56]
es["instanceTypes"]["2021.05.01"]["median"] = versions_stats[57]
es["instanceTypes"]["2021.06.01"]["medianLabel"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2021.06.01"]["mode"] = '564230'
es["instanceTypes"]["2021.06.01"]["modeLabel"] = 'dbo:Agent'
es["instanceTypes"]["2021.06.01"]["standardDeviation"] = versions_stats[58]
es["instanceTypes"]["2021.06.01"]["q1"] = versions_stats[60]
es["instanceTypes"]["2021.06.01"]["q1Label"] = 'dbo:Place'
es["instanceTypes"]["2021.06.01"]["q3"] = versions_stats[61]
es["instanceTypes"]["2021.06.01"]["q3Label"] = 'dbo:ArchitecturalStructure'
es["instanceTypes"]["2021.06.01"]["perc10"] = versions_stats[62]
es["instanceTypes"]["2021.06.01"]["perc10Label"] = 'dbo:Agent'
es["instanceTypes"]["2021.06.01"]["perc50"] = versions_stats[66]
es["instanceTypes"]["2021.06.01"]["perc50Label"] = 'dbo:AdministrativeRegion'
es["instanceTypes"]["2021.06.01"]["perc90"] = versions_stats[70]
es["instanceTypes"]["2021.06.01"]["perc90Label"] = 'dbo:NaturalPlace'
es["instanceTypes"]["2021.06.01"]["perc95"] = versions_stats[71]
es["instanceTypes"]["2021.06.01"]["perc95Label"] = 'dbo:Noble'
#uriCounts
es["uriCounts"] = {}
es["uriCounts"]["2016.10.25"] = {}
es["uriCounts"]["2016.10.25"]["nElements"] = es_stats[42]
es["uriCounts"]["2016.10.25"]["mean"] = es_stats[43]
es["uriCounts"]["2016.10.25"]["median"] = es_stats[44]
es["uriCounts"]["2016.10.25"]["medianLabel"] = 'dbpedia-es:Hinduismo'
es["uriCounts"]["2016.10.25"]["mode"] = str(R.top_2016_uriCounts_es['Count'].iloc[0])
es["uriCounts"]["2016.10.25"]["modeLabel"] = 'dbpedia-es:' + R.top_2016_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["2016.10.25"]["standardDeviation"] = es_stats[45]
es["uriCounts"]["2020.10.25"] = {}
es["uriCounts"]["2020.10.25"]["nElements"] = es_stats[82]
es["uriCounts"]["2020.10.25"]["mean"] = es_stats[83]
es["uriCounts"]["2020.10.25"]["median"] = es_stats[84]
es["uriCounts"]["2020.10.25"]["medianLabel"] = 'dbpedia-es:Huiracocha_Inca'
es["uriCounts"]["2020.10.25"]["mode"] = str(R.top_2020_uriCounts_es['Count'].iloc[0])
es["uriCounts"]["2020.10.25"]["modeLabel"] = 'dbpedia-es:' + R.top_2020_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["2020.10.25"]["standardDeviation"] = es_stats[85]
es["uriCounts"]["2021.05.25"] = {}
es["uriCounts"]["2021.05.25"]["nElements"] = es_stats[22]
es["uriCounts"]["2021.05.25"]["mean"] = es_stats[23]
es["uriCounts"]["2021.05.25"]["median"] = es_stats[24]
es["uriCounts"]["2021.05.25"]["medianLabel"] = 'dbpedia-es:III_milenio_a._C.'
es["uriCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_uriCounts_es['Count'].iloc[0])
es["uriCounts"]["2021.05.25"]["modeLabel"] = 'dbpedia-es:' + R.top_2021_05_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["2021.05.25"]["standardDeviation"] = es_stats[25]
es["uriCounts"]["2021.06.25"] = {}
es["uriCounts"]["2021.06.25"]["nElements"] = es_stats[62]
es["uriCounts"]["2021.06.25"]["mean"] = es_stats[63]
es["uriCounts"]["2021.06.25"]["median"] = es_stats[64]
es["uriCounts"]["2021.06.25"]["medianLabel"] = 'dbpedia-es:ITunes_Store'
es["uriCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_uriCounts_es['Count'].iloc[0])
es["uriCounts"]["2021.06.25"]["modeLabel"] = 'dbpedia-es:' + R.top_2021_06_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["2021.06.25"]["standardDeviation"] = es_stats[65]
#pairCounts
es["pairCounts"] = {}
es["pairCounts"]["2016.10.25"] = {}
es["pairCounts"]["2016.10.25"]["nElements"] = es_stats[46]
es["pairCounts"]["2016.10.25"]["mean"] = es_stats[47]
es["pairCounts"]["2016.10.25"]["median"] = es_stats[48]
es["pairCounts"]["2016.10.25"]["medianLabel"] = '[hinduista - dbpedia-es:Hinduismo]'
es["pairCounts"]["2016.10.25"]["mode"] = str(R.top_2016_pairCounts_es['Times linked'].iloc[0])
es["pairCounts"]["2016.10.25"]["modeLabel"] = "[" + R.top_2016_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2016_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["2016.10.25"]["standardDeviation"] = es_stats[49]
es["pairCounts"]["2020.10.25"] = {}
es["pairCounts"]["2020.10.25"]["nElements"] = es_stats[86]
es["pairCounts"]["2020.10.25"]["mean"] = es_stats[87]
es["pairCounts"]["2020.10.25"]["median"] = es_stats[88]
es["pairCounts"]["2020.10.25"]["mode"] = str(R.top_2020_pairCounts_es['Times linked'].iloc[0])
es["pairCounts"]["2020.10.25"]["medianLabel"] = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
es["pairCounts"]["2020.10.25"]["modeLabel"] = "[" + R.top_2020_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2020_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["2020.10.25"]["standardDeviation"] = es_stats[89]
es["pairCounts"]["2021.05.25"] = {}
es["pairCounts"]["2021.05.25"]["nElements"] = es_stats[26]
es["pairCounts"]["2021.05.25"]["mean"] = es_stats[27]
es["pairCounts"]["2021.05.25"]["median"] = es_stats[28]
es["pairCounts"]["2021.05.25"]["medianLabel"] = '[artículo - dbpedia-es:Película_de_culto]'
es["pairCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_pairCounts_es['Times linked'].iloc[0])
es["pairCounts"]["2021.05.25"]["modeLabel"] = "[" + R.top_2021_05_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_05_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["2021.05.25"]["standardDeviation"] = es_stats[29]
es["pairCounts"]["2021.06.25"] = {}
es["pairCounts"]["2021.06.25"]["nElements"] = es_stats[66]
es["pairCounts"]["2021.06.25"]["mean"] = es_stats[67]
es["pairCounts"]["2021.06.25"]["median"] = es_stats[68]
es["pairCounts"]["2021.06.25"]["medianLabel"] = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
es["pairCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_pairCounts_es['Times linked'].iloc[0])
es["pairCounts"]["2021.06.25"]["modeLabel"] = "[" + R.top_2021_06_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_06_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["2021.06.25"]["standardDeviation"] = es_stats[69]
#tokenCounts
es["tokenCounts"] = {}
es["tokenCounts"]["2016.10.25"] = {}
es["tokenCounts"]["2016.10.25"]["nElements"] = es_stats[50]
es["tokenCounts"]["2016.10.25"]["mean"] = es_stats[51]
es["tokenCounts"]["2016.10.25"]["median"] = es_stats[52]
es["tokenCounts"]["2016.10.25"]["medianLabel"] = 'http://es.wikipedia.org/wiki/Imperio_almohade'
es["tokenCounts"]["2016.10.25"]["mode"] = str(R.top_2016_tokenCounts_es['Nº tokens'].iloc[0])
es["tokenCounts"]["2016.10.25"]["modeLabel"] = 'http://es.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["2016.10.25"]["standardDeviation"] = es_stats[52]
es["tokenCounts"]["2020.10.25"] = {}
es["tokenCounts"]["2020.10.25"]["nElements"] = es_stats[90]
es["tokenCounts"]["2020.10.25"]["mean"] = es_stats[91]
es["tokenCounts"]["2020.10.25"]["median"] = es_stats[92]
es["tokenCounts"]["2020.10.25"]["medianLabel"] = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
es["tokenCounts"]["2020.10.25"]["mode"] = str(R.top_2020_tokenCounts_es['Nº tokens'].iloc[0])
es["tokenCounts"]["2020.10.25"]["modeLabel"] = 'http://es.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["2020.10.25"]["standardDeviation"] = es_stats[92]
es["tokenCounts"]["2021.05.25"] = {}
es["tokenCounts"]["2021.05.25"]["nElements"] = es_stats[30]
es["tokenCounts"]["2021.05.25"]["mean"] = es_stats[31]
es["tokenCounts"]["2021.05.25"]["median"] = es_stats[32]
es["tokenCounts"]["2021.05.25"]["medianLabel"] = 'http://es.wikipedia.org/wiki/Impunidad'
es["tokenCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_tokenCounts_es['Nº tokens'].iloc[0])
es["tokenCounts"]["2021.05.25"]["modeLabel"] = 'http://es.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["2021.05.25"]["standardDeviation"] = es_stats[32]
es["tokenCounts"]["2021.06.25"] = {}
es["tokenCounts"]["2021.06.25"]["nElements"] = es_stats[70]
es["tokenCounts"]["2021.06.25"]["mean"] = es_stats[71]
es["tokenCounts"]["2021.06.25"]["median"] = es_stats[72]
es["tokenCounts"]["2021.06.25"]["medianLabel"] = 'http://es.wikipedia.org/wiki/Invierno'
es["tokenCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_tokenCounts_es['Nº tokens'].iloc[0])
es["tokenCounts"]["2021.06.25"]["modeLabel"] = 'http://es.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["2021.06.25"]["standardDeviation"] = es_stats[72]
#sfAndTotalCounts
es["sfAndTotalCounts"] = {}
es["sfAndTotalCounts"]["2016.10.25"] = {}
es["sfAndTotalCounts"]["2016.10.25"]["nElements"] = es_stats[54]
es["sfAndTotalCounts"]["2016.10.25"]["mean"] = es_stats[59]
es["sfAndTotalCounts"]["2016.10.25"]["median"] = es_stats[60]
es["sfAndTotalCounts"]["2016.10.25"]["medianLabel"] ='doris miller'
es["sfAndTotalCounts"]["2016.10.25"]["mode"] = str(R.top_2016_sfAndTotalCounts_es['Times linked'].iloc[0])
es["sfAndTotalCounts"]["2016.10.25"]["modeLabel"] = R.top_2016_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["2016.10.25"]["standardDeviation"] = es_stats[61]
es["sfAndTotalCounts"]["2020.10.25"] = {}
es["sfAndTotalCounts"]["2020.10.25"]["nElements"] = es_stats[94]
es["sfAndTotalCounts"]["2020.10.25"]["mean"] = es_stats[99]
es["sfAndTotalCounts"]["2020.10.25"]["median"] = es_stats[100]
es["sfAndTotalCounts"]["2020.10.25"]["medianLabel"] = 'Ciudad del Vaticano'
es["sfAndTotalCounts"]["2020.10.25"]["mode"] = str(R.top_2020_sfAndTotalCounts_es['Times linked'].iloc[0])
es["sfAndTotalCounts"]["2020.10.25"]["modeLabel"] = R.top_2020_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["2020.10.25"]["standardDeviation"] = es_stats[101]
es["sfAndTotalCounts"]["2021.05.25"] = {}
es["sfAndTotalCounts"]["2021.05.25"]["nElements"] = es_stats[34]
es["sfAndTotalCounts"]["2021.05.25"]["mean"] =es_stats[39]
es["sfAndTotalCounts"]["2021.05.25"]["median"] =es_stats[40]
es["sfAndTotalCounts"]["2021.05.25"]["medianLabel"] = 'pulmonar'
es["sfAndTotalCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_sfAndTotalCounts_es['Times linked'].iloc[0])
es["sfAndTotalCounts"]["2021.05.25"]["modeLabel"] = R.top_2021_05_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["2021.05.25"]["standardDeviation"] = es_stats[41]
es["sfAndTotalCounts"]["2021.06.25"] = {}
es["sfAndTotalCounts"]["2021.06.25"]["nElements"] = es_stats[74]
es["sfAndTotalCounts"]["2021.06.25"]["mean"] = es_stats[79]
es["sfAndTotalCounts"]["2021.06.25"]["median"] = es_stats[80]
es["sfAndTotalCounts"]["2021.06.25"]["medianLabel"] = 'culebrera europea'
es["sfAndTotalCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_sfAndTotalCounts_es['Times linked'].iloc[0])
es["sfAndTotalCounts"]["2021.06.25"]["modeLabel"] = R.top_2021_06_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["2021.06.25"]["standardDeviation"] = es_stats[81]

en= {}
# instanceTypes
en["instanceTypes"] = {}
en["instanceTypes"]["2016.10.01"] = {}
en["instanceTypes"]["2016.10.01"]["nElements"] = versions_stats[73]
en["instanceTypes"]["2016.10.01"]["mean"] = versions_stats[74]
en["instanceTypes"]["2016.10.01"]["median"] = versions_stats[75]
en["instanceTypes"]["2016.10.01"]["medianLabel"] = 'dbo:Work'
en["instanceTypes"]["2016.10.01"]["mode"] = '1529790'
en["instanceTypes"]["2016.10.01"]["modeLabel"] = 'dbo:Agent'
en["instanceTypes"]["2016.10.01"]["standardDeviation"] = versions_stats[76]
en["instanceTypes"]["2016.10.01"]["q1"] = versions_stats[78]
en["instanceTypes"]["2016.10.01"]["q1Label"] = 'dbo:TimePeriod'
en["instanceTypes"]["2016.10.01"]["q3"] = versions_stats[79]
en["instanceTypes"]["2016.10.01"]["q3Label"] = 'dbo:Insect'
en["instanceTypes"]["2016.10.01"]["perc10"] = versions_stats[80]
en["instanceTypes"]["2016.10.01"]["perc10Label"] = 'dbo:Agent'
en["instanceTypes"]["2016.10.01"]["perc50"] = versions_stats[84]
en["instanceTypes"]["2016.10.01"]["perc50Label"] = 'dbo:Work'
en["instanceTypes"]["2016.10.01"]["perc90"] = versions_stats[88]
en["instanceTypes"]["2016.10.01"]["perc90Label"] = 'dbo:Scientist'
en["instanceTypes"]["2016.10.01"]["perc95"] = versions_stats[85]
en["instanceTypes"]["2016.10.01"]["perc95Label"] = 'dbo:Tournament'
en["instanceTypes"]["2020.10.01"] = {}
en["instanceTypes"]["2020.10.01"]["nElements"] = versions_stats[91]
en["instanceTypes"]["2020.10.01"]["mean"] = versions_stats[92]
en["instanceTypes"]["2020.10.01"]["median"] = versions_stats[93]
en["instanceTypes"]["2020.10.01"]["medianLabel"] = 'dbo:Work'
en["instanceTypes"]["2020.10.01"]["mode"] = '1968077'
en["instanceTypes"]["2020.10.01"]["modeLabel"] = 'dbo:Agent'
en["instanceTypes"]["2020.10.01"]["standardDeviation"] = versions_stats[94]
en["instanceTypes"]["2020.10.01"]["q1"] = versions_stats[96]
en["instanceTypes"]["2020.10.01"]["q1Label"] = 'dbo:Person'
en["instanceTypes"]["2020.10.01"]["q3"] = versions_stats[97]
en["instanceTypes"]["2020.10.01"]["q3Label"] = 'dbo:SoccerPlayer'
en["instanceTypes"]["2020.10.01"]["perc10"] = versions_stats[98]
en["instanceTypes"]["2020.10.01"]["perc10Label"] = 'dbo:Agent'
en["instanceTypes"]["2020.10.01"]["perc50"] = versions_stats[102]
en["instanceTypes"]["2020.10.01"]["perc50Label"] = 'dbo:Work'
en["instanceTypes"]["2020.10.01"]["perc90"] = versions_stats[106]
en["instanceTypes"]["2020.10.01"]["perc90Label"] = 'dbo:Broadcaster'
en["instanceTypes"]["2020.10.01"]["perc95"] = versions_stats[107]
en["instanceTypes"]["2020.10.01"]["perc95Label"] = 'dbo:Cyclist'
en["instanceTypes"]["2021.05.01"] = {}
en["instanceTypes"]["2021.05.01"]["nElements"] = versions_stats[109]
en["instanceTypes"]["2021.05.01"]["mean"] = versions_stats[110]
en["instanceTypes"]["2021.05.01"]["median"] = versions_stats[111]
en["instanceTypes"]["2021.05.01"]["medianLabel"] = 'dbo:Work'
en["instanceTypes"]["2021.05.01"]["mode"] = '2037245'
en["instanceTypes"]["2021.05.01"]["modeLabel"] = 'dbo:Agent'
en["instanceTypes"]["2021.05.01"]["standardDeviation"] = versions_stats[112]
en["instanceTypes"]["2021.05.01"]["q1"] = versions_stats[114]
en["instanceTypes"]["2021.05.01"]["q1Label"] = 'dbo:Person'
en["instanceTypes"]["2021.05.01"]["q3"] = versions_stats[115]
en["instanceTypes"]["2021.05.01"]["q3Label"] = 'dbo:SoccerPlayer'
en["instanceTypes"]["2021.05.01"]["perc10"] = versions_stats[116]
en["instanceTypes"]["2021.05.01"]["perc10Label"] = 'dbo:Agent'
en["instanceTypes"]["2021.05.01"]["perc50"] = versions_stats[120]
en["instanceTypes"]["2021.05.01"]["perc50Label"] = 'dbo:Work'
en["instanceTypes"]["2021.05.01"]["perc90"] = versions_stats[124]
en["instanceTypes"]["2021.05.01"]["perc90Label"] = 'dbo:Broadcaster'
en["instanceTypes"]["2021.05.01"]["perc95"] = versions_stats[125]
en["instanceTypes"]["2021.05.01"]["perc95Label"] = 'dbo:Sales'
en["instanceTypes"]["2021.06.01"] = {}
en["instanceTypes"]["2021.06.01"]["nElements"] = versions_stats[127]
en["instanceTypes"]["2021.06.01"]["mean"] = versions_stats[128]
en["instanceTypes"]["2021.06.01"]["median"] = versions_stats[129]
en["instanceTypes"]["2021.06.01"]["medianLabel"] = 'dbo:AdministrativeRegion'
en["instanceTypes"]["2021.06.01"]["mode"] = '2045255'
en["instanceTypes"]["2021.06.01"]["modeLabel"] = 'dbo:Agent'
en["instanceTypes"]["2021.06.01"]["standardDeviation"] = versions_stats[130]
en["instanceTypes"]["2021.06.01"]["q1"] = versions_stats[132]
en["instanceTypes"]["2021.06.01"]["q1Label"] = 'dbo:Person'
en["instanceTypes"]["2021.06.01"]["q3"] = versions_stats[133]
en["instanceTypes"]["2021.06.01"]["q3Label"] = 'dbo:SoccerPlayer'
en["instanceTypes"]["2021.06.01"]["perc10"] = versions_stats[134]
en["instanceTypes"]["2021.06.01"]["perc10Label"] = 'dbo:Agent'
en["instanceTypes"]["2021.06.01"]["perc50"] = versions_stats[138]
en["instanceTypes"]["2021.06.01"]["perc50Label"] = 'dbo:AdministrativeRegion'
en["instanceTypes"]["2021.06.01"]["perc90"] = versions_stats[142]
en["instanceTypes"]["2021.06.01"]["perc90Label"] = 'dbo:Broadcaster'
en["instanceTypes"]["2021.06.01"]["perc95"] = versions_stats[143]
en["instanceTypes"]["2021.06.01"]["perc95Label"] = 'dbo:Sales'
#uriCounts
en["uriCounts"] = {}
en["uriCounts"]["2016.10.25"] = {}
en["uriCounts"]["2016.10.25"]["nElements"] = en_stats[42]
en["uriCounts"]["2016.10.25"]["mean"] = en_stats[43]
en["uriCounts"]["2016.10.25"]["median"] = en_stats[44]
en["uriCounts"]["2016.10.25"]["medianLabel"] = 'dbr:Latvian_constitutional_referendum,_2008'
en["uriCounts"]["2016.10.25"]["mode"] = str(R.top_2016_uriCounts_en['Count'].iloc[0])
en["uriCounts"]["2016.10.25"]["modeLabel"] = 'dbr:' + R.top_2016_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["2016.10.25"]["standardDeviation"] = en_stats[45]
en["uriCounts"]["2020.10.25"] = {}
en["uriCounts"]["2020.10.25"]["nElements"] = en_stats[82]
en["uriCounts"]["2020.10.25"]["mean"] = en_stats[83]
en["uriCounts"]["2020.10.25"]["median"] = en_stats[84]
en["uriCounts"]["2020.10.25"]["medianLabel"] = 'dbr:Lamar_University'
en["uriCounts"]["2020.10.25"]["mode"] = str(R.top_2020_uriCounts_en['Count'].iloc[0])
en["uriCounts"]["2020.10.25"]["modeLabel"] = 'dbr:' + R.top_2020_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["2020.10.25"]["standardDeviation"] = en_stats[85]
en["uriCounts"]["2021.05.25"] = {}
en["uriCounts"]["2021.05.25"]["nElements"] = en_stats[22]
en["uriCounts"]["2021.05.25"]["mean"] = en_stats[23]
en["uriCounts"]["2021.05.25"]["median"] = en_stats[24]
en["uriCounts"]["2021.05.25"]["medianLabel"] = 'dbr:Kyrgyzstan_national_football_team'
en["uriCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_uriCounts_en['Count'].iloc[0])
en["uriCounts"]["2021.05.25"]["modeLabel"] = 'dbr:' + R.top_2021_05_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["2021.05.25"]["standardDeviation"] = en_stats[25]
en["uriCounts"]["2021.06.25"] = {}
en["uriCounts"]["2021.06.25"]["nElements"] = en_stats[62]
en["uriCounts"]["2021.06.25"]["mean"] = en_stats[63]
en["uriCounts"]["2021.06.25"]["median"] = en_stats[64]
en["uriCounts"]["2021.06.25"]["medianLabel"] = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
en["uriCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_uriCounts_en['Count'].iloc[0])
en["uriCounts"]["2021.06.25"]["modeLabel"] = 'dbr:' + R.top_2021_06_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["2021.06.25"]["standardDeviation"] = en_stats[65]
#pairCounts
en["pairCounts"] = {}
en["pairCounts"]["2016.10.25"] = {}
en["pairCounts"]["2016.10.25"]["nElements"] = en_stats[46]
en["pairCounts"]["2016.10.25"]["mean"] = en_stats[47]
en["pairCounts"]["2016.10.25"]["median"] = en_stats[48]
en["pairCounts"]["2016.10.25"]["medianLabel"] = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
en["pairCounts"]["2016.10.25"]["mode"] = str(R.top_2016_pairCounts_en['Times linked'].iloc[0])
en["pairCounts"]["2016.10.25"]["modeLabel"] = "[" + R.top_2016_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2016_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["2016.10.25"]["standardDeviation"] = en_stats[49]
en["pairCounts"]["2020.10.25"] = {}
en["pairCounts"]["2020.10.25"]["nElements"] = en_stats[86]
en["pairCounts"]["2020.10.25"]["mean"] = en_stats[87]
en["pairCounts"]["2020.10.25"]["median"] = en_stats[88]
en["pairCounts"]["2020.10.25"]["medianLabel"] = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
en["pairCounts"]["2020.10.25"]["mode"] = str(R.top_2020_pairCounts_en['Times linked'].iloc[0])
en["pairCounts"]["2020.10.25"]["modeLabel"] = "[" + R.top_2020_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2020_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["2020.10.25"]["standardDeviation"] = en_stats[89]
en["pairCounts"]["2021.05.25"] = {}
en["pairCounts"]["2021.05.25"]["nElements"] = en_stats[26]
en["pairCounts"]["2021.05.25"]["mean"] = en_stats[27]
en["pairCounts"]["2021.05.25"]["median"] = en_stats[28]
en["pairCounts"]["2021.05.25"]["medianLabel"] = '[Wallenpaupack - dbr:Lake_Wallenpaupack]'
en["pairCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_pairCounts_en['Times linked'].iloc[0])
en["pairCounts"]["2021.05.25"]["modeLabel"] = "[" + R.top_2021_05_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_05_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["2021.05.25"]["standardDeviation"] = en_stats[29]
en["pairCounts"]["2021.06.25"] = {}
en["pairCounts"]["2021.06.25"]["nElements"] = en_stats[66]
en["pairCounts"]["2021.06.25"]["mean"] = en_stats[67]
en["pairCounts"]["2021.06.25"]["median"] = en_stats[68]
en["pairCounts"]["2021.06.25"]["medianLabel"] = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
en["pairCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_pairCounts_en['Times linked'].iloc[0])
en["pairCounts"]["2021.06.25"]["modeLabel"] = "[" + R.top_2021_06_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_06_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["2021.06.25"]["standardDeviation"] = en_stats[69]
#tokenCounts
en["tokenCounts"] = {}
en["tokenCounts"]["2016.10.25"] = {}
en["tokenCounts"]["2016.10.25"]["nElements"] = en_stats[50]
en["tokenCounts"]["2016.10.25"]["mean"] = en_stats[51]
en["tokenCounts"]["2016.10.25"]["median"] = en_stats[52]
en["tokenCounts"]["2016.10.25"]["medianLabel"] = 'http://en.wikipedia.org/wiki/Kushti'
en["tokenCounts"]["2016.10.25"]["mode"] = str(R.top_2016_tokenCounts_en['Nº tokens'].iloc[0])
en["tokenCounts"]["2016.10.25"]["modeLabel"] = 'http://en.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["2016.10.25"]["standardDeviation"] = en_stats[52]
en["tokenCounts"]["2020.10.25"] = {}
en["tokenCounts"]["2020.10.25"]["nElements"] = en_stats[90]
en["tokenCounts"]["2020.10.25"]["mean"] = en_stats[91]
en["tokenCounts"]["2020.10.25"]["median"] = en_stats[92]
en["tokenCounts"]["2020.10.25"]["medianLabel"] = 'http://en.wikipedia.org/wiki/Klondike_Open'
en["tokenCounts"]["2020.10.25"]["mode"] = str(R.top_2020_tokenCounts_en['Nº tokens'].iloc[0])
en["tokenCounts"]["2020.10.25"]["modeLabel"] = 'http://en.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["2020.10.25"]["standardDeviation"] = en_stats[92]
en["tokenCounts"]["2021.05.25"] = {}
en["tokenCounts"]["2021.05.25"]["nElements"] = en_stats[30]
en["tokenCounts"]["2021.05.25"]["mean"] = en_stats[31]
en["tokenCounts"]["2021.05.25"]["median"] = en_stats[32]
en["tokenCounts"]["2021.05.25"]["medianLabel"] = 'http://en.wikipedia.org/wiki/Klas_Lund'
en["tokenCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_tokenCounts_en['Nº tokens'].iloc[0])
en["tokenCounts"]["2021.05.25"]["modeLabel"] = 'http://en.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["2021.05.25"]["standardDeviation"] = en_stats[32]
en["tokenCounts"]["2021.06.25"] = {}
en["tokenCounts"]["2021.06.25"]["nElements"] = en_stats[70]
en["tokenCounts"]["2021.06.25"]["mean"] = en_stats[71]
en["tokenCounts"]["2021.06.25"]["median"] = en_stats[72]
en["tokenCounts"]["2021.06.25"]["medianLabel"] = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
en["tokenCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_tokenCounts_en['Nº tokens'].iloc[0])
en["tokenCounts"]["2021.06.25"]["modeLabel"] = 'http://en.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["2021.06.25"]["standardDeviation"] = en_stats[72]
#sfAndTotalCounts
en["sfAndTotalCounts"] = {}
en["sfAndTotalCounts"]["2016.10.25"] = {}
en["sfAndTotalCounts"]["2016.10.25"]["nElements"] = en_stats[54]
en["sfAndTotalCounts"]["2016.10.25"]["mean"] = en_stats[59]
en["sfAndTotalCounts"]["2016.10.25"]["median"] = en_stats[60]
en["sfAndTotalCounts"]["2016.10.25"]["medianLabel"] = 'Deep Cove'
en["sfAndTotalCounts"]["2016.10.25"]["mode"] = str(R.top_2016_sfAndTotalCounts_en['Times linked'].iloc[0])
en["sfAndTotalCounts"]["2016.10.25"]["modeLabel"] = R.top_2016_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["2016.10.25"]["standardDeviation"] = en_stats[61]
en["sfAndTotalCounts"]["2020.10.25"] = {}
en["sfAndTotalCounts"]["2020.10.25"]["nElements"] = en_stats[94]
en["sfAndTotalCounts"]["2020.10.25"]["mean"] = en_stats[99]
en["sfAndTotalCounts"]["2020.10.25"]["median"] = en_stats[100]
en["sfAndTotalCounts"]["2020.10.25"]["medianLabel"] = 'The Herald'
en["sfAndTotalCounts"]["2020.10.25"]["mode"] = str(R.top_2020_sfAndTotalCounts_en['Times linked'].iloc[0])
en["sfAndTotalCounts"]["2020.10.25"]["modeLabel"] = R.top_2020_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["2020.10.25"]["standardDeviation"] = en_stats[101]
en["sfAndTotalCounts"]["2021.05.25"] = {}
en["sfAndTotalCounts"]["2021.05.25"]["nElements"] = en_stats[34]
en["sfAndTotalCounts"]["2021.05.25"]["mean"] =en_stats[39]
en["sfAndTotalCounts"]["2021.05.25"]["median"] =en_stats[40]
en["sfAndTotalCounts"]["2021.05.25"]["medianLabel"] = 'DC Comics'
en["sfAndTotalCounts"]["2021.05.25"]["mode"] = str(R.top_2021_05_sfAndTotalCounts_en['Times linked'].iloc[0])
en["sfAndTotalCounts"]["2021.05.25"]["modeLabel"] = R.top_2021_05_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["2021.05.25"]["standardDeviation"] = en_stats[41]
en["sfAndTotalCounts"]["2021.06.25"] = {}
en["sfAndTotalCounts"]["2021.06.25"]["nElements"] = en_stats[74]
en["sfAndTotalCounts"]["2021.06.25"]["mean"] = en_stats[79]
en["sfAndTotalCounts"]["2021.06.25"]["median"] = en_stats[80]
en["sfAndTotalCounts"]["2021.06.25"]["medianLabel"] = 'Cyropaedia'
en["sfAndTotalCounts"]["2021.06.25"]["mode"] = str(R.top_2021_06_sfAndTotalCounts_en['Times linked'].iloc[0])
en["sfAndTotalCounts"]["2021.06.25"]["modeLabel"] = R.top_2021_06_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["2021.06.25"]["standardDeviation"] = en_stats[81]

es_dashboard_stats = json.dumps(es,indent=4)
en_dashboard_stats = json.dumps(en,indent=4)
es_json = open(resources_directory + "es_stats.json", "w")
es_json.write(es_dashboard_stats)
es_json.close()
en_json = open(resources_directory + "en_stats.json", "w")
en_json.write(en_dashboard_stats)
en_json.close()

