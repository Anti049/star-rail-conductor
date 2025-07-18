type CharacterDetails = {
    id: number;
    name: string;
    description: string;
    rarity: 4 | 5;
    path: Path;
    element: Element;
}

type Details = {
    id: number;
    name: string;
    description: string;
    parameters?: number[];
}

type Eidolon = Details & {
    rank: number;
    extras: Details[];
}

type Skill = Details & {
    simpleDescription: string;
    type: string;
    tag: string;
    energyRegen: number;
    levels: {
        level: number;
        parameters: number[];
    }[];
}
