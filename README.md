# aero
## for run:
1) {PATH_TO_PYTHON3.9>=} -m venv venv
2) pip3 install -r requirements.txt
3) docker-compose up -d
4) venv/bin/python main.py

## crontab settings:
1) add {PATH_TO_PYTHON3.9>=} to crontab file instead of {PATH_TO_PYTHON3.9<=}
2) cat crontab | crontab && crontab -l
