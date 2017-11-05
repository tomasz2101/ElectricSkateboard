#!/usr/bin/python
from pprint import pprint
import threading
import subprocess
import configuration.config_helper as config
import time

if config.ENVIRONMENT == "production":
    import pigpio
    import cwiid
    import models.lcd as lcd
    import models.led as led

    pi = pigpio.pi()

stop_val = False


class ClassSkateboard(object):
    def __init__(self):
        if config.LED_STRIP["status"]:
            self.led_strip = led.ClassLed()
            self.led_strip.set_green(50)

        if config.MOTOR["status"]:
            pi.set_PWM_frequency(config.MOTOR["pin"],
                                 config.MOTOR["frequency"])
        self.speed = config.MOTOR["min_speed"]
        self.speed_percentage = 0
        self.motor_accel_sleep = config.MOTOR["accel_sleep"]
        self.wii = {}
        if config.LCD_DISPLAY["status"]:
            self.display = lcd.ClassLcd()
            self.display.lcd_clear()
            self.display.lcd_display_string(message="Hello World :D", line=1)
        self.wii_led = 0

    def connect_wii(self):
        connected = False
        while not connected:
            try:
                self.wii = cwiid.Wiimote(bdaddr=config.WII_REMOTE["address"])
                # enable button reporting
                self.wii.rpt_mode = cwiid.RPT_BTN
                self.wii_vibration(delay=0.2, times=2)
                self.set_wii_light(light0=1, light1=0, light2=0, light3=1)
                connected = True
                if config.LCD_DISPLAY["status"]:
                    self.display.lcd_clear()
                    self.display.lcd_display_string(
                        message="Remote connected ...",
                        line=1)
            except RuntimeError:
                if config.DEBUG:
                    print("Error opening wiimote connection")
                pass

    def wii_vibration(self, delay, times):
        for x in range(0, times):
            self.wii.rumble = 1
            time.sleep(delay)
            self.wii.rumble = 0
            if times > 1:
                time.sleep(delay)

    def set_wii_light(self, light0, light1, light2, light3):
        translation = light3 * 8 + light2 * 4 + light1 * 2 + light0
        self.wii_led = translation
        self.wii.led = translation

    def get_wii_light(self):
        return self.wii_led

    def check_wii_light(self):
        if config.DEBUG:
            pprint(self.wii_led)

    def set_speed(self, speed_value, decrease_delay):
        time.sleep(self.motor_accel_sleep / decrease_delay)
        value = max(min(speed_value, config.MOTOR["max_speed"]),
                    config.MOTOR["min_speed"])
        self.speed = value
        pi.set_servo_pulsewidth(config.MOTOR["pin"], value)
        if value < 1350 and self.get_wii_light != 0:
            self.set_wii_light(light0=0, light1=0, light2=0, light3=0)
        if 1350 <= value < 1700 and self.get_wii_light != 1:
            self.set_wii_light(light0=1, light1=0, light2=0, light3=0)
        if 1700 <= value < 2050 and self.get_wii_light != 3:
            self.set_wii_light(light0=1, light1=1, light2=0, light3=0)
        if 2050 <= value < 2400 and self.get_wii_light != 7:
            self.set_wii_light(light0=1, light1=1, light2=1, light3=0)
        if 2400 <= value < 2500 and self.get_wii_light != 15:
            self.set_wii_light(light0=1, light1=1, light2=1, light3=1)
        speed_percentage = int((value - config.MOTOR["min_speed"]) /
                               float(config.MOTOR["max_speed"] -
                                     config.MOTOR["min_speed"]) * 100)

        if self.speed_percentage != speed_percentage:
            print(speed_percentage)
            if config.LCD_DISPLAY["status"]:
                self.display.lcd_clear()
                self.display.lcd_display_string(
                    message="Speed setting ...",
                    line=1)
                self.display.lcd_display_string(
                    message=str(speed_percentage),
                    line=2)
        self.speed_percentage = speed_percentage

    def get_speed(self):
        return self.speed

    def increase_speed(self, decrease_delay):
        actual_speed = self.speed
        self.set_speed(
            speed_value=actual_speed + config.MOTOR["speed_change"],
            decrease_delay=decrease_delay)

    def decrease_speed(self, decrease_delay):
        actual_speed = self.speed
        self.set_speed(
            speed_value=actual_speed - config.MOTOR["speed_change"],
            decrease_delay=decrease_delay)

    def increase_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(
            accel_speed_value=accel_speed + config.MOTOR["accel_sleep_change"])

    def decrease_accel_sleep(self):
        accel_speed = self.motor_accel_sleep
        self.set_accel_sleep(
            accel_speed_value=accel_speed - config.MOTOR["accel_sleep_change"])

    def set_accel_sleep(self, accel_speed_value):
        value = max(min(accel_speed_value, config.MOTOR["accel_sleep_max"]),
                    config.MOTOR["accel_sleep_min"])
        self.motor_accel_sleep = value
        print(self.motor_accel_sleep)
        if config.LCD_DISPLAY["status"]:
            self.display.lcd_display_string(
                message="Accel setting ...",
                line=1)
            self.display.lcd_display_string(
                message=str(self.motor_accel_sleep),
                line=2)
        time.sleep(0.1)

    def read_wii_buttons(self):
        # global stop_val
        while True:
            buttons = self.wii["state"]['buttons']
            if buttons & cwiid.BTN_A:
                self.set_speed(speed_value=1000, decrease_delay=1)

            if buttons & cwiid.BTN_UP:
                self.increase_speed(decrease_delay=1)

            if buttons & cwiid.BTN_DOWN:
                self.decrease_speed(decrease_delay=3)

            if buttons & cwiid.BTN_B:
                self.increase_speed(decrease_delay=3)

                # if buttons & cwiid.BTN_PLUS:
                # self.increase_accel_sleep()
                # self.led_strip.increase_green()

                # if buttons & cwiid.BTN_MINUS:
                # self.decrease_accel_sleep()
                # self.led_strip.decrease_green()

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
                      config.WII_REMOTE["address"]]
    power_down = ["sudo", "shutdown", "now"]

    def run(self):
        print('testing connection')
        while True:
            self.wiimote_check()
            time.sleep(0.1)

    def try_comms(self):
        command = subprocess.Popen(self.ping_bluetooth,
                                   stdout=subprocess.PIPE).communicate()[0]
        return command

    def shutdown(self):
        self.motor_off()
        if config.DEBUG:
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
