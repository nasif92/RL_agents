import random 

class MonteCarloAgent:
	def __init__(self, root, iterations=1000):
		"""
		This agent should be able to play any types of board games with a 2d structure randomly.
		Just pass the dimensions as I am doing
		"""
		self.root =  root
		self.iterations = iterations
	
	def simulate_mcts(self):
		for _ in range(self.iterations):
			node = self.root
			# Selection
			while node.children and node.is_fully_expanded():
				node = node.best_child()
			
			# Expansion
			if not self.is_terminal_state(node.state):
				node.expand()
				node = random.choice(node.children) # randomly pick a child node to explore

			# simulation
			simulation_state = node.state.clone()
			current_player = simulation_state.current_player
			while not self.is_terminal_state(simulation_state):
				valid_moves = [1 + i for i, cell in enumerate(
                    sum(simulation_state.board, [])
                ) if cell == " "]  # Flatten board and get valid moves (1-9)
				move = random.choice(valid_moves)
				simulation_state.make_move(current_player, move)
				current_player = 'O' if current_player == 'X' else 'X'

			# Determine the simulation result
			last_player = 'O' if current_player == 'X' else 'X'
			result = 1 if simulation_state.check_win(last_player) else 0
			if simulation_state.check_draw():
				result = 0.5  # Draw

			# Backpropagation
			while node:
				node.visits += 1
				node.wins += result
				result = 1 - result
				node = node.parent

	
	def is_terminal_state(self, state):
		"""
		Check if the current node is a terminal state
		"""
		return state.check_win('X') or state.check_win('O') or state.check_draw()

				