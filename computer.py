import copy
from gameEngine import GameEngine
MAX = 100
MIN = -100
class Computer:
    def __init__(self, diskColor):
        self.diskColor = diskColor
        self.diskNums = 2
        self.difficulty = 0


    def updateDifficulty(self, difficulty):
        if(difficulty == "easy"):
            self.difficulty = 1
        elif(difficulty == "medium"):
            self.difficulty = 3
        elif(difficulty == "hard"):
            self.difficulty = 5
    
    def getMove(self, board, playerDiskColor):
        boardCpy = copy.deepcopy(board.getBoard())
        _, move = self.minimax(0, True, MIN, MAX, boardCpy, playerDiskColor)
        if move == None:
            move = GameEngine(copy.deepcopy(board.getBoard())).getValidMoves(self.diskColor)[0]
        return move
    
    
    
    
    def minimax(self, depth, maximizingPlayer, 
         alpha, beta, board, playerDiskColor): 

        gameEngine = GameEngine(board)
        
        if depth == self.difficulty: 
            return (self.evaluate(board), ())

        if maximizingPlayer: 

            best = MIN
            bestMove = None

            validMoves = gameEngine.getValidMoves(self.diskColor)
            
            for move in validMoves: 
                gameEngine.outflankOpenetDisk(move, self.diskColor)
                val,_  = self.minimax(depth + 1, 
                            False, alpha, beta, copy.deepcopy(board), playerDiskColor) 
                if val > best:
                    bestMove = move
                    best = val
                
                alpha = max(alpha, best) 

                if beta <= alpha: 
                    break
                
            return (best, bestMove)

        else:
            best = MAX
            bestMove = None

            validMoves = gameEngine.getValidMoves(playerDiskColor)
            
        
            for move in validMoves: 
                val,_ = self.minimax(depth + 1, 
                                True, alpha, beta, copy.deepcopy(board), playerDiskColor)
                if val < best:
                    best = val
                    bestMove = move
                beta = min(beta, best) 

                # Alpha Beta Pruning 
                if beta <= alpha: 
                    break

            return (best, bestMove)
    
    def evaluate(self, board):
        computerDisks = 0
        playerDisks = 0
        for i in range(8):
            for j in range(8):
                if(board[i][j] == ""):
                    continue
                if(board[i][j] == self.diskColor):
                    computerDisks += 1
                else:
                    playerDisks += 1
        return computerDisks - playerDisks
                    