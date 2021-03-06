ENVIRONMENT = "development"

DEBUG = True

I2C_MODULE = False

GPIO_MODULE = False

LOGGING_DIRECTORY = "/skateboard/log"
PROGRAM_DIRECTORY = "/skateboard/src"

BUS_VERSION = 1

MOTOR = {
    "status": False,
    "pin": 4,
    "max_speed": 2400,
    "min_speed": 1000,
    "frequency": 50,
    "speed_change": 2,
    "accel_sleep": 0.015,
    "accel_sleep_min": 0.005,
    "accel_sleep_max": 0.1,
    "accel_sleep_change": 0.1,
}

LED_STRIP = {
    "status": False,
    "pin_blue": 20,
    "pin_red": 21,
    "pin_green": 22,
    "frequency_hz": 50,
    "max_pwm": 75,
}

LCD_DISPLAY = {
    "status": False,
    "address": 0x27
}

LIGHTS = {
    "status": False,
    "pin_front": 23,
    "pin_back": 24,
}

WII_REMOTE = {
    "status": False,
    "address": "00:24:1E:A8:47:5F"
}

BATTERY_METER = {
    "status": False,
    "reference_voltage": 4.38,
    "max_value": 255,
    "modules": {
        0: {
            "address": 0x44,
            "pins": {
                "s1": 0,
                "s2": 1,
                "s3": 2,
                "s4": 3,
            }
        },
        1: {
            "address": 0x45,
            "pins": {
                "s5": 0,
                "s6": 1,
            }
        },
    },
}
BUTTON_START = 1
LED_READY = 2
