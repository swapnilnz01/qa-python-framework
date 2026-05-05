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
        config = cls._load()
        # configparser needs a section — we use DEFAULT
        return config.defaults().get(key.lower(), fallback)

    @classmethod
    def get_base_url(cls):
        return cls.get("base_url")

    @classmethod
    def get_ui_base_url(cls):
        return cls.get("ui_base_url")

    @classmethod
    def get_browser(cls):
        return cls.get("browser", "chromium")

    @classmethod
    def is_headless(cls):
        return cls.get("headless", "true").lower() == "true"

    @classmethod
    def get_timeout(cls):
        return int(cls.get("timeout", "30000"))

    @classmethod
    def get_environment(cls):
        return cls.get("environment", "staging")