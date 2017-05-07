import smbus
import pcduino as pc
from vl6180x import VL6180X
from time import sleep

from lazers import pews



#INITIALIZATION SEQUENCE

def safe_pinmode(pin, mode):
    try:
        pc.pin_mode(pin, mode)
    except Exception as e:
        print("Can't set pinmode.")
        print(e)
        q = raw_input('Continue [y/n]?')

        if q != 'y' and q != 'Y':
            exit()

def safe_pindown(pin):
    try:
        pc.digital_write(pin, pc.LOW)
        print('{} is LOW'.format(pin))
    except Exception as e:
        print("Can't set pin {} to low.".format(pin))
        print(e)
        q = raw_input('Continue [y/n]?')

        if q != 'y' and q != 'Y':
            exit()
        

def safe_pinup(pin):
    try:
        pc.digital_write(pin, pc.HIGH)
        print('{} is HIGH'.format(pin))
    except Exception as e:
        print("Can't set pin {} to high.".format(pin))
        print(e)
        q = raw_input('Continue [y/n]?')

        if q != 'y' and q != 'Y':
            exit()

def reset_pins(*args):
    for pin in args:
        safe_pinup(pin)

def reset_addr(sensor, address):
    try:
        sensor.change_address(address, 0x29)
    except Exception as e:
        print("Couldn't change address of sensor at {}".format(address))
        print(e)
        q = raw_input('Continue [y/n]?')

        if q != 'y' and q != 'Y':
            exit()

def safe_ch_addr(sensor, address, oldaddress):
    try:
        sensor.change_address(oldaddress, address)
    except Exception as e:
        print("Couldn't change address of sensor at {}".format(oldaddress))
        print(e)
        q = raw_input('Continue [y/n]?')

        if q != 'y' and q != 'Y':
            exit()


shtdn1 = 2
shtdn2 = 7
shtdn3 = 4

lzr1_addr = 0x21
lzr2_addr = 0x23
lzr3_addr = 0x25

default_addr = 0x29

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
safe_pindown(shtdn2)
sleep(sleep_time)
safe_pindown(shtdn3)
sleep(sleep_time)

#Start 1st Sensor
print('Sensor 1 Startup')
safe_pinup(shtdn1)
sleep(sleep_time)
#pews()
try:
    pew1 = VL6180X()
    sensor_good[0] = True
except Exception as e:
    print('Failed sensor 1 Startup')
    print(e)
    q = raw_input('Continue [y/n]?')

    if q != 'y' and q != 'Y':
        exit()

sleep(sleep_time)
safe_ch_addr(pew1, lzr1_addr, default_addr)
sleep(sleep_time)

#pews()

#Start 2st Sensor
print('Sensor 2 Startup')
safe_pinup(shtdn2)
sleep(sleep_time)
try:
    pew2 = VL6180X()
    sensor_good[1] = True
except Exception as e:
    print('Failed sensor 2 Startup')
    print(e)
    q = raw_input('Continue [y/n]?')

    if q != 'y' and q != 'Y':
        exit()

sleep(sleep_time)
safe_ch_addr(pew2, lzr2_addr, default_addr)
sleep(sleep_time)

#pews()

#Start 3st Sensor
print('Sensor 3 Startup')
safe_pinup(shtdn3)
sleep(sleep_time)
try:
    pew3 = VL6180X()
    sensor_good[2] = True
except Exception as e:
    print('Failed sensor 3 Startup')
    print(e)
    q = raw_input('Continue [y/n]?')

    if q != 'y' and q != 'Y':
        exit()

sleep(sleep_time)
safe_ch_addr(pew3, lzr3_addr, default_addr)
sleep(sleep_time)


pews()

