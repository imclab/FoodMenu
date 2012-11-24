#! /usr/bin/python

import json, requests

apiKey = open('apiKey.txt', 'r')
key = apiKey.readline()
apiKey.close()

service = 'FoodMenu'
# output = 'json'
# callback = 'None'
request = 'http://api.uwaterloo.ca/public/v1/'

def getMenu():
	url = request + '?' + 'key=' + key + '&' + 'service=' + service
	result = requests.get(url).text
	return result

menu = getMenu()
jsonResponseFile = open('response.txt', 'w')
jsonResponseFile.write(menu)
jsonResponseFile.close()
