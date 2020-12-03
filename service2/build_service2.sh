#!/bin/bash

# this script builds the image for Service 2.

sudo docker build -t service2 .
sudo docker run -d -p 5001:5001 --name service2 service2