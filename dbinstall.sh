#! /bin/bash
sudo apt-get -y install python-psycopg2 postgresql
sudo -u postgres dropdb compusoft
sudo -u postgres dropuser compusoft
sudo -u postgres createuser -PE -s compusoft
sudo -u postgres createdb -O compusoft -E UTF8 compusoft

psql -f loaddb.sql compusoft