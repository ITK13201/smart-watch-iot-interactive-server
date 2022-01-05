import os
import pathlib
from logging import config

API_SERVER_BASE_URL = os.environ["API_SERVER_BASE_URL"]
API_USER_USERNAME = os.environ["API_USER_USERNAME"]
API_USER_PASSWORD = os.environ["API_USER_PASSWORD"]
DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# ===

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "log")
LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
    if not os.path.isfile(LOG_FILE_PATH):
        logfile = pathlib.Path(LOG_FILE_PATH)
        logfile.touch()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s] %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
        },
        "myformat": {
            "format": "[%(levelname)s] %(asctime)s %(name)s:%(lineno)s %(funcName)s %(module)s %(process)d %(thread)d:  %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "myformat",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "myformat",
            "filename": "log/app.log",
        },
    },
    "loggers": {
        "__main__": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
    },
}
config.dictConfig(LOGGING)
