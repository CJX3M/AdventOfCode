import multiprocessing
from openData import getData
from copy import deepcopy
# if lookForLoop comes True, I'll be looking for places to put obstacles and create a loop
# if lookForLoop comes False, I'll put overStep to save positions where the guards pass by, and test for loop. if a position
# appears 10, means the guard had pass by 10 times and its on a loop
def moveGuard(input, lookForLoop = False, guardPosition = [], currentDirection = []):
    directions = [[-1, 0],
                  [0, 1],
                  [1, 0],
                  [0, -1]]
    
    currentDirectionIndex = 0 if currentDirection == [] else directions.index(currentDirection)

    guardSteps = []

    obstacleForLoop = []

    if guardPosition == []:        
        for rowIndex, row in enumerate(input):
            if '^' in row:
                col = row.index('^')
                guardPosition = [rowIndex, col]
                break

    while True:
        updateGuardPosition(input, guardPosition, guardSteps, not lookForLoop)
        if not lookForLoop and guardSteps.count(guardPosition) == 10:
            return True
        guardPosition = [a + b for a, b in zip(guardPosition, directions[currentDirectionIndex])]
        nextStep = [a + b for a, b in zip(guardPosition, directions[currentDirectionIndex])]
        if 0 > nextStep[0] or nextStep[0] >= len(input) or 0 > nextStep[1] or nextStep[1] >= len(input[0]):            
            updateGuardPosition(input, guardPosition, guardSteps, not lookForLoop)
            break
        nextDirection = directions[currentDirectionIndex+1 if currentDirectionIndex < 3 else 0]
        if lookForLoop and input[nextStep[0]][nextStep[1]] != '#' and lookObstaclesForLoop(input, guardPosition, nextDirection):
            obstacleForLoop.append({"obstacle": nextStep, "direction": nextDirection})
        if input[nextStep[0]][nextStep[1]] == '#':
            currentDirectionIndex += 1
            if currentDirectionIndex == 4:
                currentDirectionIndex = 0
    if not lookForLoop:
        return False
        
    return (guardSteps, obstacleForLoop) 

def testObstacles(map, obstacles):
    loopObstacles = []

    obstaclesCount = len(obstacles)

    while obstacles:
        obstacle = obstacles.pop()

        print(f"\rTesting {len(obstacles)} out of {obstaclesCount}", end="")

        obstacleCoords = obstacle["obstacle"]
        direction = obstacle["direction"]

        inverseDirection = [x * -1 for x in direction]

        guardStartinPos = [a + b for a, b in zip(obstacleCoords, inverseDirection)]

        map[obstacleCoords[0]][obstacleCoords[1]] = '#'

        if moveGuard(deepcopy(map), guardPosition=guardStartinPos, currentDirection=direction):
            loopObstacles.append(obstacleCoords)

        map[obstacleCoords[0]][obstacleCoords[1]] = '.'

    return loopObstacles

def updateGuardPosition(map, guard, guardSteps, overStep):
    map[guard[0]][guard[1]] = 'X'
    if guard not in guardSteps:
        guardSteps.append(guard)
    elif overStep:
        guardSteps.append(guard)
    
def lookObstaclesForLoop(map, nextPosition, direction):
    while True:
        nextPosition = [a + b for a, b in zip(nextPosition, direction)]
        if 0 > nextPosition[0] or nextPosition[0] >= len(map) or 0 > nextPosition[1] or nextPosition[1] >= len(map[0]):
            return False
        if map[nextPosition[0]][nextPosition[1]] == '#':
            return True

def divideInChunks(list, amount):

    for i in range(0, len(list), amount):
        yield list[i:i + amount]

if __name__ == "__main__":

    input = [list(r) for r in getData("day6TestInput.txt")]

    #input = [list(r) for r in getData("day6Input.txt")]

    guardSteps, obstaclesForLoop = moveGuard(deepcopy(input), True)

    #obstaclesForLoop = divideInChunks(obstaclesForLoop, 1000)

    # pool = multiprocessing.Pool()

    # resultsAsync = [pool.apply_async(testObstacles, args=(input, obstacles)) for obstacles in obstaclesForLoop]

    loopObstacles = testObstacles(input, obstaclesForLoop)

    # loopObstacles = [r.get() for r in resultsAsync]

    # corners = []

    # obstacles = []

    # currentDirectionIndex = 1

    # for obstacle in obstacles:
    #     triage = [obstacle]

    #     searchForNextObstacle(obstacle, directions, currentDirectionIndex)
    #     obstacle = [a + b for a, b in zip(obstacle, directions[currentDirectionIndex])]

    # for corner in corners:
    #     cornerA = [c for c in corners if c[0] == corner[0] and c != corner]
    #     cornerB = [c for c in corners if c[1] == corner[1] and c != corner]
    #     if cornerA and not cornerB:
    #         cornerB = [c for c in corners if (c[1] == cornerA[0][1] or c[0] == cornerA[0][0]) and c != corner and c != cornerA[0]]
    #     elif cornerB and not cornerA:
    #         cornerA = [c for c in corners if (c[1] == cornerB[0][1] or c[0] == cornerB[0][0]) and c != corner and c != cornerB[0]]
    #     addToPosibleObstacles(obstacleForLoop, corner, cornerA[0], cornerB[0])
    
    print("\n\rResult Part 1: ", len(guardSteps))
    print("\n\rResult Part 2: ", len(loopObstacles))



