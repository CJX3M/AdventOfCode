from openData import getData
from time import sleep
from os import system
from copy import deepcopy

def printMap(map: list[list], step: int, nextMove) -> None:
    clear_console()
    print("Step: ", step)
    print("Next Move: ", nextMove)
    for row in map:
        print("".join(row))
    print()
    #sleep(0.1)

def clear_console():
    system('clear')

def moveRobot(map: list[list], movement: list, part2: bool = False) -> None:

    currentPosition = tuple((px, py)
                        for px, r in enumerate(map) 
                        for py, char in enumerate(r) if char == "@")[0]
    step = 0
    nextMove = ''
    while movement:        
        nextMove = movement.pop(0)
        direction = directions[nextMove]
        nextPosition = [a+b for a, b in zip(currentPosition, direction)]
        nextChar = map[nextPosition[0]][nextPosition[1]]
        printMap(map, step, nextMove)
        step += 1
        if '.' in nextChar:
            updateMap("@", currentPosition, nextPosition, map)
            currentPosition = nextPosition
            continue
        if part2:
            if nextMove == '>':                
                nextChar = map[nextPosition[0]][nextPosition[1]] + map[nextPosition[0]][nextPosition[1]+1]
            elif nextMove == '<':
                nextChar = map[nextPosition[0]][nextPosition[1]-1] + nextChar
            if nextMove == '^' or nextMove == 'v':
                if nextChar == '[':                    
                    nextChar += map[nextPosition[0]][nextPosition[1]+1]
                elif nextChar == ']':
                    nextChar = map[nextPosition[0]][nextPosition[1]-1] + nextChar
        if nextChar == '#' or nextChar == '##':
            continue
        elif nextChar == 'O' or nextChar == '[]':
            if canMoveObstacle(nextPosition, map, direction):
                updateMap("@", currentPosition, nextPosition, map)
                currentPosition = nextPosition
    printMap(map, step, nextMove)

    return map

def canMoveObstacle(currentPosition: list, map: list[list], direction: list, part2: bool = False):
    nextPosition = [a+b for a, b in zip(currentPosition, direction)]
    currentChar = map[currentPosition[0]][currentPosition[1]]
    canMove = False    
    if currentChar == '.':
        canMove = True
    elif currentChar == 'O':
        nextChar = map[nextPosition[0]][nextPosition[1]]
        if nextChar == 'O':
            if canMoveObstacle(nextPosition, map, direction):
                updateMap('O', currentPosition, nextPosition, map)
                canMove = True
            else:
                canMove = False    
        elif nextChar == '.':
            updateMap('O', currentPosition, nextPosition, map)
            canMove = True
        elif nextChar == '#':
            canMove = False
    else:
        # move left or right
        if direction[0] == 0:
            if currentChar == ']':
                nextPosition = [nextPosition[0], nextPosition[1]-1]
                if canMoveObstacle(nextPosition, map, direction):
                    updateMap("[", currentPosition, nextPosition, map)
                    updateMap("]", currentPosition, [nextPosition[0], nextPosition[1]+1], map)
                    canMove = True
            elif currentChar == '[':
                nextPosition = [nextPosition[0], nextPosition[1]+1]
                if canMoveObstacle(nextPosition, map, direction):
                    updateMap("]", currentPosition, nextPosition, map)
                    updateMap("[", currentPosition, [nextPosition[0], nextPosition[1]-1], map)
                    canMove = True
        # move up or down
        elif direction[1] == 0:
            closingBracketPos = [currentPosition[0], currentPosition[1]-1 if currentChar == ']' else currentPosition[1]+1]
            closingBracketChar = map[closingBracketPos[0]][closingBracketPos[1]]
            closingBracketNextPos = [a+b for a, b in zip(closingBracketPos, direction)]
            closingBracketNextChar = map[closingBracketNextPos[0]][closingBracketNextPos[1]]
            nextChar = map[nextPosition[0]][nextPosition[1]]
            if nextChar == '.' and part2:
                return True
            elif nextChar == '.':                
                if canMoveObstacle(nextPosition, map, direction, part2) and canMoveObstacle(closingBracketNextPos, map, direction, part2):
                    updateMap(currentChar, currentPosition, nextPosition, map)
                    updateMap(closingBracketChar, closingBracketPos, closingBracketNextPos, map)
                    canMove = True
            elif nextChar == '#' and part2:
                return False
            elif currentChar == nextChar:
                if canMoveObstacle(nextPosition, map, direction, part2) and canMoveObstacle(closingBracketNextPos, map, direction, part2):
                    updateMap(currentChar, currentPosition, nextPosition, map)
                    updateMap(closingBracketChar, closingBracketPos, closingBracketNextPos, map)
                    canMove = True
            elif (currentChar == '[' and nextChar == ']') or (currentChar == ']' and nextChar == '['):
                cellsToUpdate = []
                if closingBracketNextChar == '.':                        
                    if canMoveObstacle(nextPosition, map, direction, part2) and canMoveObstacle([nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1], map, direction, part2):
                        abPos = [a+b for a, b, in zip (direction, nextPosition)]
                        cellsToUpdate.append(returnDict(nextChar, nextPosition, abPos))
                        nextBoxNextPosition = [nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1]
                        nextChar = ']' if nextChar == '[' else ']'
                        abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
                        cellsToUpdate.append(returnDict(nextChar, nextBoxNextPosition, abPos))                            
                else:
                    if (canMoveObstacle(nextPosition, map, direction, True) and
                        canMoveObstacle([nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1], map, direction, part2) and 
                        canMoveObstacle(closingBracketNextPos, map, direction, True) and
                        canMoveObstacle([closingBracketNextPos[0], closingBracketNextPos[1]+1 if closingBracketChar == ']' else closingBracketNextPos[1]-1], map, direction, part2)):
                            abPos = [a+b for a, b, in zip (direction, nextPosition)]
                            cellsToUpdate.append(returnDict(nextChar, nextPosition, abPos))
                            nextBoxNextPosition = [nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1]
                            nextChar = ']' if nextChar == '[' else ']'
                            abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
                            cellsToUpdate.append(returnDict(nextChar, nextBoxNextPosition, abPos))
                            abPos = [a+b for a, b, in zip (direction, closingBracketNextPos)]
                            cellsToUpdate.append(returnDict(closingBracketNextChar, closingBracketNextPos, abPos))
                            nextBoxNextPosition = [nextBoxNextPosition[0], nextBoxNextPosition[1]+1 if closingBracketChar == '[' else nextBoxNextPosition[1]-1]
                            closingBracketChar = ']' if closingBracketChar == '[' else ']'
                            abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
                            cellsToUpdate.append(returnDict(closingBracketChar, nextBoxNextPosition, abPos))
                if len(cellsToUpdate) > 0:
                    for cellToUpdate in cellsToUpdate:
                        updateMap(cellToUpdate["currentChar"], cellToUpdate["currenPos"], cellToUpdate["nextPosition"], map)
                    updateMap(currentChar, currentPosition, nextPosition, map)
                    updateMap(closingBracketChar, closingBracketPos, closingBracketNextPos, map)
                    canMove = True
        else:
            nextChar = map[nextPosition[0]][nextPosition[1]]    
            if nextChar == '#':
                canMove = False                    
    return canMove

