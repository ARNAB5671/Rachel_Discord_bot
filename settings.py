import pathlib
import os

import logging
from dotenv import load_dotenv
from logging.config import dictConfig


load_dotenv()
DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
BASE_DIR= pathlib.Path(__file__).parent
CMNDS_DIR=BASE_DIR/"cmnds"
COGS_DIR=BASE_DIR/"cogs"


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s: %(message)s"
        },
        "standard": {
            "format": "%(levelname)-8s %(name)-15s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            'level': "DEBUG",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "console2": {
            'level': "WARNING",
            'class': "logging.StreamHandler",
            'formatter': "standard"
        },
        "file": {
            'level': "INFO",
            'class': "logging.FileHandler",
            'formatter': "standard",
            'filename': "logs/info.log",
            'mode': "w",
            'formatter': "verbose"
        }
    },
    "loggers": {
        "bot": {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        "discord": {
            'handlers': ['console2', "file"],
            'level': "INFO",
            'propagate': False
        }
    }
}

dictConfig(LOGGING_CONFIG)
