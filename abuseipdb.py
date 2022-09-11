import requests
import json
import sys

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/blacklist'

querystring = {
    'limit':'500000'
}

headers = {
    'Accept': 'text/plain',
    'Key': 'YOUR-ABUSEIPDB-API-KEY'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
with open('abuseipdb.txt', 'w') as f:
	print (response.text, file=f)
