import os
import subprocess
import logging

ENVIRONMENT = "production"

DEBUG = True

I2C_MODULE = True

GPIO_MODULE = True

LOGGING_DIRECTORY = "/skateboard/log"
PROGRAM_DIRECTORY = "/skateboard/src"

BUS_VERSION = 1

MOTOR = {
    "status": True,
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
    "status": True,
    "address": 0x27
}

LIGHTS = {
    "status": False,
    "pin_front": 23,
    "pin_back": 24,
}

WII_REMOTE = {
    "status": True,
    "address": "00:24:1E:A8:47:5F"
}

BATTERY_METER = {
    "status": True,
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


def climb(path):
    """The the root directory name"""
    while 1:
        yield path
        parts = os.path.split(path)
        if parts[0] == path:  # Reached root
            break
        path = parts[0]


def get_repo_name(path):
    """ Find the repo name for a path.
        Returns None if not a repo.
    """
    cwd = os.getcwd()
    os.chdir(path)
    result = subprocess.run(['git', 'config', '--get', 'remote.origin.url'],
                            stdout=subprocess.PIPE)
    repo_name = os.path.basename(result.stdout.decode().strip())
    logging.info('get_repo_name: %s %s', path, repo_name)
    os.chdir(cwd)
    return repo_name
