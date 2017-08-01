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
2. Steps<br/>
    2.1. If not using PiBakery:<br/>
    `sudo apt-get update`<br/>
    `sudo apt-get upgrade`<br/>
    `sudo /etc/init.d/ssh start`<br/>
    `sudo dpkg --configure -a`<br/>
    `sudo raspi-config --expand-rootfs`<br/>
    `sudo raspi-config` --> enable I2C </br>
    `sudo systemctl stop serial-getty@ttyAMA0.service`<br/>
    `sudo systemctl disable serial-getty@ttyAMA0.service`<br/>
    `sudo apt-get install screen`<br/>
    `sudo apt-get install -y python3`<br/>
    `sudo apt-get install -y python3-rpi.gpio`<br/>
    `sudo apt-get install git-core`<br/>
    `sudo apt-get install git`<br/>
    `sudo apt-get autoremove`<br/>
    `sudo apt-get autoclean`<br/>
    `git clone https://github.com/tomasz2101/ElectricSkateboard`<br/>
    `(sudo crontab -l ; echo "@reboot python /home/pi/electricSkateboard/cron/reboot.py") | sudo crontab -`<br/>
    2.2. If using PiBakery:<br/>
    `sudo apt-get update`<br/>
    `sudo apt-get upgrade`<br/>
            
