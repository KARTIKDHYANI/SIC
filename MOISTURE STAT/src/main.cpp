#include <Arduino.h>
int calcMoist();
/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-client-server-wi-fi/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/
int _moisture,sensor_analog;
char moisture[20];
const int sensor_pin = A0;
// Import required libraries
#include "WiFi.h"
#include "ESPAsyncWebServer.h"
int status=0;
// Set your access point network credentials
const char* ssid = "ESP32-Access-Point";
const char* password = "123456789";

/*#include <SPI.h>
#define BME_SCK 18
#define BME_MISO 19
#define BME_MOSI 23
#define BME_CS 5*/

 // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);


void setup(){
    pinMode(2, OUTPUT);

    
  // Serial port for debugging purposes
  Serial.begin(115200);
  Serial.println();
  
  // Setting the ESP as an access point
  Serial.print("Setting AP (Access Point)…");
  // Remove the password parameter, if you want the AP (Access Point) to be open
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  server.on("/temperature", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", "aquib");
  });
  server.on("/humidity", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", "babu");
  });
  server.on("/moisture", HTTP_GET, [](AsyncWebServerRequest *request){
    String moistureValue = String(calcMoist());
    AsyncWebServerResponse *response = request->beginResponse(200, "text/plain", moistureValue);
    response->addHeader("Access-Control-Allow-Origin", "*"); // Allow requests from any origin
    request->send(response);
});

  
  server.on("/status", HTTP_POST, [](AsyncWebServerRequest *request){
    Serial.println("Received POST request to /status");
      String value = request->getParam(0)->value();
      status = value.toInt();
      Serial.println(" data recieved");
      request->send(200, "text/plain", "Status updated");
    
  });
  server.on("/get-status", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", String(status).c_str());
  });

  // Start server
  server.begin();
}
int calcMoist()
{
  
sensor_analog = analogRead(sensor_pin);
  

  _moisture = ( 100 - ( (sensor_analog/4095.00) * 100 ) );
    
return _moisture;

}
void loop(){
  digitalWrite(2,status);
}
