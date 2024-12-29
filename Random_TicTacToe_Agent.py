import random

class Random_Agent:
	def __init__(self, board):
		"""
		This agent should be able to play any types of board games with a 2d structure randomly.
		Just pass the dimensions as I am doing
		"""
		self.board = board

	def make_move(self, player):
		"""
		make a move in a random empty location in the board
		"""
		empty_positions = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[0])) if self.board[i][j] == " "]
		if empty_positions:
			row, col = random.choice(empty_positions)
			self.board[row][col] = player


