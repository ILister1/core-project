#!/bin/bash

cd service1 && . teardown_service1.sh
cd .. && cd service2 && . teardown_service2.sh
cd .. && cd service3 && . teardown_service3.sh
cd .. && cd service4 && . teardown_service4.sh