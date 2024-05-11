from gameEngine import GameEngine
from player import Player
from computer import Computer
from board import Board
from renderEngine import RenderEngine
from gameState import GameState
class GameController:
    def __init__(self):
        self.gameState = GameState(player=Player("white"), computer=Computer("black"), board=Board(), turn="black")
        self.renderEngine = RenderEngine(self.finishStartScreen, self.gameState)
        self.gameEngine = GameEngine(board=self.gameState.board)
        
    def finishStartScreen(self):
        while not self.gameEngine.isGameEnd():
            validMoves = self.gameEngine.getValidMoves(self.gameState.turn)  
            
    
    def startGame(self):
        self.renderEngine.start()
        
    def switchTurn(self):
        turn = self.gameState.turn
        if turn == "black":
            self.gameEngine.turn = "white"
        elif turn == "white":
            self.gameEngine.turn = "black"



gameController = GameController()
gameController.startGame()


