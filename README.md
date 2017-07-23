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
2. Installation<br/>
    2.1. In putty type:<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.1. sudo apt-get update<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.2. sudo apt-get upgrade<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1.3. (sudo crontab -l ; echo "@reboot python /home/pi/ElectricSkateboard/python/cron/reboot.py") | sudo crontab -
<br/>
            