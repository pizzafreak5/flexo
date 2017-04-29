import smbus
import pcduino as pc
from vl6180x import VL6180X

#sensor = VL6180X(debug = False)

#sensor.default_settings()
#def senor_test():
#       for x in range (0, 1000):
#               data = sensor.get_distance()
#               print(data)


#setup multiple lasers

shutdown_pin_1 = 1
shutdown_pin_2 = 2

#Addresses
laser_1_addr = 0x02
laser_2_addr = 0x04
laser_3_addr = 0x06

def initialize():
        pc.pin_mode(shutdown_pin_1, 'OUTPUT')
        pc.pin_mode(shutdown_pin_2, 'OUTPUT')
        #pc.pin_mode(shutdown_pin_3, 'OUTPUT')

        #Shutdown and restart the lazers to assign new addresses                                                                                                                                                     
        pc.digital_write(shutdown_pin_1, pc.LOW)
        pc.digital_write(shutdown_pin_2, pc.LOW)
        #pc.digital_write(shutdown_pin_3, pc.LOW)


        #in order, turn on each sensor, and assign it a new address

        #Turn on Sensor 1
        pc.digital_write(shutdown_pin_1, pc.HIGH)
        sensor_1 = VL6180X()

        check = sensor_1.change_address(0x29, laser_1_addr)

        if check != 0x29:
                print('Address Changed Sucessfully for Sensor 1')

        #Turn on Sensor 2
        pc.digital_write(shutdown_pin_2, pc.HIGH)

        sensor_2 = VL6180X()

        sensor_2.change_address(0x29, laser_2_addr)

        if check != 0x29:
                print('Address Changed Sucessfully for Sensor 1')

        return (sensor_1, sensor_2)


        
        

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


def test_multiple_lazers():

        [sensor_1, sensor_2] = initialize()

        for i in range (0, 200):

                data1 = sensor_1.get_distance()

                data2 = sensor_2.get_distance()

                print('{}:{}'.format(data1,data2))