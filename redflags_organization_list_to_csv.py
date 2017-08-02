#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import csv
import os

# define path to files
mypath = ""

for file in os.listdir(mypath):
    if file.endswith(".json"):
    	json_data = open(file).read()
    	data = json.loads(json_data)
    	data2 = data["result"]
    	with open('organizations_2017.csv','a') as outputfile:
    		for i in data2:
				outputfile.write(i['id'].encode('utf-8') + '\t' + i['name'].encode('utf-8') + '\t' + str(i['wins'])+ '\t' + str(i['calls']) + '\n')