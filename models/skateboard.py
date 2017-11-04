#!/usr/bin/python
import time
from pprint import pprint
import threading
import subprocess
import sys
import configuration

if configuration["environment"]["status"] == "production":
    import pigpio
    import cwiid
    from lcd import *
    from led import *

    pi = pigpio.pi()

is_debug = "debug" in sys.argv

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
        if configuration["led_strip"]["status"]:
            self.led_strip = ClassLed()
            self.led_strip.set_green(50)
        if configuration["motor"]["status"]:
            pi.set_PWM_frequency(configuration["motor"]["pin"],
                                 self.motor_frequency)
        self.speed = self.motor_speed_min
        self.speed_percentage = 0
        self.wii = False
        self.configuration = configuration
        if configuration["lcd_display"]["status"]:
            self.display = ClassLcd()
            self.display.lcd_clear()
            self.display.lcd_display_string("Hello World :D", 1)
        self.wii_led = 0

    def connect_wii(self):
        connected = False
        while not connected:
            try:
                address = configuration["wii_remote"]["address"]
                self.wii = cwiid.Wiimote(bdaddr=address)
                # enable button reporting
                self.wii.rpt_mode = cwiid.RPT_BTN
                self.wii_vibration(0.2, 2)
                self.set_wii_light(1, 0, 0, 1)
                connected = True
                if configuration["lcd_display"]["status"]:
                    self.display.lcd_clear()
                    self.display.lcd_display_string("Remote connected ...", 1)
            except RuntimeError:
                if configuration["environment"]["status"] != "production":
                    print("Error opening wiimote connection")
                pass

    def wii_vibration(self, delay, times):
        for x in range(0, times):
            self.wii.rumble = 1
            time.sleep(delay)
            self.wii.rumble = 0
            if times > 1:
                time.sleep(delay)

    def set_wii_light(self, light1, light2, light3, light4):
        translation = light4 * 8 + light3 * 4 + light2 * 2 + light1
        self.wii_led = translation
        self.wii.led = translation

    def get_wii_light(self):
        return self.wii.led

    def check_wii_light(self):
        if configuration["environment"]["status"] != "production":
            pprint(self.wii_led)

    def set_speed(self, speed_value):
        time.sleep(self.motor_accel_sleep)
        value = max(min(speed_value, self.motor_speed_max),
                    self.motor_speed_min)
        self.speed = value
        pi.set_servo_pulsewidth(configuration["motor"]["pin"], value)

        if value < 1350 and self.get_wii_light != 0:
            self.set_wii_light(0, 0, 0, 0)
        if 1350 <= value < 1700 and self.get_wii_light != 1:
            self.set_wii_light(1, 0, 0, 0)
        if 1700 <= value < 2050 and self.get_wii_light != 3:
            self.set_wii_light(1, 1, 0, 0)
        if 2050 <= value < 2400 and self.get_wii_light != 7:
            self.set_wii_light(1, 1, 1, 0)
        if 2400 <= value < 2500 and self.get_wii_light != 15:
            self.set_wii_light(1, 1, 1, 1)
        speed_percentage = int((value - self.motor_speed_min) /
                               float(self.motor_speed_max -
                                     self.motor_speed_min) * 100)
        if configuration["lcd_display"]["status"] \
                and self.speed_percentage != speed_percentage:
            self.display.lcd_clear()
            self.display.lcd_display_string("Speed setting ...", 1)
            self.display.lcd_display_string(str(speed_percentage), 2)
        # if configuration["environment"]["status"] != "production":
        print(speed_percentage)
        self.speed_percentage = speed_percentage

    def get_speed(self):
        return self.speed

    def increase_speed(self, multiplier):
        actual_speed = self.speed
        self.set_speed(actual_speed + self.motor_speed_change * multiplier)

    def decrease_speed(self, multiplier):
        actual_speed = self.speed
        self.set_speed(actual_speed - self.motor_speed_change * multiplier)

    def increase_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(accel_speed + self.motor_accel_sleep_change)

    def decrease_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(accel_speed - self.motor_accel_sleep_change)

    def set_accel_sleep(self, accel_speed_value):
        value = max(min(accel_speed_value, self.motor_accel_sleep_max),
                    self.motor_accel_sleep_min)
        self.motor_accel_sleep = value
        print(self.motor_accel_sleep)
        if configuration["lcd_display"]["status"]:
            self.display.lcd_display_string("Accel setting ...", 1)
            self.display.lcd_display_string(str(self.motor_accel_sleep), 2)
        time.sleep(0.1)

    def read_wii_buttons(self):
        # global stop_val
        while True:
            buttons = self.wii.state['buttons']
            if buttons & cwiid.BTN_A:
                self.set_speed(1000)

            if buttons & cwiid.BTN_UP:
                self.increase_speed(1)

            if buttons & cwiid.BTN_DOWN:
                self.decrease_speed(3)

            if buttons & cwiid.BTN_B:
                self.increase_speed(3)

            if buttons & cwiid.BTN_PLUS:
                # self.increase_accel_sleep()
                self.led_strip.increase_green()

            if buttons & cwiid.BTN_MINUS:
                # self.decrease_accel_sleep()
                self.led_strip.decrease_green()

    @staticmethod
    def read_console_input():
        # global stop_val
        while True:
            console_input = input("Waiting for inputs\n")
            print(console_input)


class SkateboardWatcher(threading.Thread):
    ping_bluetooth = ["sudo",
                      "l2ping",
                      "-c",
                      "1",
                      "-t",
                      "1",
                      configuration["wii_remote"]["address"]]
    power_down = ["sudo", "shutdown", "now"]

    def run(self):
        print('sprawdzenie polaczenia')
        while True:
            self.wiimote_check()
            time.sleep(0.1)

    def try_comms(self):
        command = subprocess.Popen(self.ping_bluetooth,
                                   stdout=subprocess.PIPE).communicate()[0]
        return command

    def shutdown(self):
        self.motor_off()
        if is_debug:
            print("OFF")
        else:
            print("OFF")
            # subprocess.call(powerdown)

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
