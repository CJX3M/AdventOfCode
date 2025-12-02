from openData import getData

def deepSearch(current, directions, area, region, grid, limits):
    for direction in directions:
        neighboor = tuple((a+b for a,b in zip(current, direction)))
        if neighboor not in grid:
            continue
        if inbound(neighboor, limits) and neighboor not in region and grid[neighboor] == area:
            region.append(neighboor)
            grid.pop(neighboor, None)
            region = deepSearch(neighboor, directions, area, region, grid, limits)
    return region                

def inbound (coords, limits): 
    return 0 <= coords[0] <= limits[0] and 0 <= coords[1] <= limits[1]


if __name__ == "__main__":
    print()
    input = [list(r) for r in getData("12", False)]

    directions = [[-1, 0], #up
                  [ 0,-1], #left
                  [ 0, 1], #right
                  [ 1, 0]] #down

    grid = { ( rowI, colI ): char
            for rowI, row in enumerate( input )
            for colI, char in enumerate( row ) }
    xmin, *_, xmax = sorted( { x for x, y in grid.keys() } )
    ymin, *_, ymax = sorted( { y for x, y in grid.keys() } )

    limit = (xmax, ymax)

    total1 = 0
    total2 = 0

    for coord in [c for c in grid]:
        if coord not in grid:
            continue
        region = []
        area = grid[coord]
        grid.pop(coord, None)
        region.append(coord)
        region = deepSearch(coord, directions, area, region, grid, limit)
        squares = len(region)
        perimeter = 0        
        corners = 0
        if squares == 1:
            perimeter = 4
            corners = 4
        else:
            for coords in region:
                for direction in directions:
                    neighboor = tuple((a+b for a,b in zip(coords, direction)))
                    if not inbound(neighboor, limit):
                        perimeter += 1
                    elif input[neighboor[0]][neighboor[1]] != area:
                        perimeter += 1
                
                getSide = lambda coords, direction: tuple((a+b for a,b in zip(coords, direction)))
                checkSide = lambda side, limit, input, area: not inbound(side, limit) or input[side[0]][side[1]] != area

                side = getSide(coords, directions[0])
                up = checkSide(side, limit, input, area)
                side = getSide(coords, directions[3])
                down = checkSide(side, limit, input, area)
                side = getSide(coords, directions[1])
                left = checkSide(side, limit, input, area)
                side = getSide(coords, directions[2])
                right = checkSide(side, limit, input, area)

                if up and left:
                    corners += 1
                if up and right:
                    corners += 1
                if down and left:
                    corners += 1
                if down and right:
                    corners += 1

                side = getSide(coords, [-1, 1])
                innerCorner = checkSide(side, limit, input, area)
                if not up and not right and innerCorner:
                    corners += 1

                side = getSide(coords, [-1, -1])
                innerCorner = checkSide(side, limit, input, area)
                if not up and not left and innerCorner:
                    corners += 1


                side = getSide(coords, [1, -1])
                innerCorner = checkSide(side, limit, input, area)
                if not down and not left and innerCorner:
                    corners += 1

                side = getSide(coords, [1, 1])
                innerCorner = checkSide(side, limit, input, area)
                if not down and not right and innerCorner:
                    corners += 1

        total1 += perimeter * squares
        total2 += corners * squares
        print(f"\n\rRegion {area} has an area of {squares} and a perimeter of {perimeter} for a total of {squares * perimeter}", end="")
        print(f"\n\rRegion {area} has an area of {squares} and {corners} sides for a total of {corners * squares}", end="")

    print("\r\nResult part 1: ", total1)
    print("\r\nResult part 2: ", total2)