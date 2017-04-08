#Test program to drive the motors
import pcduino
from pcduino.pinmap import PinMap
import os.path
from os import listdir
#import time

path = '/sys/class/misc/pwmtimer/'
pins = listdir(os.path.join(path, 'enable'))

speed_pin_1 = 9
pin_forback = 11
pin_go = 8

for pin in pins:
       print('\nPINS:{}'.format(str(pin)))

pcduino.pin_mode(speed_pin_1, 'OUTPUT')
pcduino.pin_mode(pin_forback, 'OUTPUT')
pcduino.pin_mode(pin_go, 'OUTPUT')

def loop():
	while True:
		pcduino.analog_write(speed_pin_1, 200)
		pcduino.digital_write(pin_forback, pcduino.HIGH)
		pcduino.digital_write(pin_go, pcduino.LOW)
		print ("looped")

loop()
