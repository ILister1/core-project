#!/bin/bash

docker build -t testing-img -f testing/Dockerfile .
docker run -it -d --name testing-cont testing-img

docker exec testing-cont pytest ./service1 --cov ./service1
docker exec testing-cont pytest ./service2 --cov ./service2
docker exec testing-cont pytest ./service3 --cov ./service3
docker exec testing-cont pytest ./service4 --cov ./service4

docker stop testing-cont
docker rm testing-cont
