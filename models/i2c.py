import smbus
import sys

sys.path.append("/skateboard/src/configuration")
from configuration import *


class ClassI2cDevice:
    def __init__(self, addr, port=1):
        self.addr = addr
        self.bus = smbus.SMBus(port)
        self.detected = False

    # Write a single command
    def write_cmd(self, cmd):
        if self.detected:
            self.bus.write_byte(self.addr, cmd)
            time.sleep(0.0001)

    # read a single command
    def read_cmd(self):
        if self.detected:
            self.bus.read_byte(self.addr)
            time.sleep(0.0001)

    def check_connection(self):
        try:
            self.bus.read_byte(self.addr)
            self.detected = True
        except IOError:
            print("i2c device with port" + self.addr + " in not detected")
