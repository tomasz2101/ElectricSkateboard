#!/usr/bin/python
import re
import smbus


class ClassAdafruitI2C(object):
    def __init__(self, address, busnum=-1, notification=False):
        """
        object init
        :param address: (string) i2c device address 
        :param busnum: (int) raspberry pi i2c bus
        :param notification: (bool) if print notification
        """
        self.address = address
        self.bus = smbus.SMBus(busnum if busnum >= 0 else self.get_pi_i2_c_bus_number())
        self.notification = notification

    @staticmethod
    def get_pi_revision():
        """Gets the version number of the Raspberry Pi board"""
        try:
            with open('/proc/cpuinfo', 'r') as infile:
                for line in infile:
                    # Match a line of the form "Revision : 0002" while ignoring extra
                    # info in front of the revision (like 1000 when the Pi was over-volted).
                    match = re.match('Revision\s+:\s+.*(\w{4})$', line)
                    if match and match.group(1) in ['0000', '0002', '0003']:
                        # Return revision 1 if revision ends with 0000, 0002 or 0003.
                        return 1
                    elif match:
                        # Assume revision 2 if revision ends with any other 4 chars.
                        return 2
                # Couldn't find the revision, assume revision 0 like older code for compatibility.
                return 0
        except IOError:
            return 0

    def get_pi_i2_c_bus_number(self):
        # Gets the I2C bus number /dev/i2c#
        return 1 if self.get_pi_revision() > 1 else 0

    @staticmethod
    def reverse_byte_order(data):
        """Reverses the byte order of an int (16-bit) or long (32-bit) value"""
        byte_count = len(hex(data)[2:].replace('L', '')[::2])
        val = 0
        for i in range(byte_count):
            val = (val << 8) | (data & 0xff)
            data >>= 8
        return val

    def err_msg(self):
        print "Error accessing 0x%02X: Check your I2C address" % self.address
        return -1

    def write8(self, reg, value):
        """Writes an 8-bit value to the specified register/address"""
        try:
            self.bus.write_byte_data(self.address, reg, value)
            if self.notification:
                print "I2C: Wrote 0x%02X to register 0x%02X" % (value, reg)
        except IOError:
            return self.err_msg()

    def write16(self, reg, value):
        """Writes a 16-bit value to the specified register/address pair"""
        try:
            self.bus.write_word_data(self.address, reg, value)
            if self.notification:
                print("I2C: Wrote 0x%02X to register pair 0x%02X,0x%02X" % (value, reg, reg + 1))
        except IOError:
            return self.err_msg()

    def write_raw8(self, value):
        """Writes an 8-bit value on the bus"""
        try:
            self.bus.write_byte(self.address, value)
            if self.notification:
                print "I2C: Wrote 0x%02X" % value
        except IOError:
            return self.err_msg()

    def write_list(self, reg, received_list):
        """Writes an array of bytes using I2C format"""
        try:
            if self.notification:
                print "I2C: Writing list to register 0x%02X:" % reg
                print received_list
            self.bus.write_i2c_block_data(self.address, reg, received_list)
        except IOError:
            return self.err_msg()

    def read_list(self, reg, length):
        """Read a list of bytes from the I2C device"""
        try:
            results = self.bus.read_i2c_block_data(self.address, reg, length)
            if self.notification:
                print("I2C: Device 0x%02X returned the following from reg 0x%02X" % (self.address, reg))
                print results
            return results
        except IOError:
            return self.err_msg()

    def read_u8(self, reg):
        """Read an unsigned byte from the I2C device"""
        try:
            result = self.bus.read_byte_data(self.address, reg)
            if self.notification:
                print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
            return result
        except IOError:
            return self.err_msg()

    def read_s8(self, reg):
        """Reads a signed byte from the I2C device"""
        try:
            result = self.bus.read_byte_data(self.address, reg)
            if result > 127:
                result -= 256
            if self.notification:
                print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
            return result
        except IOError:
            return self.err_msg()

    def read_u16(self, reg, little_endian=True):
        """Reads an unsigned 16-bit value from the I2C device"""
        try:
            result = self.bus.read_word_data(self.address, reg)
            # Swap bytes if using big endian because read_word_data assumes little
            # endian on ARM (little endian) systems.
            if not little_endian:
                result = ((result << 8) & 0xFF00) + (result >> 8)
            if self.notification:
                print "I2C: Device 0x%02X returned 0x%04X from reg 0x%02X" % (self.address, result & 0xFFFF, reg)
            return result
        except IOError:
            return self.err_msg()

    def read_s16(self, reg, little_endian=True):
        """Reads a signed 16-bit value from the I2C device"""
        try:
            result = self.read_u16(reg, little_endian)
            if result > 32767:
                result -= 65536
            return result
        except IOError:
            return self.err_msg()


if __name__ == '__main__':
    try:
        bus = ClassAdafruitI2C(address=0)
        print "Default I2C bus is accessible"
    except IOError:
        print "Error accessing default I2C bus"
