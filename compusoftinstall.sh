#! /bin/bash

# Install database
sh ./dbinstall.sh

# Build database
python3 manage.py migrate
python3 manage.py makemigrations

# Load initial information
psql -f loaddb.sql compusoft

# Register cs students
python3 ./loadstudents.py