import motor_controller as m
import time
import getch

speed = 230

while True:
    user_input = getch.getch()

    if user_input == "w":
        m.move_right_forward(speed)
        m.move_left_forward(speed)
    
    if user_input == "q":
        m.move_left_forward(speed)

    if user_input == "e":
        m.move_right_forward(speed)

    if user_input == "a":
        m.move_left_backward(speed)

    if user_input == "d":
        m.move_right_backward(speed)

    if user_input == "s":
        m.move_right_backward(speed)
        m.move_left_backward(speed)

    if user_input == " ":
        m.move_stop()

    if user_input == "x":
        m.move_stop()
        break

    print (user_input)

