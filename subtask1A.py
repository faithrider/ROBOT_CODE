#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

num_laps = 1
lap_length = 2000

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=125.5)
robot.settings(straight_speed=500)

for n in range(num_laps):
    robot.straight(-lap_length)
    robot.stop()
    #robot.straight(lap_length)
    robot.stop()