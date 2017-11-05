#!/bin/bash

############################################################
#### Execute this script only during first installation ####
############################################################

RED='\033[0;31m' # red color
NC='\033[0m' # no color
GREEN='\033[0;32m' # green color
BLUE='\033[0;34m' # blue color
YELLOW='\033[0;33m' # yellow color
now=$(date +"%Y-%m-%d %H:%M:%S")

echo -e now "${GREEN}Executing first boot...${NC}"
sleep 1

declare -a commandsToExecute=(
  # Update
  "sudo apt-get update -y"
  # Prepare files structure
  "sudo mkdir /skateboard"
  "sudo mkdir /skateboard/log"
  "sudo mkdir /skateboard/src"
  "sudo mkdir /skateboard/data"
  "sudo mkdir /backup"
  #"sudo mkdir /home/pi/logs"
  # Install packages
  "sudo apt-get install -y git"
  "sudo apt-get install -y vim"
  "sudo apt-get install -y build-essential"
  "sudo apt-get install -y python3"
  "sudo apt-get install -y python3-rpi.gpio"
  "sudo apt-get install -y python-dev"
  "sudo apt-get install -y python-pip"
  "sudo apt-get install -y python-virtualenv"
  "sudo apt-get install -y python-cwiid"
  "sudo apt-get install -y dos2unix"
  # Install pip packages
  "sudo pip install pathlib"
  # Install wiringPi
  "git clone git://git.drogon.net/wiringPi"
  "cd  /wiringPi"
  "bash build"
  "sudo pip install wiringpi2"
  "rm -rf /wiringPi"
  # Copy files
  "sudo cp ./vim.rc ~/.vimrc"
  # Copy repository
  "sudo git clone git@github.com:tomasz2101/skateboard.git /skateboard/src/"
  # Change directory owner
  "sudo chown -R pi:pi /skateboard"
  "sudo chown -R pi:pi /backup"
  # Backup crontab before replacing
  "sudo crontab -l > /backup/crontab_backup_${now}"
  # Replace crontab
  "sudo dos2unix ./crontabfile"
  "sudo crontab ./crontabfile"
  # Output crontab to validate by user
  "sudo crontab -l"
  )

for (( i=0; i<${#commandsToExecute[@]}; i++ )); do
    echo -e "executing: ${GREEN}${commandsToExecute[$i]}${NC}"
    eval ${commandsToExecute[$i]}
done
