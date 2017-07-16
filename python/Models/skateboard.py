#!/usr/bin/python
import pigpio
import configuration
import cwiid
import time
from pprint import pprint

pi = pigpio.pi()


# stop_val = True


class ClassSkateboard(object):
    # skateboard constants
    motor_speed_min = 1000
    motor_speed_max = 2500
    motor_frequency = 50
    motor_smooth_sleep = 0.005
    motor_accel_sleep = 0.015

    def __init__(self):
        print('start')
        pi.set_PWM_frequency(configuration.motor, self.motor_frequency)
        self.speed = self.motor_speed_min
        self.wii = False

    def connect_wii(self):
        connected = False
        while not connected:
            try:
                self.wii = cwiid.Wiimote(bdaddr=configuration.wiimote_address)
                connected = True
                # enable button reporting
                self.wii.rpt_mode = cwiid.RPT_BTN
                self.wii_vibration(0.2, 2)
                self.wii.led = 9
            except RuntimeError:
                print("Error opening wiimote connection")
                pass

    def wii_vibration(self, delay, times):
        for x in range(0, times):
            self.wii.rumble = 1
            time.sleep(delay)
            self.wii.rumble = 0
            if times > 1:
                time.sleep(delay)

    def set_speed(self, speed_value):
        value = max(min(speed_value, self.motor_speed_max), self.motor_speed_min)
        print(value)
        self.speed = value
        time.sleep(Skateboard.smooth_sleep)
        pi.set_servo_pulsewidth(configuration.motor, value)

    def increase_speed(self):
        actual_speed = self.speed
        self.set_speed(actual_speed + 1)

    def decrease_speed(self):
        actual_speed = self.speed
        self.set_speed(actual_speed - 1)

    def run_process(self):
        # global stop_val
        while True:
            buttons = self.wii.state['buttons']
            if buttons & cwiid.BTN_A:
                print('button A')
                pi.set_servo_pulsewidth(configuration.motor, 1000)
                time.sleep(0.5)

            if buttons & cwiid.BTN_UP:
                self.increase_speed()
                print(self.speed)

            if buttons & cwiid.BTN_DOWN:
                self.decrease_speed()
                print(self.speed)

            if buttons & cwiid.BTN_B:
                print('button B')
                pi.set_servo_pulsewidth(configuration.motor, 1700)
                time.sleep(0.5)
