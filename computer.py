class Computer:
    def __init__(self, diskColor, difficulty):
        self.diskColor = diskColor
        self.diskNums = 0
        self.difficulty = 0
        if(difficulty == "easy"):
            self.difficulty = 1
        elif(difficulty == "medium"):
            self.difficulty = 3
        elif(difficulty == "hard"):
            self.difficulty = 5

        