# import game
# carrom = game.Game()
class Player:
	# initialize player
	def __init__(self):
		self.points = 0              
		self.count = 0
		self.successive_num = []

	def get_points(self):
		"""
		Returns the current points of player
		:return (Integer): Current number of player point
		"""
		return self.points

	def set_count(self, count):
		"""
		Sets the current number of count
		:param count (Integer): Number of count
		"""
		self.count = count

	def get_count(self):
		"""
		Returns the current count
		:return (Integer): Current value of count
		"""
		return self.count	
	def get_successive_num(self):
		return self.successive_num

	def stike(self):
		"""
		Returns the  point after increment by 1
		:return (Integer): Current value of point
		"""
		self.points += 1

	def multiStrike(self):
		"""
		Returns the  point after increment by 2
		:return (Integer): Current value of point
		"""					
		self.points += 2

	def redStrike(self):	
		"""
		Returns the  point after increment by 3
		:return (Integer): Current value of point
		"""					
		self.points += 3

	def strikerStrike(self):
		"""
		Returns the  point after decrement by 1
		:return (Integer): Current value of point
		"""	
		self.points -= 1

	def defunctionCoin(self):	
		"""
		Returns the  point after decrement by 1
		:return (Integer): Current value of point
		"""					
		self.points -= 2
	

	def defunctionCoinScore(self, value, carrom):
		points = self.defunctionCoin()
		if value[1] == "Red":
			carrom.set_red_coins(carrom.get_red_coins() - 1)
		if value[1] == "Black":
			carrom.set_black_coins(carrom.get_black_coins() - 1)		

	
	def successiveTurn(self):
		"""
		Returns the  point after decrement by 1 
		:return (Integer): Current value of point
		"""	
		self.points -= 1

	def multiStrikeScore(self, chance, carrom):
		self.multiStrike()
		if chance[1] == "Red" and chance[2] == "Red":
			self.redStrike()
			self.redStrike()
			carrom.set_red_coins(carrom.get_red_coins() - 2)
			return
		if chance[1] == "Red":
			self.redStrike()
			carrom.set_red_coins(carrom.get_red_coins() - 1)
		if chance[2] == "Red":
			self.redStrike()
			carrom.set_red_coins(carrom.get_red_coins() - 1)
		if chance[1] == "Black":
			# points = self.stike()
			carrom.set_black_coins(carrom.get_black_coins() - 1)
		if chance[2] == "Black":
			# points = self.stike()
			carrom.set_black_coins(carrom.get_black_coins() - 1)

	def strikeScore(self, chance, carrom):
		# self.stike()
		if chance[1] == "Red":
			points = self.redStrike()
			carrom.set_red_coins(carrom.get_red_coins() - 1)
		else:
			carrom.set_black_coins(carrom.get_black_coins() - 1);

	def foulThreeTimes(self, i):
		self.count += 1
		if self.count%3 == 0:
			self.points -= 1
		
	def emptyChance(self,i):
		self.successive_num.append(i)
		if len(self.successive_num) >= 3:
			if self.successive_num[len(self.successive_num)-1] + self.successive_num[len(self.successive_num)-3] == 2*self.successive_num[len(self.successive_num)-2]:
				self.successiveTurn()	
		
	def changePlayersPoints(self,carrom, chance, index):
		if chance[0] == 1:
			self.strikeScore(chance, carrom)
		if chance[0] == 2:
			self.multiStrikeScore(chance, carrom)
		if chance[0] == 3:
			self.redStrike()
			carrom.set_red_coins(carrom.get_red_coins() - 1)
		if chance[0] == 4:
			self.strikerStrike()
		if chance[0] == 5:
			self.defunctionCoinScore(chance, carrom)
		if chance[0] in [4,5,6]:	
			self.emptyChance(index)
		if chance[0] in [4,5]:
			self.foulThreeTimes(index)
