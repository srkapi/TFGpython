import urllib, json
import requests
url = "http://192.168.240.1/arduino/data/1"

for x in range(5):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	measure = data['measure']
	level = data['level']
	volume = data['volume']

	requests.get('http://192.168.1.100:8000/app/measureadd/', params=data)
requests.put("https://tfgsrkapi.firebaseio.com/tfgsrkapi/datos/-KLSVTeRzs2lreouvMPE/datos.json", json.dumps(data))

print measure
print level
print volume

