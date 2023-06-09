#!/usr/bin/python
# -*- coding: utf-8 -*-

import Adafruit_PCA9685
import time

# Initialise the PCA9685 using desired address and/or bus:
pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)

# Number of servo
servo_num = 12

# Configure min and max servo pulse lengths
servo_min    = 150 # min. pulse length
servo_max    = 600 # max. pulse length
servo_offset = 50

# Set frequency to 60[Hz]
pwm.set_pwm_freq(60)

while True:
	angle=input("Angle: ")
	# Move servo on each channel
	pwm.set_pwm(1, 0, 150 + int(int(angle) * 2.8))
	pwm.set_pwm(2, 0, 150 + int(int(angle) * 2.8))
	pwm.set_pwm(3, 0, 150 + int(int(angle) * 2.8))
	pwm.set_pwm(4, 0, 150 + int(int(angle) * 2.8))
	pwm.set_pwm(8, 0, 150 + int(int(angle) * 2.8))
	pwm.set_pwm(12, 0, 150 + int(int(angle) * 2.8))
    #for i in range(servo_num):
	#	if a[i]=='1':
	#		print('Moving servo on channel: ', i)
	#		pwm.set_pwm(i, 0, 150 + int(int(angle) * 2.8))
	time.sleep(1)
