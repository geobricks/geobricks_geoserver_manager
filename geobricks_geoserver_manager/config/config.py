import logging

config = {

    "settings": {

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

        # geoserver settings
        "geoserver": {
            "geoserver_slaves": ["http://localhost:3330/geoserver/rest"],
            "geoserver_master": "http://localhost:3333/geoserver/rest",
            "username": "admin",
            "password": "geoserver",
        }
    }
}
