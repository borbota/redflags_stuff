#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

organizations_file = open("organizations_list.csv","r")

pagination_count = 1
website = "http://api.redflags.eu/organization?id="
# provided token
access_token = ""
first = "/organization?id="

for row in organizations_file:
	org_id = row.split("\t")[0]
	url = website + str(org_id) + access_token
	r = requests.get(url)
	print "downloading: " + url
	data = json.loads(r.text)
	json_str = json.dumps(data, indent = 2)
	with open('organization_data_%s.json' %org_id, 'w') as f:
		f.write(json_str)

organizations_file.close()