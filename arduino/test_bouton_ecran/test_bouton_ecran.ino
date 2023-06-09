#include <Arduino.h>
#include <U8g2lib.h>

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif

const int buttonPin = 4; //bouton en D2

int buttonState = 0;
int buttonCount=0;  // compter de clique
int timer=0;

U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);  // High speed I2C



void setup(void) {
  u8g2.begin();
  pinMode(buttonPin, INPUT);
}

void loop(void) {
  
  while(true){

    u8g2.clearBuffer();
    timer=0;          

    buttonState=digitalRead(buttonPin);      // boucle pour lire l'état du bouton
    if(buttonState==HIGH && buttonCount==0){
      buttonCount++;
    
      while(buttonCount==1){
        u8g2.clearBuffer();                  // boucle pour afficher la température  
        u8g2.setFont(u8g2_font_ncenB08_tr);   
        u8g2.drawStr(0,10,"température");    
        u8g2.sendBuffer();
        delay(10);
        buttonState=digitalRead(buttonPin);   // test si nouveau clique
        if(buttonState==HIGH){
          buttonCount++;
        }
        delay(100);
        timer++;                // timer de 5s, si aucune action l'écran s'éteint
        if(timer==50){
          break;
        }
      }
      timer=0;      
      while(buttonCount==2){
        u8g2.clearBuffer();                   
        u8g2.setFont(u8g2_font_ncenB08_tr);   
        u8g2.drawStr(0,10,"humidité");      // boucle pour afficher l'humidité 
        u8g2.sendBuffer();
        delay(10);
        buttonState=digitalRead(buttonPin);
        if(buttonState==HIGH){
          buttonCount+=1;
        }
        delay(100);
        timer++;
        if(timer==50){
          break;
        } 
      }
      timer=0;
      while(buttonCount==3){
        u8g2.clearBuffer();                   
        u8g2.setFont(u8g2_font_ncenB08_tr);   
        u8g2.drawStr(0,10,"qualité");      // boucle pour afficher la qualité de l'air
        u8g2.sendBuffer();
        delay(10);
        buttonState=digitalRead(buttonPin);
        if(buttonState==HIGH){
          buttonCount=0;
        }
        delay(100);
        timer++;
        if(timer==50){
          break;
        } 
      } 
    }
    delay(500);
  }  
}