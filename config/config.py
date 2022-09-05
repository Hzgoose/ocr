# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

path = os.getcwd()
load_dotenv(dotenv_path=str(path)+'/.env', verbose=True)

config_service = {
    "host": os.getenv('HOST_SERVICE'),
    "port": os.getenv('PORT_SERVICE'),
    "debug": os.getenv('DEBUG_SERVICE'),
    "workers": os.getenv('WORKERS_SERVICE')
}

config_file = {
    "path_file": os.getenv("PATH_FILE")
}