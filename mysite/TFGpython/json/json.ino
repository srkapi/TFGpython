/*
  Arduino Yún Bridge example

  This example for the Yún101/YunShield/Yún shows how
  to use the Bridge library to access the digital and
  analog pins on the board through REST calls.
  It demonstrates how you can create your own API when
  using REST style calls through the browser.

  Possible commands created in this shetch:

  "/arduino/digital/13"     -> digitalRead(13)
  "/arduino/digital/13/1"   -> digitalWrite(13, HIGH)
  "/arduino/analog/2/123"   -> analogWrite(2, 123)
  "/arduino/analog/2"       -> analogRead(2)
  "/arduino/mode/13/input"  -> pinMode(13, INPUT)
  "/arduino/mode/13/output" -> pinMode(13, OUTPUT)

  This example code is part of the public domain

  http://www.arduino.cc/en/Tutorial/Bridge

*/

#include <Bridge.h>
#include <BridgeServer.h>
#include <BridgeClient.h>
#include <Process.h>
// Listen to the default port 5555, the Yún webserver
// will forward there all the HTTP requests you send
BridgeServer server;


volatile int NbTopsFan;
int Calc;
int hallsensor = 2;
int AnalogPin = 0;



void setup() {
  pinMode(hallsensor, INPUT);
  pinMode(AnalogPin, INPUT);
  Serial.begin(9600);
  delay(4000);
  while(!Serial);

  Serial.print("Initializing the bridge...");

  Serial.println("Done");
  attachInterrupt(digitalPinToInterrupt(2), rpm, RISING);


  // Listen for incoming connection only from localhost
  // (no one from the external network could connect)
  server.listenOnLocalhost();
  server.begin();
}

void loop() {
  //volumenSensor();
  preasureSensor();
  // Get clients coming from server
  //BridgeClient client = server.accept();

  // There is a new client?
  // if (client) {
  // Process request
  //process(client);

  // Close connection and free resources.
  // client.stop();
  //}

  delay(50); // Poll every 50ms
}

void process(BridgeClient client) {
  // read the command
  String command = client.readStringUntil('/');

  // is "digital" command?
  if (command == "data") {
    loadData(client);
  }

}

void loadData(BridgeClient client) {
  float measure = random(10, 20);
  float level = random(10, 20);
  float volume = volumenSensor();
  Process p;

  //p.runShellCommand("curl -k -X PUT https://tfgsrkapi.firebaseapp.com/data -d ' { \"measure:"  +String(measure)+", level:"+ String(level) + ", volume:"+String(volume)+"}'");
  //while(p.running());


  // Send feedback to client
  client.print(F("{ \"measure\": "));
  client.print(measure);
  client.print(F(","));
  client.print(F(" \"level\": "));
  client.print(level);
  client.print(F(","));
  client.print("\"volume\": ");
  client.print(volume);
  client.print(F("}"));

}

float volumenSensor() {
  NbTopsFan = 0;
  sei();
  delay (1000);
  cli();
  Calc = (NbTopsFan * 60 / 5);
  Serial.print (Calc *10, DEC);
  Serial.print (" Litros/hor\r\n");
}

void preasureSensor(){
  int ResRead = analogRead(AnalogPin); // La Resistencia es igual a la lectura del sensor (Analog 0)
  Serial.print("Lectura Analogica = ");
  Serial.println(ResRead);
}

void rpm (){
  NbTopsFan++;
}


