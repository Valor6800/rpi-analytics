#!/bin/bash

cp led-controller.service /etc/systemd/system/.
systemctl daemon-reload
systemctl start led-controller
systemctl enable led-controller
