#!/bin/bash

cd /home/pi/rpi-analytics/dashboard
python3 -m pynetworktables2js --team 6800 -p 8080
