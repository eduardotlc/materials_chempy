import unittest
import requests
import json
import csv
import os
keyword = 'Plasmonic'
date_int = 2016
springer_keyword = "?q=("+ "%22" + keyword.replace(" ", "%20") + "%22" + "%20AND%20year:" + str(date_int) + ")"
springer_api_key = "56580f5684a4934af904f1edf8f07706"

base_url_springer = 'http://api.springer.com/metadata/json'

# Building the Springer Metadata API parameters dictionary
url_params_springer = {}
url_params_springer["api_key"] = springer_api_key
url_params_springer["p"] = 200   #10 results will be returned
d_springer = requests.get(base_url_springer + springer_keyword
                            ,params=url_params_springer).json()
print(len(d_springer))
#for Gitbash
print("--------Result of Springer Metadata API-----------")
#print pretty(d_springer)[:2000]
# cache the data from Scopus and collected
fr_springer = open("springer_abstract.txt","w")
fr_springer.write(json.dumps(d_springer))
fr_springer.close()