import math

class MCTSNode:
	def __init__(self, state, parent=None, move=None):
		self.state = state # The state of the current game
		self.parent = parent # parent node in of the node
		self.children = []
		self.visits = 0
		self.move = move
		self.wins = 0
	
	def expand(self):
		if not self.children:
			possible_moves = self.state.get_valid_moves()
			for moves in possible_moves:
				new_state = self.state.clone()
				new_state.make_move( self.state.current_player,int(moves))
				child_node = MCTSNode(new_state, parent=self)
				child_node.best_child_position = int(moves)  # Associate move with child node
				self.children.append(child_node)
			

	def best_child(self, c_param=1.4):
		"""
		select the best child node based on the UCB1 formula
		"""
		best_child = None
		best_move = None	
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
				best_move = child.best_child_position
		return best_child, best_move
	
	def is_fully_expanded(self):
		return len(self.children) == len(self.state.get_valid_moves())
	