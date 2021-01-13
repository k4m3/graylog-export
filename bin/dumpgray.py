import splunk.Intersplunk
import base64
import requests
import time
import sys
import os
import json
from time import gmtime, strftime
from sys import exit


__author__      = "Kelvem Sousa - k4m3"
__copyright__   = "Copyright 2021"


def graylog():
	generes = ['log']
	TOKEN = ""


	SERVER = "http://graylog-server:9000"
	QUERY = sys.argv[2]
	RANGE = sys.argv[1]


	payload = {'query': QUERY, 'range': RANGE, 'limit': '9999', 'sort': 'timestamp:desc', 'pretty': 'true'}
	url = SERVER + "/api/search/universal/relative"
	headers = {'Authorization': 'Basic '+TOKEN, 'Accept': 'application/json', 'content-type': 'application/json', }

	r = requests.get(url, params=payload, headers=headers)
	log = r.json()

	c = 0
	qtd = len(log['messages'])

	while c < qtd:
		a = generes.append(log['messages'][c]['message']['message'])
		c = c + 1

	for i in generes:
		print(i)

resultgray = graylog()

splunk.Intersplunk.outputResults(resultgray)
