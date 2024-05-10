class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append("")
            self.board.append(row)
        self.board[3][3] = "black"
        self.board[4][4] = "black"
        self.board[3][4] = "white"
        self.board[4][3] = "white"     
        
    def getBoard(self):
        return self.board            
                