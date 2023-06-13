#include <DHT.h>   
class Humidity_TempSensor
{
private:
DHT dht;
public:
Humidity_TempSensor();
void inits();
float get_temp_value();
float get_humidity_value();
void debug();

};
