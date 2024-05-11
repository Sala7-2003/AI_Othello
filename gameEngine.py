class GameEngine:
    def __init__(self, board):
        self.board = board
        self.MOVE_DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def isGameEnd(self):
        return not self.canMove("white") and not self.canMove("black")
    
    
    def isValidMove(self, move, diskColor):
        if move not in self.getValidMoves(diskColor):
            return False
        return True
                    
    def canMove(self, diskColor):
        validMoves = self.getValidMoves(diskColor)
        return len(validMoves) > 0
                        
    
    # update board
    def outflankOpenetDisk(self, move, diskColor):
        outFlankDisks = 0
        row, col = move
        board = self.board
        board[row][col] = diskColor
        for i in range(4):
            deltaRow, deltaCol = self.MOVE_DIR[i]
            newRow = row + deltaRow
            newCol = col + deltaCol
            
            isSandwich = False
            temp = 0
            
            if not self.validCorrd(newRow, newCol):
                continue
            if( board[newRow][newCol] == ""):
                continue
            if diskColor == board[newRow][newCol]:
                continue
            
            tempDisk = []
            while self.validCorrd(newRow, newCol) and board[newRow][newCol] != "":
                if board[newRow][newCol] == diskColor:
                    isSandwich = True
                    break
                
                tempDisk.append((newRow, newCol))
                newRow = newRow + deltaRow
                newCol = newCol + deltaCol
                temp += 1
                
            if isSandwich:
                outFlankDisks += temp
                for i, j in tempDisk:
                    board[i][j] = diskColor
        
        return outFlankDisks
    
    def getValidMoves(self, diskColor):
        board = self.board
        oponentColor = None
        moves = []
        if(diskColor == "white"):
            oponentColor = "black"
        else:
            oponentColor = "white"
        for row in range(8):
            for col in range(8):
                isValid = False
                if(board[row][col] != ""):
                    continue
                for i in range(4):
                    deltaRow, deltaCol = self.MOVE_DIR[i]
                    newRow = row + deltaRow
                    newCol = col + deltaCol
                    
                    if not self.validCorrd(newRow, newCol):
                        continue
                    if( board[newRow][newCol] == ""):
                        continue
                    if diskColor == board[newRow][newCol]:
                        continue
                    
                    while self.validCorrd(newRow, newCol) and board[newRow][newCol] != "":
                        if board[newRow][newCol] == diskColor:
                            isValid = True
                        newRow = newRow + deltaRow
                        newCol = newCol + deltaCol
                        
                    if isValid:
                        break
                if isValid:
                    moves.append((row, col))
        return moves
    
    def validCorrd(self, row, col):
        if row < 0 or row >=8 or col < 0 or col >= 8:
            return False
        return True
    