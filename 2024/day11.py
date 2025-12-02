from openData import getData
from copy import deepcopy
from functools import cache

@cache
def applyAction(stone):
    if stone == 0:
        return 1
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        midIndex = len(stone) // 2
        return [int(stone[:midIndex]), (int(stone[midIndex:]))]
    else:
        return stone * 2024

@cache
def performBlinks(stone, blinks):
    splits = 0
    blink = 0
    while blink < blinks:
        stone = applyAction(stone)
        if isinstance(stone, list):
            splits += 1
            stone1 = stone[1]
            stone = stone[0]
            splits += performBlinks(stone1, blinks-blink-1)
        blink += 1
    return splits

if __name__ == "__main__":

    input = [int(n) for n in getData("11", False)[0].split(' ')]

    stones = 0

    for stone in input:
        stones += performBlinks(stone, 25)

    print("Result part 1:", stones + len(input))

    stones = 0

    for stone in input:
        stones += performBlinks(stone, 75)

    print("Result part 2: ", stones + len(input))



