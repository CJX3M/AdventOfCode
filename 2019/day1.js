const input = ``.split('\n').map(v => Number.parseInt(v));

const calculateModule = (mass) => {
    return Math.floor(mass / 3) - 2;
}

const calculateModule2 = (mass) => {
    let currentMass = Math.floor(mass / 3) - 2
    if (currentMass > 0)
        return currentMass + calculateModule2(currentMass);
    currentMass = 0;
    return currentMass;
}

console.log(`For a mass of 12 the module is ${calculateModule(12)}`)
console.log(`For a mass of 14 the module is ${calculateModule(14)}`)
console.log(`For a mass of 1969 the module is ${calculateModule(1969)}`)
console.log(`For a mass of 100756 the module is ${calculateModule(100756)}`)

console.log(`1-1 answer:`, input.reduce((total, mass) => total + calculateModule(mass), 0));

console.log(`For a total mass of 12 the module is ${calculateModule2(12)}`)
console.log(`For a total mass of 14 the module is ${calculateModule2(14)}`)
console.log(`For a total mass of 1969 the module is ${calculateModule2(1969)}`)
console.log(`For a total mass of 100756 the module is ${calculateModule2(100756)}`)

console.log(`1-2 answer:`, input.reduce((total, mass) => total + calculateModule2(mass), 0));
//
