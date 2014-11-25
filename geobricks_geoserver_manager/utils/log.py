import logging
import inspect
# from pgeo.config.settings import settings

settings = {
    # Logging configurations
    "logging": {
        "level": logging.INFO,
        "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
        "datefmt": "%d-%m-%Y | %H:%M:%s"
    }
}


level = settings["logging"]["level"]
format = settings["logging"]["format"]
datefmt = settings["logging"]["datefmt"]
logging.basicConfig(level=level, format=format, datefmt=datefmt)


def logger(loggerName=None):
    logger = logging.getLogger(loggerName)
    logger.setLevel(level)
    return logger