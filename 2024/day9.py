from openData import getData
from itertools import chain

if __name__ == "__main__":

    # input = getData("day9InputTestSmall.txt")
    input = getData("day9Input.txt")
    # input = getData("testData.txt")
    memBlocks = list(input[0])

    filesBlocks = memBlocks[::2]
    freeBlocks = memBlocks[1::2]

    files = ""

    for index, file in enumerate(filesBlocks):
        files += (str(index)+',') * int(file)

    files = files.split(',')[:-1]

    block = []

    for a, b in zip(filesBlocks, freeBlocks):
        for indexFiles in range(int(a)):
            if files:
                block.append(files.pop(0))
            else:
                break
        for freeSpace in range(int(b)):
            if files:
                block.append(files.pop())
            else:
                break
    
    while files:
        block.append(files.pop(0))

    checkSum = sum([index * int(mem) for index, mem in enumerate(block)])

    print("Result Part 1: ", checkSum)

    currentIndex = 0

    blocks = []

    freeMemory = False

    for number in input[0]:
        if number != '0':
             blocks.append(['.' if freeMemory else str(currentIndex) for a in range(int(number))])
        if not freeMemory:
            currentIndex += 1
        freeMemory = not freeMemory    

    for block in blocks[::-1]:
        if '.' in block:
            continue
        foundBlockIndex = blocks.index(block)
        emptyBlocks = [b for b in blocks if '.' in b and b.count('.') >= len(block)]
        if emptyBlocks:
            emptyBlockIndex = blocks.index(emptyBlocks[0])
            if foundBlockIndex < emptyBlockIndex:
                continue
            emptyStartIndex = emptyBlocks[0].index('.')
            for i in range(len(block)):
                emptyBlocks[0][i+emptyStartIndex] = block[i]
                block[i] = '.'

    checkSum = 0

    blocks = list(chain.from_iterable(blocks))

    for index, number in enumerate(blocks):
        if number.isdigit():
            checkSum += int(number) * index
    
    print("Result Part 2: ", checkSum)