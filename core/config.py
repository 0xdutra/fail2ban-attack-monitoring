from configparser import ConfigParser

def load_config_file():
    config_object = ConfigParser()
    config_object.read("config.ini")

    return config_object
