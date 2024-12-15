let input = ''

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
//
