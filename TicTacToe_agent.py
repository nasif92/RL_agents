from Random_TicTacToe_Agent import Random_Agent
from MCTS_Agent import MonteCarloAgent

class TicTacToe:
	def __init__(self):
		# board of 9 pieces
		self.board = [[" "] * 3 for _ in range(3)]



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
		if 1 <= pos <= 9:
			row, col = divmod(pos - 1, 3)
			if self.board[row][col] == " ":
				self.board[row][col] = player
				return True
		return False
			

	def display_board(self):
		"""Displays the current state of the board"""
		for i,row in enumerate(self.board):
			print(" | ".join(row))
			if i < 2:
				print("-"*10)



		
def main():
    ttt = TicTacToe()
    random_agent = Random_Agent(ttt.board)
    mcts_agent = MonteCarloAgent(ttt.board)
    game_over = False
    player = "X"

    while not game_over:
        try:
            ttt.display_board()
            if player == "X":
                move = int(input(f"Player {player}'s turn. Make a move into an empty space (1-9): "))
                if ttt.make_move(player, move):
                    if ttt.check_win(player):
                        ttt.display_board()
                        print(f"Player {player} wins!")
                        game_over = True
                        continue
                else:
                    print("Invalid move. Try again.")
            else:
                mcts_agent.make_move(player)
                print("Random agent made their move.")
                if ttt.check_win(player):
                    ttt.display_board()
                    print("Random agent (Player O) wins!")
                    game_over = True

            player = "O" if player == "X" else "X"
        except KeyboardInterrupt:
            print("\nGame interrupted by user. Exiting...")
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
