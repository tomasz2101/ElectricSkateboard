import time
import models.i2c as i2c
# import RPi.GPIO as GPIO
import configuration.production as config


class ClassBatteryMeter:
    def __init__(self):
        self.adc_converters = {}
        self.ref_voltage = \
            config.BATTERY_METER["reference_voltage"]
        self.max_value = config.BATTERY_METER["max_value"]

        for i in range(len(config.BATTERY_METER["modules"])):
            address = config.BATTERY_METER["modules"][i]["address"]
            self.adc_converters[i] = i2c.ClassI2cDevice(address)
            self.adc_converters[i].check_connection()

    def read_battery_voltage(self):
        pins = {}
        pins.summary = 0
        for i in range(len(self.adc_converters)):
            pins = len(config.BATTERY_METER["modules"][i]["pins"])
            for j in range(pins):
                pin = config.BATTERY_METER["modules"][i]["pins"][j]
                pin_voltage = self.read_cell_voltage(pin)
                pins[j] = pin_voltage
                pins.summary += pin_voltage
                time.sleep(0.04)
        return pins

        # def read_cell_voltage(self, pin_number):
        # self.adc_converters[i].write_cmd(pin_number)
        # voltage = bus.read_cmd() * self.ref_voltage / float(self.max_value)

        # return True
