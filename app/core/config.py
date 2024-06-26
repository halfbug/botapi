from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    API_V1_ROUTE: Optional[str] = None
    ENV_STATE: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    LOG_FILE: Optional[str] = None
    LOGTAIL_API_KEY: Optional[str] = None
    MAILGUN_API_KEY: Optional[str] = None
    MAILGUN_DOMAIN: Optional[str] = None
    GOO_API_KEY_ID: Optional[str] = None
    GOO_BUCKET_NAME: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    GOOGLE_CSE_ID: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None
    SENTRY_DSN: Optional[str] = None


class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict()  # env_prefix="DEV_"


class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="PROD_")


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True
    JWT_SECRET_KEY: str = (
        "4598398cca0a7ecb7c7466fb30e43d4525bb3f5c59974183c8f46724e63ccee7"
    )
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(env_prefix="TEST_")


# @lru_cache()
def get_config(env_state: str):
    # print(env_state)
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()


# print(f"{Path(__file__).parent.parent.parent}\.env")
# print(os.path.expanduser("~/.env"))
# print(GlobalConfig().DATABASE_URL)
# print(BaseConfig().ENV_STATE)
# print(get_config(BaseConfig()))
config = get_config(BaseConfig().ENV_STATE)
