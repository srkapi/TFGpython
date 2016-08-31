import serial
import json
import requests
arduino = serial.Serial('/dev/cu.usbmodem1411', 9600)
data = {}


while True:
    rawString = arduino.readline()
    print(rawString[0])
    dataStr =  rawString.split("#")
    volume = dataStr[1]
    preassure = dataStr[3]
    data['preassure'] = preassure
    data['level'] = 'miguel comunista'
    data['volume'] = volume
    print(json.dumps(data))
    #requests.put("https://tfgsrkapi.firebaseio.com/tfgsrkapi/datos/-KLSVTeRzs2lreouvMPE/datos.json", json.dumps(data))
	requests.get('http://192.168.1.102:8000/app/measureadd/', params= json.dumps(data))

arduino.close()
