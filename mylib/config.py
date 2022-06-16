"""Config functionality"""
# mylib/config.py

import configparser
from pathlib import Path

import typer

__app_name__ = "mytodo"
__version__ = "0.1.1"


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def init_app() -> int:
    """ Initialize the config file"""
    
    config_code = _init_config_file()
    if config_code != SUCCESS
        return config_code
    return SUCCESS


