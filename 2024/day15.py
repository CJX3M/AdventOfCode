from openData import getData
# from time import sleep
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

    return map

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
                



