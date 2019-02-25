class CleanStrike:
	# initialize the CleanStrike
	def __init__(self, chances, player1, player2, board):
		self.chances = chances
		self.player1 = player1
		self.player2 = player2
		self.board = board

	def start(self):
		"""
		Starts the game
		"""
		if len(self.chances['input']) < 1:
			return "INVALID INPUT" 
		for i in range(len(self.chances['input'])):
			# Alternate chance of player 
			if i%2 == 0:
				self.player1.changePlayersPoints(self.board, self.chances['input'][i], i)
			else:
				self.player2.changePlayersPoints(self.board, self.chances['input'][i],i)

			print self.player1.get_points() , self.player2.get_points(), self.board.get_black_coins(), self.board.get_red_coins()

			if self.board.get_black_coins() < 0 or self.board.get_red_coins() < 0:
				print "INVALID INPUT"
				return 0

			 # winning condition for player2
			if (self.player2.get_points() - self.player1.get_points() > 3) and self.player2.get_points() >= 5:
				print("PLAYER2 WON THE MATCH")
				return 0

			# winning condition for player1
			if (self.player1.get_points() - self.player2.get_points() > 3) and self.player1.get_points() >= 5:
				print("PLAYER1 WON THE MATCH")		
				return 0
			if self.board.get_black_coins() == 0 and self.board.get_red_coins() == 0:
				print "DRAW" 
		print "DRAW"		