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
    #sleep(0.05)

def clear_console():
    system('clear')

def moveRobot(map: list[list], movement: list, part2: bool = False) -> None:
    for cx, r in enumerate(map): 
        for cy, char in enumerate(r):
            if char == "@":
                break
        else:
            continue
        break
    
    for step, nextMove in enumerate(movement):        
        dx, dy = directions[nextMove]
        canMove = True
        if not part2:
            nx, ny = cx + dx, cy + dy
            while True:
                if '.' in map[nx][ny]:
                    break
                if '#' in map[nx][ny]:
                    canMove = False
                    break
                elif 'O' in map[nx][ny]:
                    #canMove, cellsToUpdate = canMoveObstacle([nx, ny], map, [dx, dy], part2)
                    nx, ny = nx + dx, ny + dy
            if not canMove: continue
            map[cx][cy] = '.'
            cx, cy = cx + dx, cy + dy
            if map[cx][cy] == 'O':
                map[nx][ny] = 'O'
            map[cx][cy] = '@'
        else:
            cellsToUpdate = [(cx, cy)]
            i = 0
            while i < len(cellsToUpdate):
                ux, uy = cellsToUpdate[i]
                i += 1
                nx, ny = ux + dx, uy + dy
                if (nx, ny) in cellsToUpdate:
                    continue
                if map[nx][ny] == '#':
                    canMove = False
                    break
                if map[nx][ny] == '.':
                    continue
                if map[nx][ny] == '[':
                    cellsToUpdate.extend([(nx, ny), (nx, ny+1)])
                if map[nx][ny] == ']':
                    cellsToUpdate.extend([(nx, ny), (nx, ny-1)])

            if not canMove: continue

            currentMap = [list(row) for row in map]
            cx, cy = cx + dx, cy + dy
            for nx, ny in cellsToUpdate:
                map[nx][ny] = '.'
            for nx, ny in cellsToUpdate:
                map[nx + dx][ny + dy] = currentMap[nx][ny]
        #printMap(map, step, nextMove)

        # if canMove:
            # while cellsToUpdate:
            #     cellToUpdate = cellsToUpdate.pop(0)
            #     updateMap(cellToUpdate["currentChar"], cellToUpdate["currenPos"], cellToUpdate["nextPosition"], map)
            # cx, cy = updateRobot(map, [cx, cy], [nx, ny])
            
        

    return map

# def updateRobot(map, currentPosition, nextPosition):
#     updateMap("@", currentPosition, nextPosition, map)
#     currentPosition = nextPosition
#     return currentPosition

