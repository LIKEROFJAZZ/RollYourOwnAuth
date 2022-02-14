#!/bin/bash
service nginx start
python3 flask_api.py
while true; do sleep 1d; done
