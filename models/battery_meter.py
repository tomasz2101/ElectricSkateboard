import time
import sys
from i2c import *
import RPi.GPIO as GPIO

# sys.path.append("/skateboard/src/configuration")
from configuration import *


class ClassBatteryMeter:
    def __init__(self):
        self.adc_converters = {}
        self.ref_voltage = \
            configuration["battery_meter"]["reference_voltage"]
        self.max_value = configuration["battery_meter"]["max_value"]

        for i in range(len(configuration["battery_meter"]["modules"])):
            address = configuration["battery_meter"]["modules"][i]["address"]
            self.adc_converters[i] = ClassI2cDevice(address)
            self.adc_converters[i].check_connection()

    def read_battery_voltage(self):
        pins = {}
        pins.summary = 0
        for i in range(len(self.adc_converters)):
            pins = len(configuration["battery_meter"]["modules"][i]["pins"])
            for j in range(pins):
                pin = configuration["battery_meter"]["modules"][i]["pins"][j]
                pin_voltage = self.read_cell_voltage(pin)
                pins[j] = pin_voltage
                pins.summary += pin_voltage
                time.sleep(0.04)
        return pins

    def read_cell_voltage(self, pin_number):
        self.adc_converters[i].write_cmd(pin_number)
        voltage = bus.read_cmd() * self.ref_voltage / float(self.max_value)

        return voltage
