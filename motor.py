#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor   #we're importing the motor function
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM #we're importing other functions related to speed
from time import sleep
from ev3dev2.motor import MoveTank, MediumMotor, MoveSteering, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound

gy = GyroSensor()
sound = Sound()
angle = gy.angle
angle = 165
#print(str(angle) + ' degrees')  #this will print out the degrees of rotaion of the gyro sensor on the ev3 brick display screen
#sound.play_tone(1000+angle*10, 1) #it will also play a tone 
for n in range(2):
    tank_pair = MoveTank(OUTPUT_B, OUTPUT_D)
    tank_pair.on_for_rotations(left_speed=20, right_speed=20.05, rotations=1)
    tank_pair.on(left_speed=10,right_speed=-10)
    gy.wait_until_angle_change_by(angle)
    tank_pair.on_for_rotations(left_speed=-20, right_speed=-20.05, rotations=1)

    gy.reset()



#tank_pair.on_for_degrees(40, -40, angle, brake=True, block=True)
'''
while not ts.is_pressed:  # while touch sensor is not pressed
    sleep(0.01)
'''
tank_pair.off()
sleep(5)







'''
lm = LargeMotor()    #defining a large motor


This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s

lm.on_for_seconds(speed = 50, seconds=5)    #speed represents the percentage of the rated maximum speed of the motor. 
sleep(1)


This will run at 500 degrees per second (DPS).
You should be able to hear that the motor runs a
little slower than before.

lm.on_for_seconds(speed=SpeedDPS(500), seconds=3)
sleep(1)

# 36000 degrees per minute (DPM) (rarely useful!)
lm.on_for_seconds(speed=SpeedDPM(36000), seconds=3)
sleep(1)

# 2 rotations per second (RPS)
lm.on_for_seconds(speed=SpeedRPS(2), seconds=3)
sleep(1)

# 100 rotations per minute(RPM)
lm.on_for_seconds(speed=SpeedRPM(100), seconds=3)
'''