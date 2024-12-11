from openData import getData

def divideArray(arr):
    array1 = []
    array2 = []

    for index, number in enumerate(arr):
        if index % 2 == 0:
            array1.append(number)
        else:
            array2.append(number)

    return (array1, array2)

if __name__ == "__main__":

    input = list(getData("day9InputTestSmall.txt")[0])
    #input = list(getData("day9Input.txt")[0])

    (filesBlocks, freeBlocks) = divideArray(input)

    files = ''

    for index, file in enumerate(filesBlocks):
        files += str(index) * int(file)

    files = list(files)

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

    # freeMemory = False

    # block = ''

    # currentIndex = 0

    # for number in input:        
    #     block += ('.' if freeMemory else str(currentIndex)) * int(number)
    #     if not freeMemory:
    #         currentIndex += 1
    #     freeMemory = not freeMemory
    
    # block = list(block)

    # currentIndex = 0

    # for index, mem in enumerate(block):
    #     if not any([c.isdigit() for c in block[index:-1]]):
    #         break
    #     if mem == '.':
    #         lastCurrentPosition = block[-1-currentIndex]
    #         while lastCurrentPosition == '.':
    #             currentIndex += 1
    #             lastCurrentPosition = block[-1-currentIndex]
    #         block[index] = lastCurrentPosition
    #         block[-1-currentIndex] = '.'
    #         currentIndex += 1
    
    checkSum = 0

    for index, mem in enumerate(block):
        checkSum += index * int(mem)

    print("Result: ", checkSum)