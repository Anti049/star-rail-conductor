interface Path {
    name: string;
    internalName: string;
}

const paths: Path[] = [
    { name: "Abundance", internalName: "Priest" },
    { name: "Destruction", internalName: "Warrior" },
    { name: "Erudition", internalName: "Mage" },
    { name: "Harmony", internalName: "Shaman" },
    { name: "Nihility", internalName: "Warlock" },
    { name: "Preservation", internalName: "Knight" },
    { name: "Remembrance", internalName: "Memory" },
    { name: "The Hunt", internalName: "Rogue" }
];

interface Element {
    name: string;
    internalName: string;
}

const elements: Element[] = [
    { name: "Physical", internalName: "Physical" },
    { name: "Fire", internalName: "Fire" },
    { name: "Ice", internalName: "Ice" },
    { name: "Lightning", internalName: "Thunder" },
    { name: "Wind", internalName: "Wind" },
    { name: "Quantum", internalName: "Quantum" },
    { name: "Imaginary", internalName: "Imaginary" }
];
