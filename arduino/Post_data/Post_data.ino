/*
  Simple POST client for ArduinoHttpClient library
  Connects to server once every five seconds, sends a POST request
  and a request body

  created 14 Feb 2016
  modified 22 Jan 2019
  by Tom Igoe
  
  this example is in the public domain
 */
#include <ArduinoJson.h>
#include <ArduinoHttpClient.h>
#include <WiFiNINA.h>
#include "AirSensor.h"
#include "arduino_secrets.h"
#include "PressionSensor.h"
#include "humidityTempSensor.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
/////// Wifi Settings ///////
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

char serverAddress[] = "10.0.0.7";  // server address
int port = 7657;

WiFiClient wifi;
HttpClient client = HttpClient(wifi, serverAddress, port);
int status = WL_IDLE_STATUS;
AirSensor airsensor(A0);
PressionSensor pressionsensor;
Humidity_TempSensor humidity_tempsensor;
void setup() {
  Serial.begin(9600);
  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);                   // print the network name (SSID);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);
  }

  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
  //AirSensor
  airsensor.inits();
  pressionsensor.inits();
  humidity_tempsensor.inits();
}

void loop() {
  status = WiFi.status();
  while ( status != WL_CONNECTED) {
    WiFi.end();
    WiFi.disconnect();
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);                   // print the network name (SSID);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);
    delay(5000);
  }
  //sensor debug
  airsensor.debug();
  pressionsensor.debug();
  //
  Serial.println("making POST request");
  // Create Json
  StaticJsonDocument<200> doc;
  doc["temperature"]=humidity_tempsensor.get_temp_value();
  doc["air_quality_value"]=airsensor.getqualityair_value();
  doc["air_quality"]=airsensor.getqualityair();
  doc["pressure"]=pressionsensor.getpression_value();
  doc["humidity"]=humidity_tempsensor.get_humidity_value();
  // 
  serializeJsonPretty(doc, Serial);//Write Json in serial
  //Post data 
  String contentType = "application/json";
  String postData;
  serializeJson(doc, postData);
  client.post("/add_data/", contentType, postData);
  //
  // read the status code and body of the response
  int statusCode = client.responseStatusCode();
  String response = client.responseBody();

  Serial.print("Status code: ");
  Serial.println(statusCode);
  Serial.print("Response: ");
  Serial.println(response);

  Serial.println("Wait thirty seconds");
  delay(30000);
}
