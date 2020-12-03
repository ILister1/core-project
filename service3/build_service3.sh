#!/bin/bash

# this script builds the image for Service 3.

sudo docker build -t service3 .
sudo docker run -d -p 5002:5002 --name service3 service3