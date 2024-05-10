class Player:
    def __init__(self, diskColor):
        self.name = ""
        self.diskColor = diskColor
        self.diskNums = 0
        self.move = (0, 0)
    
    def getMove(self):
        return self.move
    
    def userClick(self, event):
        row = event.widget.grid_info()["row"]
        column = event.widget.grid_info()["column"]
        self.move = (row, column)
            
        