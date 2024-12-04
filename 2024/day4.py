from openData import getData

def searchWord(grid, word):
    rows = len(grid)
    columns = len(grid[0])

    ans = []

    for row in range(rows-4):
        for col in range(columns-4):
            ans.append(searchGrid(grid, word , row, col))
    
    return ans

def getMask(grid, currRow, currCol):
    mask = []

    for row in range(4):
        mask.append(grid[currRow+row][currCol:4])

    return mask



def searchGrid(grid, word, row, col):
    mask = getMask(grid, row, col)
    # rows = len(grid)
    # columns = len(grid[0])

    # if grid[row][col] != word[0]:
    #     return False
    
    # x = [-1, -1, -1,  0, 0,  1, 1, 1]
    # y = [-1,  0,  1, -1, 1, -1, 0, 1]

    # for dir in range(len(x)):
    #     currX, currY = row + x[dir], col + y[dir]

    #     k = 1

    #     while k < len(word):

    #         if currX >= columns or currX < 0 or currY >= rows or currY < 0:
    #             break

    #         if grid[currX][currY] != word[k]:
    #             break

    #         currX += x[dir]
    #         currY += y[dir]
    #         k += 1

    #     if k == len(word):
    #         return True
    
    # return False

def printResults(results):
    for result in results:
        print(f"{{{result[0]}, {result[1]}}}", end=" ")
    print()

if __name__ == "__main__":
    input = getData("day4InputTest.txt")
    #input = getData("day4Input.txt")

    word = "XMAS"
    wordBackwards = "SAMX"

    ans = searchWord(input, word)
    ans.append(searchWord(input, wordBackwards))

    printResults(ans)

    print("\n\rResults: ", len(ans))

