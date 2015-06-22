# data.cityofchicago.org

import json

with open("test.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)



# import from external source / api

import urllib

url = 'https://data.cityofchicago.org/resource/i6bp-fvbx.json'
result = json.load(urllib.urlopen(url))
print result[0]



