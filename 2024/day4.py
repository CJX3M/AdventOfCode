from openData import getData

def searchHorizontal(grid, rows, word):
    res = 0
    reverseWord = word[::-1]

    for row in range(rows):
        if word in grid[row]:
            res += grid[row].count(word)
        if reverseWord in grid[row]:
            res += grid[row].count(reverseWord)
    
    return res

def searchVertical(grid, rows, columns, word):
    rotateGrid = []
    # lets rotate 90 degrees the grid
    for i in range(rows):
        vertical = ""
        for j in range(columns):
            vertical += grid[j][i]

        rotateGrid.append(vertical)

    return searchHorizontal(rotateGrid, rows, word)

def searchWord(grid, word):
    rows = len(grid)
    columns = len(grid[0])
    
    res = 0

    # look for horizontal matches
    res += searchHorizontal(grid, rows, word)
    # look for vertical matches
    res += searchVertical(grid, rows, columns, word)

    wordLen = len(word)
    # look for diagonal
    for row in range(rows):
        if wordLen + row > rows:
            break
        for col in range(columns):
            if wordLen + col > columns:
                break
            res += searchGrid(grid, word , row, col)
    
    return res

def getMask(grid, currRow, currCol, size):
    mask = []

    for row in range(size):
        mask.append(grid[currRow+row][currCol:currCol+size])

    return mask

def searchGrid(grid, word, row, col):
    mask = getMask(grid, row, col, 4)

    ocurrences = 0
    reverseWord = word[::-1]

    diagonal = mask[0][0] + mask[1][1] + mask[2][2] + mask[3][3]
    inverseDiagonal = mask[0][3] + mask[1][2] + mask[2][1] + mask[3][0]

    if diagonal == word:
        ocurrences += 1
    if inverseDiagonal == word:
        ocurrences += 1
    if diagonal == reverseWord:
        ocurrences += 1
    if inverseDiagonal == reverseWord:
        ocurrences += 1

    return ocurrences

def searchXMases(grid, word):
    rows = len(grid)
    columns = len(grid[0])
    
    ocurrences = 0

    wordLen = len(word)
    reverseWord = word[::-1]

    for row in range(rows):
        if wordLen + row > rows:
            break
        for col in range(columns):
            if wordLen + col > columns:
                break

            mask = getMask(grid, row, col, 3)

            if mask[1][1] == word[1]:
                diagonal = mask[0][0] + mask[1][1] + mask[2][2]
                inverseDiagonal = mask[0][2] + mask[1][1] + mask[2][0]

                if (diagonal == word or diagonal == reverseWord) and (inverseDiagonal == word or inverseDiagonal == reverseWord):
                    ocurrences += 1
    
    return ocurrences

def printResults(results):
    for result in results:
        print(f"{{{result[0]}, {result[1]}}}", end=" ")
    print()

if __name__ == "__main__":
    #input = getData("day4InputTest.txt")
    input = getData("day4Input.txt")

    word = "XMAS"

    ans = searchWord(input, word)

    print("\n\rPart 1 Results: ", ans)

    word = "MAS"

    ans = searchXMases(input, word)

    print("\n\rPart 2 Results: ", ans)

