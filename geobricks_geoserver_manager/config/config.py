import logging

config = {
    # To be used by Flask: DEVELOPMENT ONLY
    "debug": True,

    # Flask host: DEVELOPMENT ONLY
    "host": "localhost",

    # Flask port: DEVELOPMENT ONLY
    "port": 5903,

    # Logging configurations
    "logging": {
        "level": logging.INFO,
        "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
        "datefmt": "%d-%m-%Y | %H:%M:%s"
    },
}
