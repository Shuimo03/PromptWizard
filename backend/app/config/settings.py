
from pydantic import BaseModel
import yaml
from pathlib import Path

class DifyConfig(BaseModel):
    api_key: str
    base_url: str

class AppConfig(BaseModel):
    dify: DifyConfig

class ConfigManager:
    _instance = None
    _config: AppConfig = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._config is None:
            self.load_config()

    def load_config(self, env: str = "development"):
        config_path = Path("config") / f"{env}.yaml"
        with open(config_path, "r") as f:
            config_data = yaml.safe_load(f)
            self._config = AppConfig(**config_data)

    @property
    def dify(self) -> DifyConfig:
        return self._config.dify