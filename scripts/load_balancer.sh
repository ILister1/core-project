#!bin/bash
  
sudo docker run -d -p 80:80 --name nginx --mount type=bind,source=$(pwd)/nginx/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine