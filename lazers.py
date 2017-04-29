import smbus
import pcduino as pc
from vl6180x import VL6180X
from subprocess import call

#sensor = VL6180X(debug = False)

#sensor.default_settings()
#def senor_test():
#       for x in range (0, 1000):
#               data = sensor.get_distance()
#               print(data)


#setup multiple lasers

shutdown_pin_1 = 1
shutdown_pin_2 = 2
#shutdown_pin_3 = 4

#Addresses
laser_1_addr = 0x12
laser_2_addr = 0x14
laser_3_addr = 0x16


def ch_addr_test():			# Depricated function to be deleted
        sensor = VL6180X()
        sensor.change_address(0x29, 0x10)

def initialize():
        pc.pin_mode(shutdown_pin_1, 'OUTPUT')
        pc.pin_mode(shutdown_pin_2, 'OUTPUT')
        #pc.pin_mode(shutdown_pin_3, 'OUTPUT')

        #Shutdown and restart the lazers to assign new addresses                                                                                                                                                     
        pc.digital_write(shutdown_pin_1, pc.LOW)
        pc.digital_write(shutdown_pin_2, pc.LOW)
        #pc.digital_write(shutdown_pin_3, pc.LOW)

        pews()

        input('Continue?')


        #in order, turn on each sensor, and assign it a new address

        #Turn on Sensor 3, which cannot be shut down
        sensor_3 = VL6180X()

        check = sensor_3.change_address(0x29, laser_3_addr)

        if check != 0x29:
                print('Address Changed Sucessfully for Sensor 3')

        pews()

        input('Continue?')

        #Turn on Sensor 2
        pc.digital_write(shutdown_pin_2, pc.HIGH)

        pews()

        input('Continue?')

        sensor_2 = VL6180X()

        check = sensor_2.change_address(0x29, laser_2_addr)

        if check != 0x29:
                print('Address Changed Sucessfully for Sensor 2')

        pews()

        input('Continue?')

        #Turn on Sensor 1
        pc.digital_write(shutdown_pin_1, pc.HIGH)

        pews()

        input('Continue?')

        sensor_1 = VL6180X()

        check = sensor_1.change_address(0x29, laser_1_addr)

        pews()

        input('Continue?')

        if check != 0x29:
                print('Address Changed Sucessfully for Sensor 1')

        return (sensor_1, sensor_2, sensor_3)


        
        

def shutdown_test():
        
        pc.pin_mode(shutdown_pin_1, 'OUTPUT')
        pc.pin_mode(shutdown_pin_2, 'OUTPUT')
        pc.pin_mode(shutdown_pin_3, 'OUTPUT')

        pc.digital_write(shutdown_pin_1, pc.LOW)
        pc.digital_write(shutdown_pin_2, pc.LOW)
        
        sensor = VL6180X()

        print('Shutdown Test')
        print ('LASER ON')
        
        
        pc.digital_write(shutdown_pin_3, pc.HIGH)
        for i in range (0, 25):
                data = sensor.get_distance()
                print(data)

        print('LASER OFF')
        pc.digital_write(shutdown_pin_3, pc.LOW)

        for i in range (0, 25):
                data = sensor.get_distance()
                print(data)


def test_multiple_lazers():

        [sensor_1, sensor_2, sensor_3] = initialize()

        for i in range (0, 200):

                data1 = sensor_1.get_distance()

                data2 = sensor_2.get_distance()

                data3 = sensor_3.get_distance()

                print('{}:{}:{}'.format(data1,data2,data3))

def pews():
        call(['i2cdetect', '-y', '2'])
        
