
#include "DHT.h"
#include "Seeed_BMP280.h"
#include <Wire.h>
#include"AirQuality.h"

// temperature et humidite
#define DHTTYPE DHT10 
DHT dht(DHTTYPE);

#if defined(ARDUINO_ARCH_AVR)
    #define debug  Serial

#elif defined(ARDUINO_ARCH_SAMD) ||  defined(ARDUINO_ARCH_SAM)
    #define debug  SerialUSB
#else
    #define debug  Serial
#endif

// pression
BMP280 bmp280;


// qualite de l'air
int current_quality =-1;


void setup() {

    Serial.begin(9600);

    while(!Serial){
      Serial.println("Waiting sensor to init...");
      delay(200000);        
    }

    debug.begin(115200);
    debug.println("DHTxx test!");
    Wire.begin();
    dht.begin();

    if(!bmp280.init()){
    debug.println("Device error!");

  }
    
}

void loop() {
    float temp_hum_val[2] = {0};
    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)


    if (!dht.readTempAndHumidity(temp_hum_val)) {
        debug.print("Humidity: ");
        debug.print(temp_hum_val[0]);
        debug.print(" %\t");
        debug.print("Temperature: ");
        debug.print(temp_hum_val[1]);
        debug.println(" *C");
    } else {
        debug.println("Failed to get temprature and humidity value.");
    }

    

float pressure;
  
  
  //get and print atmospheric pressure data
  debug.print("Pressure: ");
  debug.print(pressure = bmp280.getPressure()/100);
  debug.println("hPa");
  
  //get and print altitude data
  debug.print("Altitude: ");
  debug.print(bmp280.calcAltitude(pressure*100));
  debug.println("m");
  
  
  
  
  
  debug.println("\n");//add a line between output of different times.

  




  delay(2000);



}