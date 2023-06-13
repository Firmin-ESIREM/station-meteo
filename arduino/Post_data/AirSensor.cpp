#include "AirSensor.h"
AirSensor::AirSensor(int pin): sensor(pin)
{
}
void AirSensor::inits()
{ 
  Serial.println("Waiting Air Quality sensor to init...");
  delay(20000);
 if (sensor.init()) 
    {
        Serial.println("Air Quality sensor ready.");
    } 
    else
    {
        Serial.println("Air Quality Sensor ERROR!");
    }
}

int AirSensor::getqualityair_value()
{
    int quality = sensor.slope();
    return sensor.getValue();
}
int AirSensor::getqualityair()
{
  
    int quality = sensor.slope();
    if (quality == AirQualitySensor::FORCE_SIGNAL) {
        return 0;
    } else if (quality == AirQualitySensor::HIGH_POLLUTION) {
        return 1;
    } else if (quality == AirQualitySensor::LOW_POLLUTION) {
        return 2;
    } else if (quality == AirQualitySensor::FRESH_AIR) {
        return 3;
    }
}
void AirSensor::debug()
{

  
    int quality = sensor.slope();
    Serial.print("Sensor value: ");
    Serial.println(sensor.getValue());
    if (quality == AirQualitySensor::FORCE_SIGNAL) {
        Serial.println("High pollution! Force signal active.");
    } else if (quality == AirQualitySensor::HIGH_POLLUTION) {
        Serial.println("High pollution!");
    } else if (quality == AirQualitySensor::LOW_POLLUTION) {
        Serial.println("Low pollution!");
    } else if (quality == AirQualitySensor::FRESH_AIR) {
        Serial.println("Fresh air.");
    }
  

}