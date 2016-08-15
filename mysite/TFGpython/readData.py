import urllib, json
import requests
url = "http://192.168.240.1/arduino/data/1"

for x in range(5):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	pressure = data['pressure']
	level = data['level']
	volume = data['volume']
	requests.put("https://tfgsrkapi.firebaseio.com/tfgsrkapi/datos/-KLSVTeRzs2lreouvMPE/datos.json", json.dumps(data))
	requests.get('http://192.168.1.102:8000/app/measureadd/', params=data)


print measure
print level
print volume

