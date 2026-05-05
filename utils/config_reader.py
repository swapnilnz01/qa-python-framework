import configparser
import os

class ConfigReader:
    _config = None

    @classmethod
    def _load(cls):
        if cls._config is None:
            cls._config = configparser.RawConfigParser()
            config_path = os.path.join(
                os.path.dirname(__file__), '..', 'config.properties'
            )
            cls._config.read(config_path)
        return cls._config

    @classmethod
    def get(cls, key, fallback=None):
        return cls._load().get("settings", key.lower(), fallback=fallback)