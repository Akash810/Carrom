class Game:
	# initialize the game 
	def __init__(self):
		self.red_coins = 1
		self.black_coins = 9
	# fetch the numbers of red coins
	def get_red_coins(self):
		"""
		Returns the current number of red coins
		:return (Integer): Current number of red coins
		"""
		return self.red_coins

	def set_red_coins(self, red_coins):
		"""
		Sets the current number of red coins
		:param red_coins (Integer): Number of red coins
		"""
		self.red_coins = red_coins

	def get_black_coins(self):
		"""
		Returns the current number of black coins
		:return (Integer): Current number of black coins
		"""
		return self.black_coins

	def set_black_coins(self, black_coins):
		"""
		Sets the current number of black coins
		:param black_coins (Integer): Number of black coins
		"""
		self.black_coins = black_coins

