from openData import getData

def createBoards(data):
    newBoard = False
    currentBoard = []
    boards = []

    for lines in data:
        if ',' in lines:
            continue
        
        if lines == "":
            newBoard = True
            continue

        if newBoard and len(currentBoard) > 0:
            boards.extend([currentBoard])
            currentBoard = []
        
        newBoard = False    
        currentBoard.append(lines.split())
    
    # missing last board!
    boards.extend([currentBoard])
    return boards

def checkForBingoRow(board):
    for line in board:        
        checks = [i for i in line if "x" in i]
        if len(checks) == 5:
            return True
    return False

def checkForBingoColumn(board):
    rowLength = len(board[0])
    i = 0
    j = 0
    marked = 0
    while i < rowLength:
        j = 0
        while j < len(board):
            if "x" == board[j][i]:
                marked += 1
            j += 1
        if marked == 5:
            return True
        i += 1
        marked = 0

data = getData("day4.txt")

drawNumbers = data[0].split(',')
boards = createBoards(data)
winnerBoard = []
lastNumber = 0

for number in drawNumbers:
    for board in boards:
        if len(board) == 6:
            continue        
        index = [(k, j) for k in range(len(board)) for j in range(len(board[k])) if board[k][j] == number]
        if index:
            (k, j) = index[0]
            board[k][j] = "x"
            lastNumber = int(number)
            if checkForBingoRow(board):
                print(len(boards))
                winnerBoard = board
                board.extend("x")
                continue
            if checkForBingoColumn(board):
                print(len(boards))
                winnerBoard = board
                board.extend("x")
                continue


notMarked = []

print(winnerBoard)

for row in winnerBoard:
    for number in row:
        if "x" not in number:
            notMarked.append(int(number))

print("Board Score: ", sum(notMarked) * lastNumber)