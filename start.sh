#!/bin/sh
echo Starting rabbit
sleep 15
nameko run --config config.yml ilumination_server
