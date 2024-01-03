from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    bot_token: SecretStr
    db_url: PostgresDsn
    payments_token: SecretStr
    support_chat: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = BotSettings()
