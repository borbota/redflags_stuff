#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import csv
import os

sys.stdout = open('log_organization_data.txt', 'w')

#provide path to jsons
mypath = ""
for file in os.listdir(mypath):
	if file.endswith(".json"):
		json_data = open(file).read()
		data = json.loads(json_data)
		data2 = data["result"]
		data3 = data2["wins"]
		with open("organization_data.csv", "a") as outputfile:
			for wins in data3:
				for i in wins["winners"]:
					if wins["title"] is None:
						print "no wins data, " + file
					else:
						wins_id = str(wins["id"])
						if wins_id[-5:] == "-2016" or wins_id[-5:] == "-2017":
							for j in wins["flags"]:
								org_id = i["id"].encode("utf-8")
								org_name = i["name"].encode("utf-8")
								total = str(wins["total"])
								currency = wins["totalCurr"].encode("utf-8")
								title = wins["title"].replace('\n', ' ').encode("utf-8")
								flags = str(wins["flagCount"])
								date = str(wins["date"])
								information = j["information"].replace('\n', ' ').encode("utf-8")
								outputfile.write(wins_id + "\t" + org_id + "\t" + org_name\
									 + "\t" + total + "\t" + currency + "\t" + title + "\t" + \
									 flags + "\t" + date + "\t" +  information + "\n")			
						else:
							print "regebbi," + file
#data.columns = ["wins_id", "org_id", "org_name", "total", "currency", "title", "flag_count", "date", "information"]
sys.stdout.close()