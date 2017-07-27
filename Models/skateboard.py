#!/usr/bin/python
import pigpio
import configuration
import cwiid
import time
from pprint import pprint
import threading
import subprocess
import sys
# from lcd import *

is_debug = "debug" in sys.argv
pi = pigpio.pi()

stop_val = False


class ClassSkateboard(object):
    # skateboard constants
    motor_frequency = 50
    motor_speed_min = 1000
    motor_speed_max = 2400
    motor_speed_change = 1

    motor_accel_sleep = 0.015
    motor_accel_sleep_min = 0.005
    motor_accel_sleep_max = 0.1
    motor_accel_sleep_change = 0.005

    def __init__(self):
        pi.set_PWM_frequency(configuration.motor, self.motor_frequency)
        self.speed = self.motor_speed_min
        self.wii = False
        # self.display = ClassLcd()
        # self.display.lcd_clear()
        # self.display.lcd_display_string("Skateboard init ...", 1)

    def connect_wii(self):
        connected = False
        while not connected:
            try:
                self.wii = cwiid.Wiimote(bdaddr=configuration.wiimote_address)
                # self.display.lcd_clear()
                # self.display.lcd_display_string("Remote connecting ...", 1)
                # enable button reporting
                self.wii.rpt_mode = cwiid.RPT_BTN
                self.wii_vibration(0.2, 2)
                self.wii_light(1, 0, 0, 1)
                connected = True
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

    def wii_light(self, light1, light2, light3, light4):
        translation = light1 * 8 + light2 * 4 + light3 * 2 + light4
        self.wii.led = translation

    def set_speed(self, speed_value):
        time.sleep(self.motor_accel_sleep)
        value = max(min(speed_value, self.motor_speed_max), self.motor_speed_min)
        self.speed = value
        pi.set_servo_pulsewidth(configuration.motor, value)
        print(value)
        if value % 10 == 0:
            print("test")
            # self.display.lcd_display_string("Speed setting ...", 1)
            # self.display.lcd_display_string(str(value), 2)

    def get_speed(self):
        return self.speed

    def increase_speed(self):
        actual_speed = self.speed
        self.set_speed(actual_speed + self.motor_speed_change)

    def decrease_speed(self):
        actual_speed = self.speed
        self.set_speed(actual_speed - self.motor_speed_change)

    def increase_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(accel_speed + self.motor_accel_sleep_change)

    def decrease_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(accel_speed - self.motor_accel_sleep_change)

    def set_accel_sleep(self, accel_speed_value):
        value = max(min(accel_speed_value, self.motor_accel_sleep_max), self.motor_accel_sleep_min)
        self.motor_accel_sleep = value
        print(self.motor_accel_sleep)
        # self.display.lcd_display_string("Accel setting ...", 1)
        # self.display.lcd_display_string(str(self.motor_accel_sleep), 2)
        time.sleep(0.5)

    def run_process(self):
        # global stop_val
        while True:
            buttons = self.wii.state['buttons']
            if buttons & cwiid.BTN_A:
                print('button A')
                self.set_speed(1000)

            if buttons & cwiid.BTN_UP:
                self.increase_speed()

            if buttons & cwiid.BTN_DOWN:
                self.decrease_speed()

            if buttons & cwiid.BTN_B:
                print('button B')
                self.set_speed(2000)

            if buttons & cwiid.BTN_PLUS:
                self.increase_accel_sleep()

            if buttons & cwiid.BTN_MINUS:
                self.decrease_accel_sleep()


class SkateboardWatcher(threading.Thread):
    ping_bluetooth = ["sudo", "l2ping", "-c", "1", "-t", "1", configuration.wiimote_address]
    power_down = ["sudo", "shutdown", "now"]

    def run(self):
        print('sprawdzenie polaczenia')
        while True:
            self.wiimote_check()
            time.sleep(0.1)

    def try_comms(self):
        command = subprocess.Popen(self.ping_bluetooth, stdout=subprocess.PIPE).communicate()[0]
        return command

    def shutdown(self):
        self.motor_off()
        if is_debug:
            print("OFF")
        else:
            subprocess.call(powerdown)

    @staticmethod
    def motor_off():
        global stop_val
        stop_val = True

    def wiimote_check(self):
        try:
            output = self.try_comms()
            print(output)
            if "100% loss" in output or output == "":
                self.shutdown()
        except Exception as e:
            print(e)
            self.shutdown()
