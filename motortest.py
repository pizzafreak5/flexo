#Test program to drive the motors
import pcduino
#import time

speed_pin_1 = 'gpio9'
pin_forback = 'gpio11'
pin_go = 'gpio8'


pcduino.pin_mode(speed_pin_1, 'OUTPUT')
pcduino.pin_mode(pin_forback, 'OUTPUT')
pcduinp.pin_mode(pin_go, 'OUTPUT')

def loop():
	while True:
		pcduino.analog_swrite(speed_pin_1, 200)
		pcduino.digital_write(pin_forback, gpio.HIGH)
		pcduino.digital_write(pin_go, gpio.HIGH)
