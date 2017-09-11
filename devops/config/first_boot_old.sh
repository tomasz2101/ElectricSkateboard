no#!/bin/bash

############################################################
#### Execute this script only during first installation ####
############################################################

RED='\033[0;31m' # red color
NC='\033[0m' # no color
GREEN='\033[0;32m' # green color
BLUE='\033[0;34m' # blue color
YELLOW='\033[0;33m' # yellow color

echo -e "${GREEN}Executing first boot...${NC}"
sleep 1

echo "tesT"
if [ $# -eq 0 ]
  then
    echo -e "${RED}No arguments supplied -> test environment${NC}"
fi
# to install each command needs word "true" before e.g. "true apt-get update -y"
declare -a commandsToExecute=(
  #update & upgrade
  "sudo apt-get update -y"
  # install packages
  "sudo mkdir /skateboard"
  "sudo mkdir /skateboard/log"
  "sudo mkdir /skateboard/src"
  "chown -R pi:pi /skateboard"
  "cp ./.ssh ~/.ssh"
  "sudo apt-get install -y git"
  "sudo apt-get install -y vim"
  "sudo apt-get install -y build-essential"
  "sudo apt-get install -y python3"
  "sudo apt-get install -y python3-rpi.gpio"
  "sudo apt-get install -y python-dev"
  "sudo apt-get install -y python-pip"
  "sudo apt-get install -y python-virtualenv"
  "sudo apt-get install -y python-cwiid"
  "sudo pip install pathlib"
  "sudo mkdir /home/pi/logs"
  "git clone git://git.drogon.net/wiringPi"
  "cd  /wiringPi"
  "bash build"
  "sudo pip install wiringpi2"
  "sudo cp ./vim.rc ~/.vimrc"
  "git clone git@github.com:tomasz2101/skateboard.git"
  )

#  this has to be executet as root user
#    echo "dtparam=i2c_arm=on" >> /boot/config.txt


for (( i=0; i<${#commandsToExecute[@]}; i++ )); do
    echo -e "executing: ${GREEN}${commandsToExecute[$i]}${NC}"
    eval ${commandsToExecute[$i]}
done

pidfile="./info.pid"

#if [ -f "$pidfile" ]; then
  echo -e "${RED}Script was allready executed${YELLOW} (if not delete info.pid)${NC}"
#else
  now=$(date +"%Y-%m-%d %H:%M:%S")


  
  # clean after
  #apt-get clean
  # in case of emergency clean manually 
  #rm -rf /var/lib/apt/lists/*

  #other steps
  #pip install pyserial
  #git clone git://git.drogon.net/wiringPi

  #echo "Executing script for the first time"
  #echo "Current time : $now"
  #echo "Script first_boot was executed successfully: $now" >> $pidfile
#fi   
