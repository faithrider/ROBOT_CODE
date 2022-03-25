#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from time import sleep

cl = ColorSensor() 
ts = TouchSensor()

# Stop program by long-pressing touch sensor button
#his program will make the color sensor display RGB colors together

while not ts.is_pressed:
    # rgb is a tuple containing three integers
    # each 0-255 representing the amount of
    # red, green and blue in the reflected light
    print(cl.rgb)
    red = cl.rgb[0]
    green=cl.rgb[1]
    blue=cl.rgb[2]
    print("Red: "+str(red)+", Green: "+str(green)+", Blue: "+str(blue)+'\n')
    # '\n' is the newline character so an extra (blank) line is printed
    sleep(1)

    '''
#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire
STUD_MM = 8
# test with a robot that:
# - uses the standard wheels known as EV3Tire
# - wheels are 16 studs apart
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 16 * STUD_MM)

# Enable odometry
mdiff.odometry_start()

# Use odometry to drive to specific coordinates
mdiff.on_to_coordinates(SpeedRPM(40), 300, 300)

# Use odometry to go back to where we started
mdiff.on_to_coordinates(SpeedRPM(40), 0, 0)

# Use odometry to rotate in place to 90 degrees
mdiff.turn_to_angle(SpeedRPM(40), 90)

# Disable odometry
mdiff.odometry_stop()





#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from time import sleep

# Connect  touch sensor to port 1
ts = TouchSensor()
leds = Leds()

leds.all_off() # stop the LEDs flashing (as well as turn them off)

while True:  # The loop will run continously when you keep pressing the touch sensor, color changes from red to yellow and back to red and then yellow and so on
    leds.set_color('LEFT', ('RED',  'YELLOW')[ts.is_pressed])
    leds.set_color('RIGHT', ('RED', 'YELLOW')[ts.is_pressed])
    sleep (0.01) # Give the CPU a rest
    '''