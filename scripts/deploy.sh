#!/bin/bash
sudo docker swarm init
sudo docker stack deploy --compose-file docker-compose.yaml core-project