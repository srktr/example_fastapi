from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Setting(BaseSettings):
   # model_config = ConfigDict(env_file = ".env")

    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algrithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Setting()