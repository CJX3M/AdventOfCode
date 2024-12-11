from openData import getData

if __name__ == "__main__":

    # input = getData("day9InputTestSmall.txt")
    input = getData("day9Input.txt")
    # input = getData("testData.txt")
    memBlocks = list(input[0])

    filesBlocks = memBlocks[::2]
    freeBlocks = memBlocks[1::2]

    files = ""

    for index, file in enumerate(filesBlocks):
        # for i in range(int(file)):
        #     files.append(index)
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

    print("Result: ", checkSum)