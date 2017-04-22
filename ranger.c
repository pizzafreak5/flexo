#include <core.h>
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
 
	printf("%f", cm)
 
	delay (1000);
 }
 
 int main()
 {
	 int i = 0;
	 for (i = 0; i < 50, i++)
	 {
		 loop()
	 }
 }