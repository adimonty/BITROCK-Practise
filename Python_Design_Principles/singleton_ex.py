import json
from threading import Lock

class ConfigManager:

    _instance = None
    _lock = Lock()

    def __init__(self):
        if not ConfigManager._instance:
            print("Initializing configuration...")
            ConfigManager._instance = self
            self.configs = {}
            self.load_config()
        else:
            raise Exception("Cannot instantiate second singleton class.")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = ConfigManager()
        return cls._instance

    def get_config(self, key):
        return self.configs.get(key)

    def set_config(self, key, value):
        self.configs[key] = value
        self.save_config()

    def load_config(self):
        try:
            with open('config.json') as f:
                self.configs = json.load(f)
        except FileNotFoundError:
            print("Config file not found, starting with empty config")

    def save_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.configs, f)

# Usage
config = ConfigManager.get_instance()
config.set_config("language", "English")
print(config.get_config("language")) # English