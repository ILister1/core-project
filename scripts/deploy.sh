#!/bin/bash
sudo docker swarm init
git pull
sudo docker stack deploy --compose-file docker-compose.yaml core-project