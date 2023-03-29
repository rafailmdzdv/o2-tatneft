import pathlib

from pydantic import BaseSettings


class Env(BaseSettings):

    SECOND_SECRET_TOKEN: str | None
    THIRD_SECRET_TOKEN: str | None

    class Config:
        env_file = f'{pathlib.Path(__file__).resolve().parent.parent}/.env'


env = Env()
