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
    
    return boards



data = getData("day4.txt")

drawNumbers = data[0].split(',')
boards = createBoards(data)

for number in drawNumbers:
    for board in boards:        
        index = [(k, j) for k in range(len(board)) for j in range(len(board[k])) if board[k][j] == number]
        if index:            
            (k, j) = index[0]
            board[k][j] += "x"
        print(board)
    