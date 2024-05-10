import tkinter as tk
from tkinter import ttk
from gameState import GameState
from player import Player
from computer import Computer
from board import Board

class RenderEngine:
    def __init__(self, startCommand, gameState):
        self.window = tk.Tk()
        self.window.geometry("900x800")
        self.window.title("Othello Game")   
        self.startFrame = tk.Frame(self.window)
        self.boardFrame = tk.Frame(self.window)
        self.startCommand = startCommand
        self.gameState = gameState
        
        self.initBackgroundImg()
        self.initStartFrm()
        
    
    def start(self):
        self.showStartFrame()
        self.window.mainloop()
    
    def showStartFrame(self):
        self.boardFrame.pack_forget()
        self.startFrame.pack(fill=tk.BOTH, expand=True)
    
    def showBoardFrame(self):
        self.startFrame.pack_forget()
        self.boardFrame.pack(fill=tk.BOTH, expand=True)
    
    def initBackgroundImg(self):
        self.bgImg = tk.PhotoImage(file="./assets/background2.png")
        
        self.bgImgLbl = tk.Label(self.startFrame, image=self.bgImg)
        self.bgImgLbl.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.bgImgLbl2 = tk.Label(self.boardFrame, image=self.bgImg)
        self.bgImgLbl2.place(x=0, y=0, relwidth=1, relheight=1)
    
    def initStartFrm(self):
        labelName = tk.Label(self.startFrame, text="Player Name:", font=("Arial", 18), fg="white", bg='#2e6131', relief="flat", justify="center")
        labelName.pack(pady=20)
        
        self.entryName = tk.Entry(self.startFrame, font=("Arial", 12))
        self.entryName.pack(pady=5, padx=10, ipadx=100)
        
        labelDifficulty = tk.Label(self.startFrame, text="Choose Difficulty:", font=("Arial", 18), fg="white", bg="#2e6131", justify="center")
        labelDifficulty.pack(pady=20)
        
        buttonEasy = ttk.Button(self.startFrame, text="Easy", style="Custom.TButton", command=self.setEasyDifficulty)
        buttonEasy.pack(pady=5, padx=10, ipadx=20, ipady=10)
        
        buttonMedium = ttk.Button(self.startFrame, text="Medium", style="Custom.TButton", command=self.setMediumDifficulty)
        buttonMedium.pack(pady=5, padx=10, ipadx=20, ipady=10)
        
        buttonHard = ttk.Button(self.startFrame, text="Hard", style="Custom.TButton", command=self.setHardDifficulty)
        buttonHard.pack(pady=5, padx=10, ipadx=20, ipady=10)
        
        # Style configuration for custom button
        self.window.style = ttk.Style()
        self.window.style.theme_use('clam')
        self.window.style.configure('Custom.TButton', background='#59ab16', foreground='white', borderwidth=0, bd=0)
        self.window.style.map('Custom.TButton', background=[('active', 'green')], bordercolor=[('active', '#3E3E3E')], foreground=[('active', 'white')])
    
    def setEasyDifficulty(self):
        self.startGame("easy")
    
    def setMediumDifficulty(self):
        self.startGame("medium")
        
    def setHardDifficulty(self):
        self.startGame("hard")
    
    def startGame(self, difficulty):
        if(self.entryName.get() == ""):
            return
        self.gameState.player.name = self.entryName.get()
        self.gameState.computer.difficulty = difficulty
        self.startCommand()  
        self.showBoardFrame()
    
    def initBoardFrm(self):
        playerPieceImg = tk.PhotoImage(file="./assets/black_disk_small.png")
        computerPiecetImg = tk.PhotoImage(file="./assets/white_disk_small.png")
        
        self.boardFrame.grid_columnconfigure(0, weight=1, uniform="column")
        self.boardFrame.grid_columnconfigure(1, weight=1, uniform="column")
        playerFrame = tk.Frame(self.boardFrame, bg="green")
        playerFrame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.Label(playerFrame, image=playerPieceImg, bg="black").pack(side="right")
        tk.Label(playerFrame, text="Player", font=("Arial", 16), bg='#2e6131', fg="white", relief="flat", justify="center").pack(fill="x", pady=5, anchor="center")
        self.playerScore = tk.Label(playerFrame, text=str(self.gameState.player.diskNums), font=("Arial", 16), bg='#2e6131', fg="white", relief="flat", justify="center").pack(fill="x", pady=5, anchor="center")

        
        computerFrame = tk.Frame(self.boardFrame, bg="green")
        computerFrame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        tk.Label(computerFrame, image=computerPiecetImg).pack(side="right")
        tk.Label(computerFrame, text="Computer", font=("Arial", 16), bg='#2e6131', fg="white", relief="flat", justify="center").pack(fill="x", pady=5, anchor="center")
        self.computerScore = tk.Label(computerFrame, text=str(self.gameState.computer.diskNums), font=("Arial", 16), bg='#2e6131', fg="white", relief="flat", justify="center").pack(fill="x", pady=5, anchor="center")
        
        turnFrame = tk.Frame(self.boardFrame, bg="green")
        turnFrame.grid(row=1, columnspan=2, padx=10, pady=10, sticky="ew")
        self.lblTurn = tk.Label(turnFrame, text=self.gameState.turn, font=("Arial", 16), bg='#2e6131', fg="white", relief="flat", justify="center").pack(fill="x", pady=5, anchor="center")
        self.drawBoard([])
        
    def drawBoard(self, validMoves):
        self.gridBoardFrm = []
        wrapperFrame = tk.Frame(self.boardFrame)
        wrapperFrame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        circle_radius = 25
        
        board = self.gameState.board.getBoard()

        for i in range(8):
            frames = []
            for j in range(8):
                fr = tk.Frame(wrapperFrame, width='60', height='60', bg='green', highlightbackground='black', highlightthickness=2)
                frames.append(fr)
                fr.grid(row=i, column=j, padx=2, pady=2)  # Adjust padding as needed
                
                # Create a canvas in each frame
                canvas = tk.Canvas(fr, width=60, height=60, bg='green', highlightthickness=0)
                canvas.pack()
                
                # Calculate circle coordinates
                x = 30
                y = 30
                
                for row, col in validMoves:
                    if (i, j) == (row, col):
                        canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, outline="black", fill="green")

                if(board[i][j] == "white"):
                    canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, outline="black", fill="white")

                if(board[i][j] == "black"):
                    canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, outline="black", fill="black")
                                       
            self.gridBoardFrm.append(frames)
    
        

def startGame():
    pass
    
gameState =  GameState(player=Player("white"), computer=Computer("black", ""), board=Board(), turn="player")   
renderEng = RenderEngine(startCommand=startGame, gameState=gameState)
renderEng.initBoardFrm()
renderEng.start()
