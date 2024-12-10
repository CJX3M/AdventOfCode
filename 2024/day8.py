from openData import getData
from copy import deepcopy

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
    if coord[0] >= 0 and coord[0] < maxRows and coord[1] >= 0 and coord[1] < maxCols:
        if map[coord[0]][coord[1]] == '.':
            map[coord[0]][coord[1]] = '#'
        if coord not in antiNodes:
            antiNodes.append(coord)
    else:
        return False
    return True


if __name__ == "__main__":
    # input = [list(r) for r in getData("day8testInput.txt")]

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

    antenas = []    

    for unique in uniqueFrequencies:
        if part2 and len(uniqueFrequencies[unique]) > 2:
            [antiNodes.append(deepcopy(coord)) for coord in uniqueFrequencies[unique] if coord not in antiNodes]
        while uniqueFrequencies[unique]:
            antenaDistances = []
            currentCoords = uniqueFrequencies[unique].pop(0)
            for coords in uniqueFrequencies[unique]:
                distance = [currentCoords[0]-coords[0], currentCoords[1]-coords[1]]                                    
                createAntinode(currentCoords, coords, distance, antiNodes, input, part2)

    for r in input:
        print(f"\n\r{''.join(r)}", end='')

    print("\n\rResults: ", len(antiNodes))





