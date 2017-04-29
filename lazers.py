import smbus
import pcduino as pc
from vl6180x import VL6180X

sensor = VL6180X(debug = False)

sensor.default_settings()
def senor_test():
	for x in range (0, 1000):
		data = sensor.get_distance()
		print(data)


#setup multiple lasers

shutdown_pin_1 = 1
shutdown_pin_2 = 2 

def initilize():
	pc.pin_mode(shutdown_pin_1, 'OUTPUT')
	pc.pin_mode(shutdown_pin_2, 'OUTPUT')

	#Shutdown and restart the lazers                                                                                                                                                     
	pc.digital_write(shutdown_pin_1, pc.LOW)
	pc.digital_write(shutdown_pin_1, pc.LOW)

def shutdown_test():

	print('Shutdown Test')
	print ('LASER ON')

	pc.pin_mode(shutdown_pin_1, 'OUTPUT')
	pc.digital_write(shutdown_pin_1, pc.HIGH)
	for i in range (0, 500):
		data = sensor.get_distance()
		print(data)

	print('LASER OFF')
	pc.digital_write(shutdown_pin_1, pc.LOW)

	for i in range (0, 500):
		data = sensor.get_distance()
		print(data)
