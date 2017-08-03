#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import csv
import os

# provide paths
mypath_notices = ""
mypath_winners = ""
mypath_flags = ""
mypath_for_notices_jsons = ""
with open(mypath_notices, 'w') as notices,\
			 open(mypath_winners, 'w') as winners,\
			 open(mypath_flags, 'w') as flagsdata:
	for file in os.listdir(mypath_for_notices_jsons):
		if file.endswith(".json"):
			print "processing: " + str(file)
			my_win_id = os.path.splitext(file)[0][23:]
			json_data = open(file).read()
			data = json.loads(json_data)
			data2 = data["result"]
			data_family = data2["familyMembers"]
			awards = data2["awards"]
			for each in range(len(data_family)):
				if data_family[each]["id"] == my_win_id:
					typeid = data_family[each]["typeId"].encode("utf-8")
					if typeid == "TD-7":
						title = data_family[each]["title"].replace("\n", " ").encode("utf-8")
						total = str(data_family[each]["total"])
						contractingOrgName = data_family[each]["contractingOrgName"].encode("utf-8")
						contractingOrgId = data_family[each]["contractingOrgId"].encode("utf-8")
						flagcount = str(data_family[each]["flagCount"])
						flagpackage = data_family[each]["flags"]
						aggregate_content = my_win_id + "\t" + contractingOrgName + "\t" + \
						contractingOrgId + "\t" + typeid + "\t" + title + "\t" + flagcount \
			 			+ "\t" + total
						notices.write(aggregate_content + "\n")
						#notices.columns = ["wins_id_notices", "contractingOrgName", "contractingOrgId", "typeID", "title", "flagcount", "total_amount"]
						for flags in range(len(flagpackage)):
							information = flagpackage[flags]["id"].encode("utf-8")
							flags_content = my_win_id + "\t" + information
							flagsdata.write(flags_content + '\n')
							#flags.columns = ["wins_id_flags", "information"]
			for award in range(len(awards)):
				if awards[award]["noticeId"] == my_win_id:
					if awards[award]["winner_name"] != None:
						winner = awards[award]["winner_name"].encode("utf-8")
						total_final_value = str(awards[award]["totalFinalValue"])
						winners_contet = my_win_id + "\t" + winner + "\t" + total_final_value
						winners.write(winners_contet + "\n")
						#winners.columns = ["wins_id_winners", "winner", "winner_final_value"]