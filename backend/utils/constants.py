# Imports
from __future__ import annotations
from typing import Final, Literal
from .enums import HSRElement, Language, HSRPath

__all__ = ("HSR_CHARACTER_RARITY_MAP", "HSR_PATH_NAMES", "HSR_ELEMENT_NAMES")

HSR_PLAYER_NAMES: Final[dict[Language, str]] = {
    Language.EN: "Trailblazer",
    Language.JA: "開拓者",
    Language.ZH: "开拓者",
    Language.KO: "개척자",
}

HSR_CHARACTER_RARITY_MAP: Final[dict[str, Literal[4, 5]]] = {
    "CombatPowerAvatarRarityType4": 4,
    "CombatPowerAvatarRarityType5": 5,
}

HSR_PATH_NAMES: Final[dict[Language, dict[HSRPath, str]]] = {
    Language.EN: {
        HSRPath.ABUNDANCE: "Abundance",
        HSRPath.DESTRUCTION: "Destruction",
        HSRPath.ERUDITION: "Erudition",
        HSRPath.HARMONY: "Harmony",
        HSRPath.NIHILITY: "Nihility",
        HSRPath.PRESERVATION: "Preservation",
        HSRPath.THE_HUNT: "The Hunt",
        HSRPath.REMEMBRANCE: "Remembrance",
    },
    Language.JA: {
        HSRPath.ABUNDANCE: "豊穣",
        HSRPath.DESTRUCTION: "壊滅",
        HSRPath.ERUDITION: "知恵",
        HSRPath.HARMONY: "調和",
        HSRPath.NIHILITY: "虚無",
        HSRPath.PRESERVATION: "存護",
        HSRPath.THE_HUNT: "巡狩",
        HSRPath.REMEMBRANCE: "記憶",
    },
    Language.ZH: {
        HSRPath.ABUNDANCE: "丰饶",
        HSRPath.DESTRUCTION: "毁灭",
        HSRPath.ERUDITION: "智识",
        HSRPath.HARMONY: "同谐",
        HSRPath.NIHILITY: "虚无",
        HSRPath.PRESERVATION: "存护",
        HSRPath.THE_HUNT: "巡猎",
        HSRPath.REMEMBRANCE: "记忆",
    },
    Language.KO: {
        HSRPath.ABUNDANCE: "풍요",
        HSRPath.DESTRUCTION: "파멸",
        HSRPath.ERUDITION: "지식",
        HSRPath.HARMONY: "화합",
        HSRPath.NIHILITY: "공허",
        HSRPath.PRESERVATION: "보존",
        HSRPath.THE_HUNT: "수렵",
        HSRPath.REMEMBRANCE: "기억",
    },
}

HSR_ELEMENT_NAMES: Final[dict[Language, dict[HSRElement, str]]] = {
    Language.EN: {
        HSRElement.PHYSICAL: "Physical",
        HSRElement.FIRE: "Fire",
        HSRElement.ICE: "Ice",
        HSRElement.LIGHTNING: "Lightning",
        HSRElement.WIND: "Wind",
        HSRElement.QUANTUM: "Quantum",
        HSRElement.IMAGINARY: "Imaginary",
    },
    Language.JA: {
        HSRElement.PHYSICAL: "物理",
        HSRElement.FIRE: "火",
        HSRElement.ICE: "氷",
        HSRElement.LIGHTNING: "雷",
        HSRElement.WIND: "風",
        HSRElement.QUANTUM: "量子",
        HSRElement.IMAGINARY: "想象",
    },
    Language.ZH: {
        HSRElement.PHYSICAL: "物理",
        HSRElement.FIRE: "火",
        HSRElement.ICE: "冰",
        HSRElement.LIGHTNING: "雷电",
        HSRElement.WIND: "风",
        HSRElement.QUANTUM: "量子",
        HSRElement.IMAGINARY: "想象",
    },
    Language.KO: {
        HSRElement.PHYSICAL: "물리",
        HSRElement.FIRE: "불",
        HSRElement.ICE: "얼음",
        HSRElement.LIGHTNING: "번개",
        HSRElement.WIND: "바람",
        HSRElement.QUANTUM: "양자",
        HSRElement.IMAGINARY: "상상",
    },
}
