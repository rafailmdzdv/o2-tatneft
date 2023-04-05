import pathlib

from pydantic import BaseSettings


class Env(BaseSettings):

    SECOND_SECRET_TOKEN: str | None
    THIRD_SECRET_TOKEN: str | None
    LK_TATNEFT_LOGIN: str | None
    LK_TATNEFT_PASSWORD: str | None
    EMAIL_HOST_USER: str | None
    EMAIL_HOST_PASSWORD: str | None

    class Config:
        env_file = f'{pathlib.Path(__file__).resolve().parent.parent}/.env'


env = Env()
