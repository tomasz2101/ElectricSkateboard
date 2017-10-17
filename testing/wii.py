#!/usr/bin/python
# http://www.raspberrypi-spy.co.uk/?p=1101

import cwiid
import time


def wii_vibration(wii_remote, delay, times):
    for x in range(0, times):
        wii_remote.rumble = 1
        time.sleep(delay)
        wii_remote.rumble = 0
        if times > 1:
            time.sleep(delay)


def print_status():
    print(wii.state)


button_delay = 0.1

print('Press 1 + 2 on your Wii Remote now ...')
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    # start wii remote controll
    wii = cwiid.Wiimote(bdaddr='00:24:1E:A8:47:5F')
    print('Wii Remote connected...\n')
    print('Press some buttons!\n')
    print('Press PLUS and MINUS together to disconnect and quit.\n')
    # enable button reporting
    wii.rpt_mode = cwiid.RPT_BTN
    wii_vibration(wii, 0.2, 2)
    wii.led = 9


except RuntimeError:
    print("Error opening wiimote connection")
    quit()

while True:

    buttons = wii.state['buttons']

    # If Plus and Minus buttons pressed
    # together then rumble and quit.
    if buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0:
        print('\nClosing connection ...')
        wii_vibration(wii, 1, 1)
        exit(wii)

    # Check if other buttons are pressed by
    # doing a bitwise AND of the buttons number
    # and the predefined constant for that button.
    if buttons & cwiid.BTN_LEFT:
        print('Left pressed')
        time.sleep(button_delay)
        print_status()

    if buttons & cwiid.BTN_RIGHT:
        print('Right pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_UP:
        print('Up pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_DOWN:
        print('Down pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_1:
        print('Button 1 pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_2:
        print('Button 2 pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_A:
        print('Button A pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_B:
        print('Button B pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_HOME:
        print('Home Button pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_MINUS:
        print('Minus Button pressed')
        time.sleep(button_delay)

    if buttons & cwiid.BTN_PLUS:
        print('Plus Button pressed')
        time.sleep(button_delay)
