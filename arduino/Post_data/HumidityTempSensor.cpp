#include "humidityTempSensor.h"
#define DHTTYPE DHT10
#define DHTPIN 2
Humidity_TempSensor::Humidity_TempSensor(): dht(DHTTYPE)
{

  
}
void Humidity_TempSensor:: inits()
{
Serial.println("Waiting Humidity temp sensor to init...");
  delay(20000);
  Wire.begin();
  dht.begin();
 if (1) 
    {
        Serial.println("Pression sensor ready.");
    } 
    else
    {
        Serial.println("Pression sensor ERROR!");
    }

}
float Humidity_TempSensor::get_temp_value()
{
   float temp_hum_val[2] = {0};
  dht.readTempAndHumidity(temp_hum_val); 
  return temp_hum_val[1];

}

float Humidity_TempSensor::get_humidity_value()
{
  float temp_hum_val[2] = {0};
  dht.readTempAndHumidity(temp_hum_val);
  return temp_hum_val[0];

}
void Humidity_TempSensor::debug()
{
<<<<<<< HEAD

=======
  Serial.println("Humidity:");
  Serial.println(get_humidity_value());

  Serial.println("Temperature:");
  Serial.println(get_temp_value());
>>>>>>> 90d9b703aec2369c57779c3160effef96d2f57e6

}