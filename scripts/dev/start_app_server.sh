#!/bin/bash

. /Users/mishankov/Documents/Git/mishankov.io/scripts/dev/output_style.config

. /Users/mishankov/Documents/Git/mishankov.io/scripts/dev/app_server.config

echo LOGGING_LEVEL

echo -e "${Info}Set working directory ${Reset}"
cd /Users/mishankov/Documents/Git/mishankov.io/source

echo -e "${Info}Set LOGGING_LEVEL for dlogging to DEBUG${Reset}"
export LOGGING_LEVEL

echo -e "${Info}Create the virtual environment${Reset}"
python3 -m venv venv

echo -e "${Info}Activate the virtual environment${Reset}"
. venv/bin/activate

echo -e "${Info}Install or update python modules${Reset}"
pip3 install --upgrade -r requirements.txt

echo -e "${Info}Get latest dlogging module from git${Reset}"
cd utils/
rm -rf dlogging
git clone https://github.com/mishankov/dlogging.git
cd ../

echo -e "${Info}Initialize data base ${Link}${DB_PATH}${ResetLink}${Reset}"
export DB_PATH
python3 utils/init_db.py

echo -e "${Info}Start ${Link}utils/data_agent.py${ResetLink} in background and save its PID to ${Link}data_agent_pid.txt${Reset}"
nohup python3 utils/data_agent.py > LOGS/data_agent_nohup.log>&1 &
echo $! > data_agent_pid.txt

echo -e "${Start}Start application server at ${Link}http://${APP_HOST}:${APP_PORT}${ResetLink} with ${APP_WORKERS} workers${Reset}"
gunicorn -b $APP_HOST:$APP_PORT -w=$APP_WORKERS wsgi:app

echo -e "${Info}Kill ${Link}utils/data_agent.py${ResetLink} background process and delete ${Link}data_agent_pid.txt${Reset}"
kill -9 `cat data_agent_pid.txt`
rm data_agent_pid.txt

echo -e "${Info}Deactivate the virtual environment${Reset}"
deactivate

echo -e "${Stop}Application server stopped${Reset}"