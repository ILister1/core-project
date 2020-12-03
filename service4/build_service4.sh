#!/bin/bash

# this script builds the image for Service 4.

sudo docker build -t service4 .
sudo docker run -d -p 5003:5003 --name service4 service4