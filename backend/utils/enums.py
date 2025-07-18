# Imports
from enum import StrEnum


class Language(StrEnum):
    """
    Enum representing the languages supported in Honkai: Star Rail.
    """

    EN = "en"
    JA = "ja"
    ZH = "zh"
    KO = "ko"


class HSRPath(StrEnum):
    """
    Enum representing the paths in Honkai: Star Rail.
    """

    ABUNDANCE = "Priest"
    DESTRUCTION = "Warrior"
    ERUDITION = "Mage"
    HARMONY = "Shaman"
    NIHILITY = "Warlock"
    PRESERVATION = "Knight"
    REMEMBRANCE = "Memory"
    THE_HUNT = "Rogue"


class HSRElement(StrEnum):
    """
    Enum representing the elements in Honkai: Star Rail.
    """

    PHYSICAL = "Physical"
    FIRE = "Fire"
    ICE = "Ice"
    LIGHTNING = "Thunder"
    WIND = "Wind"
    QUANTUM = "Quantum"
    IMAGINARY = "Imaginary"
