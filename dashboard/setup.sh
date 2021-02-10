#!/bin/bash

cp dashboard.service /etc/systemd/system/.
systemctl daemon-reload
systemctl start dashboard
systemctl enable dashboard
