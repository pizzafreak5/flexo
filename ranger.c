#include <pcduino/Arduino.h>
#include <stdio.h>
 
 const int TriPin = 2;
 const int EchoPin = 3;
 float cm;
 
 
void setup()
 {
	pinMode (TriPin, OUTPUT);
	pinMode (EchoPin, INPUT);
 }
 
void loop()
 {
	digitalWrite (TriPin, LOW);
	delayMicroseconds (2);
	digitalWrite (TriPin, HIGH);
	delayMicroseconds (10);
	digitalWrite (TriPin, LOW);
	cm = pulseIn (EchoPin, HIGH, 100000) / 58.0;
	cm = (int (cm * 100.0)) / 100.0;
 
	printf("\nFucker spotted at %f", cm);
 
	delay (1000);
 }
 