# def canMoveObstacle(currentPosition: list, map: list[list], direction: list, part2: bool = False):
#     cx, cy = currentPosition
#     nx, ny = [a+b for a, b in zip(currentPosition, direction)]
#     currentChar = map[cx][cy]
#     canMove = False
#     cellsToUpdate = []
#     if currentChar == '.':
#         canMove = True
#     elif currentChar == 'O':
#         nextChar = map[nx][ny]
#         if nextChar == 'O':
#             if canMoveObstacle([nx, ny], map, direction):
#                 updateMap('O', [cx, cy], [nx, ny], map)
#                 canMove = True
#             else:
#                 canMove = False    
#         elif nextChar == '.':
#             updateMap('O', [cx, cy], [nx, ny], map)
#             canMove = True
#         elif '#' in nextChar:
#             canMove = False
#     else:
#         # move left or right
#         if direction[0] == 0:
#             if '#' in currentChar:
#                 canMove = False
#             elif currentChar == ']':
#                 ny -= 1
#                 (canMove, cellsToUpdate) = canMoveObstacle([nx, ny], map, direction)
#                 if canMove:
#                     updateMap("[", [cx, cy], [nx, ny], map)
#                     updateMap("]", [cx, cy], [nx, ny+1], map)
#                     canMove = True
#             elif currentChar == '[':
#                 ny += 1
#                 (canMove, cellsToUpdate) = canMoveObstacle([nx, ny], map, direction)
#                 if canMove:
#                     updateMap("]", [cx, cy], [nx, ny], map)
#                     updateMap("[", [cx, cy], [nx, ny-1], map)
#                     canMove = True
#         # move up or down
#         elif direction[1] == 0:
#             cbPx, cbPy = [cx, cy-1 if currentChar == ']' else cy+1]
#             closingBracketChar = map[cbPx][cbPy]
#             cbNPx, cbNPy = cbNPx + direction[0], cbNPy + direction[1]
#             closingBracketNextChar = map[cbNPx][cbNPy]
#             nextChar = map[nx][ny]
#             if nextChar == '.' and closingBracketNextChar == '.':                    
#                 # if canMoveObstacle(nextPosition, map, direction, part2) and canMoveObstacle(closingBracketNextPos, map, direction, part2):
#                 # updateMap(currentChar, currentPosition, nextPosition, map)
#                 # updateMap(closingBracketChar, closingBracketPos, closingBracketNextPos, map)
#                 cellsToUpdate.append(returnDict(currentChar, [cx, cy], [nx, ny]))
#                 cellsToUpdate.append(returnDict(closingBracketChar, [cbNPx, cbNPy], [cbNPx, cbNPy]))
#                 canMove = True
#                 return (canMove, cellsToUpdate)
#             elif '#' in nextChar and part2:
#                 canMove = False
#             elif currentChar == nextChar:
#                 (canMove1, cells1) = canMoveObstacle([nx, ny], map, direction, part2)
#                 (canMove2, cells2) = canMoveObstacle([cbNPx, cbNPy], map, direction, part2)
#                 if canMove1 and canMove2:
#                     cellsToUpdate.extend(cells1)
#                     cellsToUpdate.append(returnDict(currentChar, [cx, cy], [nx, ny]))
#                     cellsToUpdate.append(returnDict(closingBracketChar, [cbPx, cbPy], [cbNPx, cbNPy]))
#                     # updateMap(currentChar, currentPosition, nextPosition, map)
#                     # updateMap(closingBracketChar, closingBracketPos, closingBracketNextPos, map)
#                     canMove = True
#                     return (canMove, cellsToUpdate)
#             elif (currentChar == '[' and nextChar == ']') or (currentChar == ']' and nextChar == '['):                
#                 if closingBracketNextChar == '.':                        
#                     (canMove1, cells1) = canMoveObstacle([nx, ny], map, direction, part2)
#                     (canMove2, cells2) = canMoveObstacle([nx, ny+1 if nextChar == '[' else ny-1], map, direction, part2)
#                     if canMove1 and canMove2:
#                         cellsToUpdate.extend(cells2)
#                         cellsToUpdate.extend(cells1)
#                         cellsToUpdate.append(returnDict(currentChar, [cx, cy], [nx, ny]))
#                         cellsToUpdate.append(returnDict(closingBracketChar, [cbPx, cbPy], [cbNPx, cbNPy]))
#                         canMove = True
#                         return (canMove, cellsToUpdate)
#                         # abPos = [a+b for a, b, in zip (direction, nextPosition)]
#                         # cellsToUpdate.append(returnDict(nextChar, nextPosition, abPos))
#                         # nextBoxNextPosition = [nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1]
#                         # nextChar = ']' if nextChar == '[' else ']'
#                         # abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
#                         # cellsToUpdate.append(returnDict(nextChar, nextBoxNextPosition, abPos))                            
#                 else:
#                     (canMove1, cells1) = canMoveObstacle([nx, ny], map, direction, part2)
#                     (canMove2, cells2) = canMoveObstacle([nx, ny+1 if nextChar == '[' else ny-1], map, direction, part2)
#                     (canMove3, cells3) = canMoveObstacle([cbNPx, cbNPy], map, direction, part2)
#                     (canMove4, cells4) = canMoveObstacle([cbNPx, cbNPy+1 if closingBracketChar == ']' else cbNPy-1], map, direction, part2)
#                     if canMove1 and canMove2 and canMove3 and canMove4:
#                         cellsToUpdate.extend(cells4)
#                         cellsToUpdate.extend(cells3)
#                         cellsToUpdate.extend(cells2)
#                         cellsToUpdate.extend(cells1)
#                         cellsToUpdate.append(returnDict(currentChar, [cx, cy], [nx, ny]))
#                         cellsToUpdate.append(returnDict(closingBracketChar, [cbPx, cbPy], [cbNPx, cbNPy]))
#                         canMove = True
#                         return (canMove, cellsToUpdate)
#                             # abPos = [a+b for a, b, in zip (direction, nextPosition)]
#                             # cellsToUpdate.append(returnDict(nextChar, nextPosition, abPos))
#                             # nextBoxNextPosition = [nextPosition[0], nextPosition[1]+1 if nextChar == '[' else nextPosition[1]-1]
#                             # nextChar = ']' if nextChar == '[' else ']'
#                             # abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
#                             # cellsToUpdate.append(returnDict(nextChar, nextBoxNextPosition, abPos))
#                             # abPos = [a+b for a, b, in zip (direction, closingBracketNextPos)]
#                             # cellsToUpdate.append(returnDict(closingBracketNextChar, closingBracketNextPos, abPos))
#                             # nextBoxNextPosition = [nextBoxNextPosition[0], nextBoxNextPosition[1]+1 if closingBracketChar == '[' else nextBoxNextPosition[1]-1]
#                             # closingBracketChar = ']' if closingBracketChar == '[' else ']'
#                             # abPos = [a+b for a, b, in zip (direction, nextBoxNextPosition)]
#                             # cellsToUpdate.append(returnDict(closingBracketChar, nextBoxNextPosition, abPos))
#         else:
#             nextChar = map[nx][ny]    
#             if '#' in nextChar:
#                 canMove = False                    
#     return (canMove, cellsToUpdate if canMove else [])

