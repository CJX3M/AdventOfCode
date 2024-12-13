from openData import getData
from copy import deepcopy

if __name__ == "__main__":

    input = [list(r) for r in getData("12", True)]

    garden = dict()

    maxRows = len(input)
    maxCols = len(input[0])

    for rowI, r in enumerate(input):
        for colI, area in enumerate(r):
            if area not in garden:
                garden[area] = {
                    "region": [[rowI, colI]],
                    "area": 1,
                    "perimeter": 0
                }
            else:
                garden[area]["region"].append([rowI, colI])
                garden[area]["area"] += 1
                    
    directions = [[ 1,0], #down
                  [ 0,1], #right
                  [-1,0], #up
                  [ 0,-1]]#left

    inbound = lambda coords: 0 <= coords[0] < maxRows and 0 <= coords[1] < maxCols

    total = 0

    for area in garden.keys():
        for coords in garden[area]["region"]:
            regionNeighboor = False
            for direction in directions:
                neighboor = [a+b for a,b in zip(coords, direction)]
                if not inbound(neighboor):
                    garden[area]["perimeter"] += 1
                    continue
                if input[neighboor[0]][neighboor[1]] != area:
                    garden[area]["perimeter"] += 1
                else:                    
                    regionNeighboor = True
            if not regionNeighboor:
                garden[area]["area"] -= 1
            if garden[area]["area"] == 0:
                garden[area]["area"] = 1
        total += garden[area]["perimeter"] * garden[area]["area"]

    print("\r\nResult part 1: ", total)