def returnDict(currentChar, currentPosition, nextPosition):
    return {"currentChar": currentChar, "currenPos": currentPosition, "nextPosition": nextPosition}

def updateMap(currentChar, currentPosition, nextPosition, map):
    map[nextPosition[0]][nextPosition[1]] = currentChar
    map[currentPosition[0]][currentPosition[1]] = "."

def extendMap(map):
    newMap = []
    for row in map:
        newRow = []
        for element in row:
            if element == 'O':
                newRow.append('[')
                newRow.append(']')
            elif element == '@':
                newRow.append('@')
                newRow.append('.')
            else:
                newRow.append(element)
                newRow.append(element)
        newMap.append(newRow)
    return newMap

directions = {
    "^": [-1,  0], #up
    ">": [ 0,  1], #right
    "<": [ 0, -1], #left
    "v": [ 1,  0]} #down


if __name__ == "__main__":

    input = [list(r) for r in getData("15", True)]

    emptyLine = {"index": lineIndex for lineIndex, line in enumerate(input) if line == []}

    # map = deepcopy(input[:emptyLine["index"]])

    # movement = deepcopy(input[emptyLine["index"]+1:])

    # movement = [move for line in movement for move in line]

    # map = moveRobot(map, movement)

    # boxesLocations1 =  sum([(100 * px + py)
    #                     for px, r in enumerate(map) 
    #                     for py, char in enumerate(r) if char == "O"])

    extendedMap = extendMap(deepcopy(input[:emptyLine["index"]]))

    movement = deepcopy(input[emptyLine["index"]+1:])

    movement = [move for line in movement for move in line]

    map = moveRobot(extendedMap, movement, True)

    boxesLocations2 =  sum([(100 * px + (py - 1))
                         for px, r in enumerate(map) 
                         for py, char in enumerate(r) if char == "]"])

    print("\n\rResult Part 1: ", boxesLocations1)
    print("\r\nResult Part 2: ", boxesLocations2)
                



