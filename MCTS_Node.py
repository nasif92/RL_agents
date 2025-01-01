import math

class MCTSNode:
	def __init__(self, state, parent=None):
		self.state = state # The state of the current game
		self.parent = parent # parent node in of the node
		self.children = []
		self.visits = 0
		self.wins = 0
	
	def expand(self):
		if not self.children:
			possible_moves = self.state.get_valid_moves()
			for moves in possible_moves:
				new_state = self.state.clone()
				new_state.make_move( self.state.current_player,int(moves))
				self.children.append(MCTSNode(new_state, parent=self))
			

	def best_child(self, c_param=1.4):
		"""
		select the best child node based on the UCB1 formula
		"""
		best_child = None
		best_score = float('-inf')
		for child in self.children:
			if child.visits == 0:
				score = float('inf')  # Favor unvisited nodes
			else:
				# Calculate UCB1 score
				score = (
					child.wins / child.visits +
					c_param * math.sqrt(math.log(self.visits) / child.visits)
				)
			if score > best_score:
				best_score = score
				best_child = child
		return best_child
	
	def is_fully_expanded(self):
		return len(self.children) == len(self.state.get_valid_moves())
	