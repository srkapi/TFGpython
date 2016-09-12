import serial
import json
import requests
arduino = serial.Serial('/dev/cu.usbmodem1411', 9600)
data = {}


while True:
    rawString = arduino.readline()
    print(rawString[0])
    dataStr = rawString.split("#")
    volume = dataStr[1]
    preassure = dataStr[3]
    data['preassure'] = preassure
    data['level'] = '12'
    data['volume'] = volume
    print(json.dumps(data))
    requests.put("https://tfgsrkapi.firebaseio.com/tfgsrkapi/datos/-KLSVTeRzs2lreouvMPE/datos.json", json.dumps(data))
    requests.get('http://127.0.0.1:8000/app/measureadd/', params=data)


arduino.close()
