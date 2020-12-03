#!/bin/bash

cd service1 && . build_service1.sh
cd .. && cd service2 && . build_service2.sh
cd .. && cd service3 && . build_service3.sh
cd .. && cd service4 && . build_service4.sh