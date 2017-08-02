#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


pagination_count = 1

# provide token
token = ""
url = "http://api.redflags.eu/organizations?count=50&page=1&access_token=" + token
while url is not None:
	r = requests.get(url)
	data = json.loads(r.text)
	data2 = data['links']
	json_str = json.dumps(data,indent=2)	
	with open('organizations_%d.json' %pagination_count, 'w') as f:
		f.write(json_str)
	pagination_count +=1
	print "downloading" + ": "+str(url)
	url = data2["next"]	