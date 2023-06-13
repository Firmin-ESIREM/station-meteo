#include "Air_Quality_Sensor.h"
#include "Arduino.h"
class AirSensor 
{
private:
AirQualitySensor sensor;
public:
AirSensor(int pin);
void inits();
int getqualityair_value();
int getqualityair();
void debug();

};