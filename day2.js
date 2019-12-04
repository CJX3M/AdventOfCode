let input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0'

let intCode = input => {
    let currentIndex = 0;

    while (input[currentIndex] !== 99) {
        const instruction = input[currentIndex];
        const int1 = Number.parseInt(input[input[currentIndex+1]]), 
            int2 = Number.parseInt(input[input[currentIndex+2]]),
            resPos = Number.parseInt(input[currentIndex+3]);
        switch (instruction) {
            case 1:
                input[resPos] = int1 + int2;
                break;
            case 2:
                input[resPos] = int1 * int2;
                break;
            default:
                break;
        }
        currentIndex += 4;
    }

    return input;
}

let convertToIntArray = string => string.split(',').map(v => Number.parseInt(v));

let testInput = convertToIntArray("1,9,10,3,2,3,11,0,99,30,40,50");
console.log(`for ${testInput} the result it ${intCode(testInput)}`);
console.log(`for 1,0,0,0,99 the result it ${intCode(convertToIntArray('1,0,0,0,99'))}`);
console.log(`for 2,3,0,3,99 the result it ${intCode(convertToIntArray('2,3,0,3,99'))}`);
console.log(`for 2,4,4,5,99,0 the result it ${intCode(convertToIntArray('2,4,4,5,99,0'))}`);
console.log(`for 1,1,1,4,99,5,6,0,99 the result it ${intCode(convertToIntArray('1,1,1,4,99,5,6,0,99'))}`);

let inputPart1 = convertToIntArray(input);
inputPart1[1] = 12;
inputPart1[2] = 2;

console.log(`2-1 answer: ${intCode(convertToIntArray(input))[0]}`);

let inputPart2 = convertToIntArray(input), noun = 0, verb = 0;

while (true) {
    inputPart2[1] = noun;
    inputPart2[2] = verb;
    inputPart2 = intCode(inputPart2);

    console.log(`With noun ${noun} and verb ${verb} the output is ${inputPart2[0]}`);

    if (inputPart2[0] === 19690720)
        break;
    
    inputPart2 = convertToIntArray(input);

    noun++;
    if (noun === 101) {
        verb++;
        noun = 0;
    }
}

console.log(`2-2 answer: ${noun}${verb}`);
