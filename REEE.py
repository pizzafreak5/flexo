import smbus
import pcduino as pc
from vl6180x import VL6180X
from subprocess import call


#setup multiple lasers

shutdown_pin_1 = 1
shutdown_pin_2 = 2
#shutdown_pin_3 = 4

#Addresses
laser_1_addr = 0x12
laser_2_addr = 0x14
laser_3_addr = 0x16

pc.pin_mode(shutdown_pin_1, 'OUTPUT')
pc.pin_mode(shutdown_pin_2, 'OUTPUT')
#pc.pin_mode(shutdown_pin_3, 'OUTPUT')

#Shutdown and restart the lazers to assign new addresses                                                                                                                                                     
pc.digital_write(shutdown_pin_1, pc.LOW)
pc.digital_write(shutdown_pin_2, pc.LOW)



#in order, turn on each sensor, and assign it a new address
#Turn on Sensor 3, which cannot be shut down

sensor_3 = VL6180X()

check = sensor_3.change_address(0x29, laser_3_addr)
#Turn on Sensor 2
pc.digital_write(shutdown_pin_2, pc.HIGH)


sensor_2 = VL6180X()

check = sensor_2.change_address(0x29, laser_2_addr)

#Turn on Sensor 1
pc.digital_write(shutdown_pin_1, pc.HIGH)

sensor_1 = VL6180X()

check = sensor_1.change_address(0x29, laser_1_addr)

call(['i2cdetect','-y','2'])
