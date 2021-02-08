#!/bin/bash

cp dashboard-analytics.service /etc/systemd/system/.
systemctl daemon-reload
systemctl start dashboard-analytics
systemctl enable dashboard-analytics
