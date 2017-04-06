#Test program to drive the motors
import pcduino
import os.path
from os import listdir
#import time

pins = listdir(os.path.join(path, 'enable'))

speed_pin_1 = 'gpio9'
pin_forback = 'gpio11'
pin_go = 'gpio8'

for pin in pcduino.pins:
        print('\nPINS:{}'.format(str(pin)))

pcduino.pin_mode(speed_pin_1, 'OUTPUT')
pcduino.pin_mode(pin_forback, 'OUTPUT')
pcduino.pin_mode(pin_go, 'OUTPUT')

def loop():
	while True:
		pcduino.analog_write(speed_pin_1, 200)
		pcduino.digital_write(pin_forback, pcduino.HIGH)
		pcduino.digital_write(pin_go, pcduino.HIGH)

loop()
