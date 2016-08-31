


import serial



import urllib, json
import requests

url = "http://192.168.240.1/arduino/data/1"
arduino = serial.Serial('/dev/cu.usbmodem1411',9600)
data = data = {}
while True:
	#response = urllib.urlopen(url)
    rawString = arduino.readline()
    rawString.split('#')
    volume = rawString[1]
    preassure = rawString[3]
	#data = json.loads(response.read())
    data['preassure'] = preassure
	data['level'] = '12'
	data['volume'] = volume
	#requests.put("https://tfgsrkapi.firebaseio.com/tfgsrkapi/datos/-KLSVTeRzs2lreouvMPE/datos.json", json.dumps(data))
	requests.get('http://192.168.1.102:8000/app/measureadd/', params= json.dumps(data))

print(volume)

arduino.close()