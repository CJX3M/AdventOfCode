from openData import getData
from copy import deepcopy

def performBlinks(input, blinks):
    stones = []
    blink = 1
    while blink <= blinks:
        print(f"\rBlink {blink}", end="")
        blink += 1
        if len(stones) > 0:
            input = deepcopy(stones)
            stones = []
        for stone in input:
            if stone == "0":
                stones.append("1")
            elif len(stone) % 2 == 0:
                midIndex = len(stone) // 2
                stones.append(str(int(stone[:midIndex])))
                stones.append(str(int(stone[midIndex:])))
            else:
                stones.append(str(int(stone) * 2024))
    return stones

if __name__ == "__main__":

    input = getData("day11", False)[0].split(' ')

    stones = performBlinks(input, 25)

    print("Result part 1:", len(stones))

    stones = performBlinks(stones, 50)

    print("Result part 2: ", len(stones))



