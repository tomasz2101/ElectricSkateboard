## Electric Skateboard 
![image](http://imagizer.imageshack.us/v2/1024x768q90/923/lkH8oz.jpg)
### Changes

 - [CHANGELOG.md](https://github.com/tomasz2101/skateboard/blob/master/CHANGELOG.md)

### Requirements
- SD cart (min 8GB)
- raspberry pi
- putty (http://www.putty.org/)
- PiBakery (http://www.pibakery.org/)
- PiBakery configuration (included as rPi_setup_piBakery.xml)

### Project structure
    $ sudo mkdir /skateboard
    $ sudo mkdir /skateboard/src
    $ sudo mkdir /skateboard/log
    $ sudo chwon -R pi:pi /skateboard
### Prepare rPi
    $ sudo . /skateboard/src/devops/preaprare_rpi/install_on_rpi.sh