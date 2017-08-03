#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

# file with winsids
winsids = open("win_id_list.csv","r")

website = "http://api.redflags.eu/notice?id="

# provide token
access_token = ""

for row in winsids:
	win_id = row.split(",")[0].replace('\n','')
	url = website + str(win_id) + access_token
	r = requests.get(url)
	print "downloading: " + url	
	data = json.loads(r.text)
	json_str = json.dumps(data, indent = 2)
	with open('notices_data_%s.json' %win_id, 'w') as f:
		f.write(json_str)

winsids.close()