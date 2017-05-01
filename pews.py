import smbus
import pcduino as pc
from vl6180x import VL6180X
from time import sleep

from lazers import pews()

shtdn1 = 2
shtdn2 = 7
shtdn3 = 8

lzr1_add = 0x21
lzr2_add = 0x23
lzr3_add = 0x25

sleep_time = 1

sensor_good = [False, False, False]

safe_pinmode(shtdn1, 'OUTPUT')
sleep(sleep_time)
safe_pinmode(shtdn2, 'OUTPUT')
sleep(sleep_time)
safe_pinmode(shtdn3, 'OUTPUT')
sleep(sleep_time)

#Shutdown all lazers

safe_pindown(shtdn1)
sleep(sleep_time)
safe_pindown(shtdn1)
sleep(sleep_time)
safe_pindown(shtdn1)
sleep(sleep_time)

#Start 1st Sensor
print('Sensor 1 Startup')
safe_pinup(shtdn1)
sleep(sleep_time)
try:
    pew1 = sensor()
    sensor_good[0] = True
except Exception as e:
    print('Failed sensor 1 Startup')
    print(e)
    q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y':
            exit()

pews()

#Start 2st Sensor
safe_pinup(shtdn2)
sleep(sleep_time)
try:
    pew2 = sensor()
    sensor_good[1] = True
except Exception as e:
    print('Failed sensor 1 Startup')
    print(e)
    q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y':
            exit()

pews()

#Start 3st Sensor
safe_pinup(shtdn3)
sleep(sleep_time)
try:
    pew3 = sensor()
    sensor_good[3] = True
except Exception as e:
    print('Failed sensor 1 Startup')
    print(e)
    q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y':
            exit()

pews()

#INITIALIZATION SEQUENCE

def safe_pinmode(pin, mode):
    try:
        pc.pin_mode(pin, mode)
    except Exception as e:
        print("Can't set pinmode.")
        print(e)
        q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y':
            exit()

def safe_pindown(pin):
    try:
        pc.digital_write(pin, pc.LOW)
    except Exception as e:
        print("Can't set pin {} to low.".format(pin))
        print(e)
        q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y'::
            exit()
        

def safe_pinup(pin):
    try:
        pc.digital_write(pin, pc.LOW)
    except Exception as e:
        print("Can't set pin {} to low.".format(pin))
        print(e)
        q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y'::
            exit()

def reset_pins(args*):
    for pin in args:
        safe_pinup(pin)

def reset_addr(sensor, address):
    try:
        sensor.change_address(address, 0x29)
    except Exception as e:
        print("Couldn't change address of sensor at {}".format(address))
        print(e)
        q = input('Continue [y/n]?')

        if q != 'y' || q != 'Y'::
            exit()
