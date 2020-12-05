#!/bin/bash

ssh swarm-manager << EOF

cd core-project
git pull
sudo docker stack deploy --compose-file docker-compose.yaml core-project

EOF

ssh nginx-lb << EOF

cd core-project
git pull
sudo docker stop nginx
sudo docker rm nginx
sudo docker rmi nginx:alpine
. scripts/load_balancer.sh

#EOF