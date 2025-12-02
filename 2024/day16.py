from openData import getData
from os import system
from heapq import heappop, heappush

def printMap(labyrinth, startLocation, points):
    system("clear")
    for r, row in enumerate(labyrinth):
        for c, col in enumerate(row):
            # if (r, c) == startLocation:
            #     print("@", end="")
            if (r, c) in points:
                print("O", end="")                
            else:
                print(col, end="")
        print()
    print()


if __name__ == "__main__":
    labyrinth = [list(r) for r in getData("16", False)]
     
    currentDirectionIndex = 0

    startLocation = [(sr, sc) for sr, r in enumerate(labyrinth) for sc, c in enumerate(r) if c == 'S'][0]

    endLocation = [(er, ec) for er, r in enumerate(labyrinth) for ec, c in enumerate(r) if c == 'E'][0]

    queue = [(0, *startLocation, 0, 1, [startLocation])]

    seen = {(*startLocation, 0, 1)}

    cost = None

    bestScore = float("inf")

    points = set()

    while queue:

        steps, cr, cc, dr, dc, path = heappop(queue)
        seen.add((cr, cc, dr, dc))

        if (cr, cc) == endLocation:
            if not cost:
                cost = steps
            if cost <= bestScore:
                bestScore = cost
                for point in path:
                    points.add(point)
            else:
                break

        nr, nc = cr + dr, cc + dc

        if labyrinth[nr][nc] != "#" and (nr, nc, dr, dc) not in seen:
            heappush(queue, (steps + 1, nr, nc, dr, dc, path + [(nr, nc)]))

        for ndr, ndc in [(-dc, dr), (dc, -dr)]:
            if (cr, cc, ndr, ndc) not in seen and labyrinth[cr + ndr][cc + ndc] != "#":
                heappush(queue, (steps + 1000, cr, cc, ndr, ndc, list(path)))
        

    printMap(labyrinth, (nr, nc), points)

    print("Part 1 result:", cost)

    part2Score = len(points)

    print("Part 2 result:", part2Score)