import random 

class MonteCarloAgent:
	def __init__(self, board):
		"""
		This agent should be able to play any types of board games with a 2d structure randomly.
		Just pass the dimensions as I am doing
		"""
		self.board = board
	
	def simulate_game(self, board, player):
		"""
		Simulate a random game starting from the given board state.
		:param board: The current state of the game board
		:param player: The player whose turn it is
		:return: 1 if the player wins, 0 for a draw, -1 if the opponent wins
		"""
		current_player = player
		available_positions = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == " "]
		while available_positions:
			move = random.choice(available_positions)
			row, col = move
			board[row][col] = current_player

			if self.check_win_sim(board, current_player):
				return 1 if current_player == player else -1

			current_player = "X" if current_player == "O" else "O"
			available_positions = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == " "]
		return 0

	def check_win_sim(self, board, player):
		"""Check if the given player has won in the simulated board."""
		for row in board:
			if all(cell == player for cell in row):
				return True
		for col in range(3):
			if all(board[row][col] == player for row in range(3)):
				return True
		if all(board[i][i] == player for i in range(3)):
			return True
		if all(board[i][2 - i] == player for i in range(3)):
			return True
		return False

	def select_move(self, player):
		"""
		Select the best move using the Monte Carlo Tree Search (MCTS) algorithm.
		:param player: The symbol of the player (e.g., 'X' or 'O')
		:return: The selected move as (row, col)
		"""
		available_positions = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[0])) if self.board[i][j] == " "]
		if not available_positions:
			return None

		scores = {pos: 0 for pos in available_positions}
		simulations_per_move = 200

		for pos in available_positions:
			for _ in range(simulations_per_move):
				simulated_board = [row[:] for row in self.board]
				row, col = pos
				simulated_board[row][col] = player
				result = self.simulate_game(simulated_board, "X" if player == "O" else "O")
				scores[pos] += result

		best_move = max(scores, key=scores.get)
		return best_move

	def make_move(self, player):
		"""
		Make a move in the best location according to MCTS.
		:param player: The symbol of the player (e.g., 'X' or 'O')
		"""
		move = self.select_move(player)
		if move:
			row, col = move
			self.board[row][col] = player
