# Imports
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator
from typing import Literal, Optional, List, Dict, Any

from utils.enums import HSRElement, HSRPath, Language
from utils.constants import HSR_CHARACTER_RARITY_MAP, HSR_PLAYER_NAMES


class Character(BaseModel):
    """
    Represents a character in Honkai: Star Rail.
    """

    id: int = Field(..., description="Unique identifier for the character")
    names: dict[Literal["en", "cn", "kr", "jp"], str]
    description: str = Field(alias="desc", description="Description of the character")
    rarity: Literal[4, 5] = Field(
        alias="rank", description="Rarity of the character (4/5 stars)"
    )
    element: HSRElement = Field(
        alias="damageType", description="Element type of the character"
    )
    path: HSRPath = Field(alias="baseType", description="Path type of the character")

    @computed_field
    @property
    def name(self, lang: Language = Language.EN) -> str:
        value = self.names.get(lang, "")
        if value == "{NICKNAME}":
            value = HSR_PLAYER_NAMES.get(lang, "")
        return value

    @computed_field
    @property
    def image(self) -> str:
        return f"https://api.hakush.in/hsr/UI/avatarshopicon/{self.id}.webp"

    @field_validator("rarity", mode="before")
    @classmethod
    def __convert_rarity(cls, value: str) -> Literal[4, 5]:
        return HSR_CHARACTER_RARITY_MAP[value]

    @field_validator("description", mode="before")
    @classmethod
    def __convert_description(cls, value: str | None) -> str:
        return value or ""

    @model_validator(mode="before")
    @classmethod
    def __transform_names(cls, values: dict[str, Any]) -> dict[str, Any]:
        # This is probably the most questionable API design decision I've ever seen.
        values["names"] = {
            "en": values.pop("en"),
            "cn": values.pop("cn"),
            "kr": values.pop("kr"),
            "jp": values.pop("jp"),
        }
        return values
