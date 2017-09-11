import time
import sys
import RPi.GPIO as GPIO

sys.path.append("/skateboard/src/configuration")
from configuration import *


class ClassLed:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(configuration["led_strip"]["pin_blue"], GPIO.OUT)
        GPIO.setup(configuration["led_strip"]["pin_red"], GPIO.OUT)
        GPIO.setup(configuration["led_strip"]["pin_green"], GPIO.OUT)

        self.blue = GPIO.PWM(configuration["led_strip"]["pin_blue"], configuration["led_strip"]["frequency_hz"])
        self.red = GPIO.PWM(configuration["led_strip"]["pin_blue"], configuration["led_strip"]["frequency_hz"])
        self.green = GPIO.PWM(configuration["led_strip"]["pin_blue"], configuration["led_strip"]["frequency_hz"])

        self.blue.start(0)
        self.red.start(0)
        self.green.start(0)
        self.status = {
            "blue": 0,
            "green": 0,
            "red": 0,
        }

    @staticmethod
    def set_led(led, value):
        try:
            value = int(value)
            if value > configuration["led_strip"]["max_pwm"]:
                raise ValueError('PWM value exceed max possible')
            led.ChangeDutyCycle(value)
            return value
        except ValueError:
            led.ChangeDutyCycle(0)
            return 0

    def set_blue(self, value):
        set_led(self.blue, value)
        self.status["blue"] = value

    def set_green(self, value):
        set_led(self.green, value)
        self.status["green"] = value

    def set_red(self, value):
        set_led(self.red, value)
        self.status["red"] = value

    def increase_green(self):
        try:
            set_led(self.green, int(self.status["green"]) + 1)
        except ValueError:
            set_led(self.green, 0)

    def decrease_green(self):
        try:
            set_led(self.green, int(self.status["green"]) - 1)
        except ValueError:
            set_led(self.green, 0)
