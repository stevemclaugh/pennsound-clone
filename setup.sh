#!/bin/bash

python /home/load_metadata_db.py

#gunicorn --workers 10 --bind 0.0.0.0:80 wsgi
