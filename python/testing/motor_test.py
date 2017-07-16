#!/usr/bin/env python

# esc_start.py
# 2015-04-14
# Public Domain
#
# Sends the servo pulses needed to initialise some ESCs
#
# Requires the pigpio daemon to be running
#
# sudo pigpiod

import time

import pigpio

SERVO = 4

pi = pigpio.pi()  # Connect to local Pi.
pi.set_servo_pulsewidth(SERVO, 1000)  # Minimum throttle.
time.sleep(5)

pi.set_servo_pulsewidth(SERVO, 1000)  # Minimum throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 1500)  # Maximum throttle.

time.sleep(100)

pi.set_servo_pulsewidth(SERVO, 1100)  # Slightly open throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 0)  # Stop servo pulses.

pi.stop()  # Disconnect from local Raspberry Pi.
