import serial as serial
import keyboard
import time

from Player import Player
from AI import AI
from Game import Game

def main():
  try:
    human = Player("x", "Human")
    ai = AI("o", "TriquiBot")
    game = Game(ai, human)
    winner = game.checkWinner()
    print("START")
    time.sleep(3)
    
    while winner == None: 
      game.play()
      winner = game.checkWinner()
      if winner:
        print("Wins: ", winner)

      if keyboard.is_pressed("q"):
        break

  except Exception as err:
    print(str(err))

main()