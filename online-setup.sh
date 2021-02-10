#!/bin/bash

sudo apt-get update
sudo apt-get install -y gcc make build-essential python-dev git scons swig python3 idle3 python3-pip

git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
sudo scons
cd python
sudo python3 setup.py build 
sudo python3 setup.py install 
sudo pip3 install adafruit-circuitpython-neopixel
sudo pip3 uninstall rpi_ws281x
sudo pip3 install rpi_ws281x

sudo pip3 install pynetworktables2js
