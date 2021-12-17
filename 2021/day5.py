def printField(field):
    for row in field:
        print(row)

entryInput = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

data = [i.split('->') for i in entryInput.split('\n')]

field = [[0 for i in range(10)] for r in range(10)]

for coord in data:
    x1, y1 = [int(i) for i in coord[0].split(',')]
    x2, y2 = [int(i) for i in coord[1].split(',')]
    if x1 == x2 or y1 == y2:
        xMin = min(x1, x2)
        while xMin <= max(x1, x2):
            yMin = min(y1, y2)
            while yMin <= max(y1, y2):
                field[xMin][yMin] += 1
                yMin += 1
            xMin += 1
            
printField(field)
