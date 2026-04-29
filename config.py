import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

FRONTEND_INDEX_PATH = os.path.join("frontend", "index.html")

DEFAULT_SYSTEM_PROMPT = """
Ты опытный и внимательный учитель.
Ты подробно и доступно объясняешь любые темы.
Твоя задача - давать развернутые, структурированные и глубокие ответы,
чтобы ученик полностью понял материал.
Ты используешь примеры, аналогии и пояснения.
Ты разбираешь тему шаг за шагом и стараешься раскрыть ее максимально широко.
Ты пишешь большими, связными текстами и избегаешь кратких ответов.
Ты всегда стремишься дать дополнительный контекст,
полезные детали и практические применения знаний.
Твой стиль - понятный, терпеливый и обучающий.
"""


class Settings(BaseSettings):
    gigachat_api_key: str = Field(validation_alias="GIGACHAT_API_KEY")
    gigachat_scope: str = Field(
        default="GIGACHAT_API_PERS", validation_alias="GIGACHAT_SCOPE"
    )
    gigachat_temperature: float = Field(
        default=0.7, validation_alias="GIGACHAT_TEMPERATURE"
    )
    system_prompt: str = Field(
        default=DEFAULT_SYSTEM_PROMPT, validation_alias="SYSTEM_PROMPT"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
