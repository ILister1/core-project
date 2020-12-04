#!/bin/bash

ssh swarm-manager << EOF

cd core-project
git pull
sudo docker stack deploy --compose-file docker-compose.yaml core-project

EOF