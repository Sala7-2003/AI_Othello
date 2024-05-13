from gameEngine import GameEngine
from player import Player
from computer import Computer
from board import Board
from renderEngine import RenderEngine
from gameState import GameState
import threading


class GameController:
    def __init__(self):
        self.gameState = GameState(player=Player("black"), computer=Computer("white"), board=Board(), turn="black")
        self.renderEngine = RenderEngine(self.finishStartScreen, self.gameState, self.playerPlay)
        self.gameEngine = GameEngine(board=self.gameState.board.getBoard())
        
    def finishStartScreen(self):
        validMoves = self.gameEngine.getValidMoves(self.gameState.turn) 
        self.renderEngine.updateBoardFrm(validMoves)
        
    
    def startGame(self):
        self.renderEngine.start()
        
    def switchTurn(self):
        turn = self.gameState.turn
        if turn == "black":
            self.gameEngine.turn = "white"
        elif turn == "white":
            self.gameEngine.turn = "black"
    
    def playerPlay(self, move):
        # not player turn
        if not self.gameState.turn == self.gameState.player.diskColor:
            return
        
        if not self.gameEngine.isValidMove(move, self.gameState.turn):
            return
        
        diskOutFlanked = self.gameEngine.outflankOpenetDisk(move, self.gameState.turn)
        
        self.gameState.player.diskNums += diskOutFlanked + 1
        self.gameState.computer.diskNums -= diskOutFlanked 
        self.gameState.player.disksPlayed += 1
        
        
        if self.gameEngine.isGameEnd(self.gameState.player.disksPlayed, self.gameState.computer.disksPlayed):
            self.endGame()    
            return
        
        if not self.gameEngine.canMove(self.gameState.computer.diskColor):
            self.renderEngine.updateBoardFrm(self.gameEngine.getValidMoves(self.gameState.turn))
            return
        
        
        self.gameState.turn = self.gameState.computer.diskColor
        
        self.renderEngine.updateBoardFrm(self.gameEngine.getValidMoves(self.gameState.turn))
        
        # threading.Timer(3, self.computerMove).start()
        self.computerMove()
        
        

    def computerMove(self):     
        while(self.gameState.turn == self.gameState.computer.diskColor):
            move = self.gameState.computer.getMove(self.gameState.board, self.gameState.player.diskColor, self.gameState.player.disksPlayed)
                    
            diskOutFlanked = self.gameEngine.outflankOpenetDisk(move, self.gameState.turn)
            
            self.gameState.player.diskNums -= diskOutFlanked
            self.gameState.computer.diskNums += diskOutFlanked + 1
            self.gameState.computer.disksPlayed += 1;
            
            
            if self.gameEngine.isGameEnd(self.gameState.player.disksPlayed, self.gameState.computer.disksPlayed):
                    self.endGame()
                    return   
                
            if not self.gameEngine.canMove(self.gameState.player.diskColor):
                    self.renderEngine.updateBoardFrm(self.gameEngine.getValidMoves(self.gameState.turn))
                    continue
                
            # switch turn to player
            self.gameState.turn = self.gameState.player.diskColor
            
             
                
            self.renderEngine.updateBoardFrm(self.gameEngine.getValidMoves(self.gameState.turn))
        

    def endGame(self):
        winner = None
        if(self.gameState.player.diskNums > self.gameState.computer.diskNums):
            winner = f"{self.gameState.player.name} Wins"
        elif(self.gameState.player.diskNums < self.gameState.computer.diskNums):
            winner = "Computer Wins"
        else:
            winner = "Draw"
        self.renderEngine.displayWinner(winner)
    
    



