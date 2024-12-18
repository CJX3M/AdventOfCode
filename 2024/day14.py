from openData import getData
from collections import defaultdict, deque
from math import floor
from re import findall
import os
from time import sleep

class robot():

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def getPosition(self):
        return self.position
    
    def getVelocity(self):
        return self.velocity
    
    def updatePosition(self, newPosition):
        self.position = newPosition

def clear_console():
    os.system('clear')

def isTree(positions):

    adj = defaultdict(list)
    positions_set = set(positions)
    
    for x, y in positions:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Adjacent cells
            neighbor = (x + dx, y + dy)
            if neighbor in positions_set:
                adj[(x, y)].append(neighbor)
    
    # Use DFS to check for connectedness and cycles
    visited = set()
    stack = [(positions[0], None)]  # (current node, parent node)
    edges = 0
    
    while stack:
        node, parent = stack.pop()
        if node in visited:
            return False  # Cycle detected
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor != parent:
                stack.append((neighbor, node))
                edges += 1
    
    # Check connectedness and edge count
    return len(visited) == len(positions) and edges == len(positions) - 1

def simulateRobots(robots: list[robot], steps, grid_size, part2):
    grid_width, grid_height = grid_size

    step = 1

    while step < steps:
        # Create an empty grid
        grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]
        for robot in robots:
            x, y = robot.getPosition()
            x += robot.getVelocity()[0]
            y += robot.getVelocity()[1]

            x, y = x % grid_width, y % grid_height
            # Place the robot on the grid
            grid[y][x] = 'R'  # Invert y-axis for display

            robot.updatePosition((x, y))

        if part2:
            steps += 1
        step += 1

        # Clear the console for real-time effect
        clear_console()

        # Print the grid
        print(f"Step {step}/{steps}")
        for row in grid:
            print(f"{' '.join(row)}")

        if part2 and step >= 8100:
            if isTree([r.getPosition() for r in robots]):
                break

    return robot

if __name__ == "__main__":

    input = getData("14", False)

    robots = []

    grid_size = (101, 103)

    steps = 100

    # for row in input:
    #     px, py, vx, vy = findall("-?\\d+", row)
    #     rob = simulateRobots(robot((int(px), int(py)), (int(vx), int(vy))), steps, grid_size)
    #     robots.append(rob)

    part2 = True

    for row in input:
        px, py, vx, vy = findall("-?\\d+", row)
        robots.append(robot((int(px), int(py)), (int(vx), int(vy))))
    simulateRobots(robots, steps, grid_size, part2)


    checkPosition = lambda position, minX, maxX, minY, maxY: minX <= position[1] < maxX and minY <= position[0] < maxY

    midX =  floor(grid_size[0]/2)
    maxX = grid_size[0]
    midY = floor(grid_size[1]/2)
    maxY = grid_size[1]

    cuadrant1 = [r for r in robots if checkPosition(r.getPosition(), 0, midY, 0, midX)]
    cuadrant2 = [r for r in robots if checkPosition(r.getPosition(), 0, midY, midX+1, maxX)]
    cuadrant3 = [r for r in robots if checkPosition(r.getPosition(), midY+1, maxY, 0, midX)]    
    cuadrant4 = [r for r in robots if checkPosition(r.getPosition(), midY+1, maxY, midX+1, maxX)]

    print(f"\r\nResult Part1: {len(cuadrant1) * len(cuadrant2) * len(cuadrant3) * len(cuadrant4)}")