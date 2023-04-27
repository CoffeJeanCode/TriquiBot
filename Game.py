import matplotlib.pyplot as plt
import time

from BiArray import BiArray

class Game:
  def __init__(self, ai, human):

    self.ai = ai
    self.human = human

    self.ai.score = 10
    self.human.score = -10

    self.scores = { 
      str(self.ai): self.ai.score,                                                                                                                                                                                                      
      str(self.human): self.human.score,
      "tie": 0 
    }

    self.currentPlayer = self.human
    self.board = BiArray(3, 3).fill("")
    self.moves = []


  def play(self):

    # get last move
    self.changePlayer(self.human) 
    
    time.sleep(6)

    lastMove  = self.ai.analyzeGame(self.moves)
    lastMove = self.updateBoard(lastMove)

    print("\n")

    # get best move
    self.changePlayer(self.ai) 
    bestMove = self.ai.getBestMove(self)
    bestMove = self.updateBoard(bestMove)
    
    # move robot
    self.ai.moveRobot(bestMove)
    print("last move (human) ", lastMove)
    print("best move (ai) ", bestMove)
    print(self.board, "moves", self.moves)

  def showBoard(self):
    # Crear una figura y un conjunto de ejes
    fig, ax = plt.subplots(figsize=(3, 3))

    # Configurar los ejes
    ax.set_aspect('equal')
    ax.axis('off')

    # Dibujar la cuadrícula del tablero
    for i in range(4):
        ax.plot([0, 3], [i, i], 'k')
        ax.plot([i, i], [0, 3], 'k')

    # Dibujar las marcas en el tablero
    for i in range(9):
      # Calcular las coordenadas de la celda en el gráfico
      x = (i % 3) + 0.5
      y = (i // 3) + 0.5
      
      # Determinar la marca o número a dibujar en la celda
      cell_value = self.board.rawGet(i)
      if cell_value == 'X':
          ax.plot(x, y, marker='x', markersize=20, markeredgewidth=2, markeredgecolor='black', linestyle='none')
      elif cell_value == 'O':
          ax.plot(x, y, marker='o', markersize=20, markeredgewidth=2, markeredgecolor='black', markerfacecolor='none', linestyle='none')
      else:
          ax.text(x, y, str(i + 1), fontsize=15, ha='center', va='center')

    # Mostrar el gráfico
    plt.show()

  def changePlayer(self, newPlayer):
    print(newPlayer)
    self.currentPlayer = newPlayer 
    

  def updateBoard(self, move):
    self.board.rawSet(move, str(self.currentPlayer.sign))
    self.moves.append(move)
    return move + 1

  def equalMoves(a, b, c):
    return a == b and b == c and a != ""

  def checkWinner(self):
    winner = None

    # horizontal
    for i in range(3):
      if Game.equalMoves(self.board.get(i, 0), self.board.get(i, 1), self.board.get(i, 2)):
        winner = self.board.get(i, 0)
      
    # Vertical
    for i in range(3):
      if Game.equalMoves(self.board.get(0, i), self.board.get(1, i), self.board.get(2, i)):
        winner = self.board.get(0, i)
      
    # Diagonal
    if Game.equalMoves(self.board.get(0, 0), self.board.get(1, 1), self.board.get(2, 2)):
      winner = self.board.get(0, 0)
    
    if Game.equalMoves(self.board.get(2, 0), self.board.get(1, 1), self.board.get(0, 2)): 
      winner = self.board.get(2, 0)
    

    openSpots = 0
    for i in range(3):
      for j in range(3): 
        if (self.board.get(i, j) == ''):
          openSpots += 1

    if winner == None and openSpots == 0: 
      return 'tie'
    else: 
      return winner
    