# SmartPython
Python for Smart Home

Requirements:
- SD cart (min 8GB)
- raspberry pi
- putty (http://www.putty.org/)
- PiBakery (http://www.pibakery.org/)
- PiBakery configuration (included as rPi_setup_piBakery.xml)

1. Installation<br/>
    1.1. Install PiBakery<br/>
    1.2. Import configuration and change network SSID and password<br/>
    1.3. Write system to SD card<br/>
2. Domoticz installation<br/>
    2.1. In putty type:<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.1. sudo apt-get update<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.2. sudo apt-get upgrade<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.3. sudo curl -L install.domoticz.com | sudo bash<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.4. sudo reboot<br/>
3. Start Domoticz<br/>
    3.1. Open link 192.168.0.x:8080<br/>
4. Enable I2C support<br/>
    4.1. First check<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.1. ls -l/dev<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.1.2. ls -l /dev/ttyAMA0<br/>
    4.2. If it was empty<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1. sudo nano /boot/config.txt<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.2. change enable_uart=0 to enable_uart=1<br/>
    4.3. sudo reboot<br/>
5. Domoticz configuration to use python scripts<br/>
    5.1. For each dummy switch on on/off command put: <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script:///home/pi/SmartHome/python/switchExecute.py id command<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id = global switch id<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command = on/off/1/0