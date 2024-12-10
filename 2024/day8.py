from openData import getData
from copy import deepcopy

def inbound(antiNode):
    return 0 <= antiNode[0] < maxRows and 0 <= antiNode[1] < maxCols

def createAntinode(currentCoords, coords, distance, antiNodes, map, part2 = False):
    inverseDistance = [distance[0]*-1, distance[1]*-1]
    antenna1 = [a+b for a, b in zip(coords, inverseDistance)]
    antenna2 = [a+b for a, b in zip(distance, currentCoords)]

    addAntinode1 = addAntinode(antenna1, antiNodes, map)
    addAntinode2 = addAntinode(antenna2, antiNodes, map)

    if not addAntinode1 and not addAntinode2:
        return
    if part2:
        createAntinode(antenna2, antenna1, distance, antiNodes, map, True)
    
def addAntinode(coord, antiNodes, map):
    if not inbound(coord):
        return False
    if map[coord[0]][coord[1]] == '.':
        map[coord[0]][coord[1]] = '#'
    if coord not in antiNodes:
        antiNodes.append(coord)    
    return True


if __name__ == "__main__":
    #input = [list(r) for r in getData("day8testInput.txt")]

    input = [list(r) for r in getData("day8Input.txt")]

    part2 = True

    uniqueFrequencies = {}

    for rowI, row in enumerate(input):
        frequencies = [freq for freq in row if freq != '.']
        for freq in frequencies:
            colI = row.index(freq)
            if freq not in uniqueFrequencies:                
                uniqueFrequencies[freq] = [[rowI, colI]]
            else:
                uniqueFrequencies[freq].append([rowI, colI])

    maxCols = len(input[0])
    maxRows = len(input)

    antiNodes = []

    for unique in uniqueFrequencies:
        if part2 and len(uniqueFrequencies[unique]) > 2:
            [antiNodes.append(deepcopy(coord)) for coord in uniqueFrequencies[unique] if coord not in antiNodes]
        while uniqueFrequencies[unique]:
            currentCoords = uniqueFrequencies[unique].pop(0)
            input[currentCoords[0]][currentCoords[1]] = '*'
            for coords in uniqueFrequencies[unique]:
                input[coords[0]][coords[1]] = '*'
                distance = [currentCoords[0]-coords[0], currentCoords[1]-coords[1]]                                    
                createAntinode(currentCoords, coords, distance, antiNodes, input, part2)
                input[coords[0]][coords[1]] = unique
            input[currentCoords[0]][currentCoords[1]] = unique

    for r in input:
        print(f"\n\r{''.join(r)}", end='')

    print("\n\rResults: ", len(antiNodes))