# def returnDict(currentChar, currentPosition, nextPosition):
#     return {"currentChar": currentChar, "currenPos": currentPosition, "nextPosition": nextPosition}

# def updateMap(currentChar, currentPosition, nextPosition, map):
    map[nextPosition[0]][nextPosition[1]] = currentChar
    map[currentPosition[0]][currentPosition[1]] = "."

def extendMap(map):
    elems = {
        "O": "[]",
        "@": "@.",
        "#": "##",
        ".": ".."
    }
    newMap = []
    for row in map:
        newRow = []
        for element in row:
            newRow.extend(elems[element])
        newMap.append(newRow)
    return newMap

directions = {
    "^": [-1,  0], #up
    ">": [ 0,  1], #right
    "<": [ 0, -1], #left
    "v": [ 1,  0]} #down


if __name__ == "__main__":

    input = [list(r) for r in getData("15", False)]

    emptyLine = {"index": lineIndex for lineIndex, line in enumerate(input) if line == []}

    map = deepcopy(input[:emptyLine["index"]])

    movement = input[emptyLine["index"]+1:]

    movement = [move for line in movement for move in line]

    map = moveRobot(map, movement)

    boxesLocations1 =  sum([(100 * px + py)
                        for px, r in enumerate(map) 
                        for py, char in enumerate(r) if char == "O"])

    extendedMap = extendMap(deepcopy(input[:emptyLine["index"]]))

    map = moveRobot(extendedMap, movement, True)

    boxesLocations2 =  sum([(100 * px + (py - 1))
                         for px, r in enumerate(map) 
                         for py, char in enumerate(r) if char == "]"])

    print("\n\rResult Part 1: ", boxesLocations1)
    print("\r\nResult Part 2: ", boxesLocations2)
                



