# Tutorial

## Setup env

- Create instance `multipass launch -m 5G -n airflow-tut`
- Log into `multipass shell airflow-tut`
- Add ssh your key `vim ~/.ssh/authorized_keys` 
- `sudo apt update`
- `sudo apt-get install python3-venv`
- `python3 -m venv sandbox`
- Open sandbox env in python `source sandbox/bin/activate`
- `pip install wheel`
- `sudo apt install sqlite3`
- `sudo apt-get install gcc python3-dev`
- `pip install apache-airflow==2.0.0 --constraint https://gist.githubusercontent.com/marclamberti/742efaef5b2d94f44666b0aec020be7c/raw/5da51f9fe99266562723fdfb3e11d3b6ac727711/constraint.txt`
- `pip install apache-airflow-providers-http`
- Create db, init always wipe old db `airflow db init`
- Create basic user `airflow users create -u admin -p password -l admin -f admin -e admin@airflow.com -r Admin`
- Start webserver `airflow webserver -D`
- Start scheduler `airflow scheduler`

## port forwarding

`ssh airflow_udemy -L 8080:localhost:8080`

## Kill processes to be able to restart webserver

`killall -9 airflow`

## Panel

Add sqlite connection in panel

- Go to admin => connection
- Add new connection  db_sqlite + ${pwd}/airflow.db

## Test changes

- `airflow tasks test user_processing creating_table 2020-01-01`


## Use Postgres

- `sudo apt install postgres`
- `sudo -u postgres psql`
- `ALTER USER postgres PASSWORD 'postgres';`
- `\q`
- `pip install 'apache-airflow[postgres]'`
- Update executor and sql_alchemy_conn
- Stop webserver  
- `airflow db init`
- `airflow users create -u admin -p password -l admin -f admin -e admin@airflow.com -r Admin`
- Start airflow

# Queue

- `pip install 'apache-airflow[celery]'`
- `sudo apt install redis`
- Change supervised to systemd `sudo vim /etc/redis/redis.conf`
- `sudo systemctl redis.service`
