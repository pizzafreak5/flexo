# flexo
Embedded project

The purpose of this project is to navigate a course from start to end.

This project uses python 2.7 to control the hardware and the AI responsible for navigating the course.

This project utilizes a pcduino 3, three vl6180x proximity sensors, and the pcduino motor shield (http://store.linksprite.com/motor-shield/) to drive 2 dc motors.

The pcduino folder includes all the python files made available by the makers of the pcduino to allow for hardware control using python. In order to be able to use this pcduino python library and therefore this project, the pcduino linux kernel has to be modified to the one available on linksprite which then allows python to modify the system files that correspond to its GPIO, without doing this, the pcduino will not be able to write to the GPIO files and a generic IOerror will be shown when using python.

The control loop that uses an AI to navigate the course is found in new_ai.py. To start it, using terminal run the command "python new_ai.py" without quotes.

The AI uses a graph search (breadth first search) to determine the best path to take for the course. The course is defined in map_system.py. The course definition can be changed in map_system.py to match a new course. The course is defined as a set of junctions on the map where flexo can change directions.

The motor controls used to control the two motors are defined in motor_controller.py

In order to use the vl6180x.py file, the smbus-cffi python library should be installed. 

The base information used to setup the vl6180x sensors is in vl6180x.py, it was modified from the original RPisensors library to allow the i2c address of the vl6180x sensor to be changed. pews.py extends the usage of the lasers by changing the address of the 3 vl6180x laser sensors used, allowing all three to be used at the same time. pews.py handles the initialization required before using the 3 laser sensors.

To manually control the robot, manual_control.py should be run just how new_ai.py would be run. 


