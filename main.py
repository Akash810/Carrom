# import pdb; pdb.set_trace()
from game import Game
from player import Player
from config import INPUT_X, INPUT_Y
from clean_strike import CleanStrike

if __name__ == "__main__":
									 # For INPUT_X
	print("starting game 1...")
	p1 = Player()                     # instance of player class
	p2 = Player()
	board = Game()					  # instance of game class

	
	game = CleanStrike(INPUT_X, p1, p2, board)       
	game.start()					   # call the method "start" of CleanStrike class
