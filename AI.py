import numpy as np
from serial import Serial

from Player import Player
from Camera import Camera

class AI(Player):
  def __init__(self, sign, name):
    super().__init__(sign, name)
    self.robot = Serial("COM3", 9600)
    self.camera = Camera()


  def analyzeGame(self, moves):
    print("Start camera")
    self.camera.takePhoto("newboard")

    # get move 
    cells = self.camera.generateCells()
    lastMove = self.identifyMove(cells, moves)

    return lastMove

  def identifyMove(self, cells, moves):
    num = 0
    for i in range(0, 10):
      if i in moves:
        continue
      for cell in cells[i]:
        for pixel in cell:
          if pixel == 255: 
            num += 1
            if num >= 5:
              return i
    return None
  
  def getBestMove(self, game):     
    board = game.board 
    bestScore = -np.inf
    move = []
    
    for i in range(3):
      for j in range(3):
        if (board.get(i, j) == ''): 
          
          board.set(i, j, str(game.ai))
          score = self.minmax(game, 0, False)
          board.set(i, j, "")

          if (score > bestScore):
            bestScore = score
            move =  [i, j]
    
    i, j = move

    return board.index(i, j)

  def moveRobot(self, move):
    moveEncoded = str(move).encode("ASCII")
    self.robot.write(moveEncoded)

  def minmax(self, game, depth, isMaximizing):
    result = game.checkWinner()

    if result != None:
      return game.scores[result]
    
    if (isMaximizing): 
      bestScore = -np.inf

      for i in range(3): 
        for j in range(3):
          if (game.board.get(i, j) == ''): 
            
            game.board.set(i, j, str(game.ai))
            score = self.minmax(game, depth + 1, False)
            game.board.set(i, j, "") 

            bestScore = max(score, bestScore)
      return bestScore
    else: 
      bestScore = np.inf
      
      for i in range(3): 
        for j in range(3): 
          if (game.board.get(i, j) == ''):

            game.board.set(i, j, str(game.human))
            score = self.minmax(game, depth + 1, True)
            game.board.set(i, j, "") 

            bestScore = min(score, bestScore)
    
      return bestScore