#include "PressionSensor.h"
PressionSensor::PressionSensor(): bmp280()
{
}
void PressionSensor::inits()
{
   Serial.println("Waiting Pression sensor to init...");
  delay(20000);
 if (bmp280.init()) 
    {
        Serial.println("Pression sensor ready.");
    } 
    else
    {
        Serial.println("Pression sensor ERROR!");
    }
}
float PressionSensor::getpression_value()
{
  float pressure;
  pressure = bmp280.getPressure()/100;
  return pressure;
}
void PressionSensor::debug()
{

  Serial.println("Pressure: ");
  Serial.println(getpression_value());
  Serial.println("hPa");


}