#include "FastLED.h"
#define NUM_LEDS 25
CRGB leds[NUM_LEDS];
#define PIN 2

void setup()
{
  FastLED.addLeds<WS2811, PIN, GRB>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
  Serial.begin(9600);
}


void loop() {
  char mode  = Serial.read();
  if (mode == 'B') {
     FadeInOut(0x1C, 0x77, 0xFF);
    }
  else if (mode == 'Y') {
     FadeInOut(0xFF, 0xE7, 0x0D);
    }
  else if (mode == 'G') {
     FadeInOut(0x03, 0xFF, 0x13);
    }
  else if (mode == 'P') {
     FadeInOut(0xFF, 0x0A, 0x85);
    }
  else if (mode == 'W') {
     FadeInOut(0xFF, 0xFF, 0xFF);
    }
  else if (mode == 'R') {
     FadeInOut(0xFF, 0x1F, 0x1F);
    }
  else if (mode == 'O') {
     FadeInOut(0xFF, 0x77, 0x00);
    }
    
  else {
     setAll(0xFF, 0xFF, 0xFF);
     showStrip();
    
    }
}

void FadeInOut(byte red, byte green, byte blue){
  float r, g, b;
     
  for(int k = 0; k < 220; k=k+1) {
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
    delay(20);
    
  }
     
  for(int k = 220; k >= 0; k=k-2) {
    r = (k/256.0)*red;
    g = (k/256.0)*green;
    b = (k/256.0)*blue;
    setAll(r,g,b);
    showStrip();
    delay(20);
  }
}


void showStrip() {
 #ifdef ADAFRUIT_NEOPIXEL_H
   // NeoPixel
   strip.show();
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   FastLED.show();
 #endif
}

void setPixel(int Pixel, byte red, byte green, byte blue) {
 #ifdef ADAFRUIT_NEOPIXEL_H
   // NeoPixel
   strip.setPixelColor(Pixel, strip.Color(red, green, blue));
 #endif
 #ifndef ADAFRUIT_NEOPIXEL_H
   // FastLED
   leds[Pixel].r = red;
   leds[Pixel].g = green;
   leds[Pixel].b = blue;
 #endif
}

void setAll(byte red, byte green, byte blue) {
  for(int i = 0; i < NUM_LEDS; i++ ) {
    setPixel(i, red, green, blue);
  }
  showStrip();
}
