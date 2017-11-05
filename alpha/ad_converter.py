import smbus
import time


# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.


bus = smbus.SMBus(1)
max_voltage = 4.38
max_value = 255
while True:
    bus.write_byte(0x48, 1)
    first_input = bus.read_byte(0x48) * max_voltage / float(max_value)
    bus.write_byte(0x48, 4)
    second_input = bus.read_byte(0x48) * max_voltage / float(max_value)
    print(round(first_input, 2), round(second_input, 2))
    time.sleep(0.04)
