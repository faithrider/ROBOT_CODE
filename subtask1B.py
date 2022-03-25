#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

num_laps = 1
lap_length = 1200
org_lap_length = 304.8
second_lap_length = 2438.4

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=58.5, axle_track=125.5)
robot.settings(straight_speed=300, turn_rate=50)

for y in range(num_laps):
    robot.straight(-org_lap_length)
    robot.stop()
    robot.turn(160)
    robot.stop()
    robot.straight(-second_lap_length)
    robot.stop()
    robot.turn(-168)
    robot.stop()