import urllib2
import json

response = urllib2.urlopen('http://localhost:8080/api/json')
data = json.load(response)
print data