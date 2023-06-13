#include "Seeed_BMP280.h"
#include "Arduino.h"
class PressionSensor
{
private:
BMP280 bmp280;
public:
PressionSensor();
void inits();
float getpression_value();
void debug();

};