from Random_TicTacToe_Agent import Random_Agent
from MCTS_Agent import MonteCarloAgent
from MCTS_Node import MCTSNode

class TicTacToe:
	def __init__(self):
		# board of 9 pieces
		self.board = [[" "] * 3 for _ in range(3)]
		self.current_player = "X"  # Player X starts the game

	def get_valid_moves(self):
		"""
		Returns a list of valid moves for the current state of the game.
		:return: A list of tuples, where each tuple represents a valid move (row, column)
		"""
		valid_moves = []
		for i, row in enumerate(self.board):
			for j, cell in enumerate(row):
				if cell == " ":  # Check for empty cells
					valid_moves.append(3 * i + j + 1)  # Convert (row, col) to 1-9 format
		return valid_moves
	
	def clone(self):
		"""
		Creates a deep copy of the current game state.
		:return: A new TicTacToe instance with the same board and current player.
		"""
		cloned_game = TicTacToe()  # Create a new TicTacToe instance
		cloned_game.board = [row[:] for row in self.board]  # Deep copy the board
		cloned_game.current_player = self.current_player  # Copy the current player
		return cloned_game

	def check_win(self, player):
		"""
		Checks if the given player has won the game.
		:param player: The symbol of the player (e.g., 'X' or 'O')
		:return: True if the player has won, otherwise False
		"""
		# Check rows
		for row in self.board:
			if all(cell == player for cell in row):
				return True

		# Check columns
		for col in range(3):
			if all(self.board[row][col] == player for row in range(3)):
				return True

		# Check diagonals
		if all(self.board[i][i] == player for i in range(3)):
			return True
		if all(self.board[i][2 - i] == player for i in range(3)):
			return True

		return False
	
	def make_move(self, player, pos):
		pos = int(pos)
		if 1 <= pos <= 9:
			row, col = divmod(pos - 1, 3)
			if self.board[row][col] == " ":
				self.board[row][col] = player
				return True
		return False
			
	def check_draw(self):
		return all(cell != " " for row in self.board for cell in row) and not self.check_win('X') and not self.check_win('O')

	def display_board(self):
		"""Displays the current state of the board"""
		for i,row in enumerate(self.board):
			print(" | ".join(row))
			if i < 2:
				print("-"*10)



		
def main():
	ttt = TicTacToe()
	random_agent = Random_Agent(ttt.board)
	root = MCTSNode(ttt)
	mcts_agent = MonteCarloAgent(root, iterations=1000)
	game_over = False
	player = "X"

	while not game_over:
		try:
			ttt.display_board()  # Display the board at the start of each turn

			if player == "X":
				# Human player's turn
				move = input(f"Player {player}'s turn. Enter your move (1-9): ")
				try:
					move = int(move)
					if not 1 <= move <= 9:
						raise ValueError
					
					if ttt.make_move(player, move):  # Make the move for the human player
						if ttt.check_win(player):
							ttt.display_board()
							print(f"Player {player} wins!")
							game_over = True
							continue
						elif ttt.check_draw():
							ttt.display_board()
							print("It's a draw!")
							game_over = True
							continue
					else:
						print("Invalid move. Try again.")
						continue
				except (ValueError, IndexError):
					print("Invalid input format! Enter a number between 1 and 9.")
					continue

			else:
				# MCTS agent's turn
				print("MCTS agent is thinking...")
				mcts_agent.simulate_mcts()  # Run MCTS to find the best move
				best_move_node, best_move_position = mcts_agent.root.best_child(c_param=0)  # Choose the best move
				print(f"MCTS agent (Player {player}) selects move: {best_move_position}, with win rate: {best_move_node.wins / best_move_node.visits}")
				
				ttt.make_move(player, best_move_position)  # Make the move for the MCTS agent
				mcts_agent.root = best_move_node  # Update the root of the tree

				if ttt.check_win(player):
					ttt.display_board()
					print("MCTS agent (Player O) wins!")
					game_over = True
					continue
				elif ttt.check_draw():
					ttt.display_board()
					print("It's a draw!")
					game_over = True
					continue

			# Switch players
			print("Switcihng players")
			player = "O" if player == "X" else "X"
		except KeyboardInterrupt:
			print("\nGame interrupted!")
			break

if __name__ == "__main__":
    main()
