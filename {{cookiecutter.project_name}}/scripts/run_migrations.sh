#! /bin/bash

python3 src/manage.py db init
python3 src/manage.py db migrate -m "Initial migration."
python3 src/manage.py db upgrade
