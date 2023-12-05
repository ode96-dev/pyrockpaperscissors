import random
import sys

class RockPaperScissors:
    def __init__(self):
        print("Welcome to PyRockPaperScissors")
        self.moves:dict = {"Rock":"🪨", "Paper":"📄", "Scissors":"✂️"}
        self.valid_moves: list[str] = list(self.moves.keys())
    
    def play_game(self):
        user_move: str = input("Rock, Paper, and Scissors: >>")
        if user_move == "exit":
            print("Thanks for playing!")
            sys.exit()
        if user_move not in self.valid_moves:
            print("Invalid move")
            return self.play_game
        ai_move:str = random.choice(self.valid_moves)
        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_move(self, user_move:str, ai_move:str):
        print("================================================================")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[user_move]}")
        print("================================================================")

    def check_move(self, user_move:str, ai_move:str):
        if user_move == ai_move:
            print("This is a tie!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print("You win")
        elif user_move == 'scissors' and ai_move == 'paper':
            print("You win")
        elif user_move == 'paper' and ai_move == 'rock':
            print("You win")
        elif user_move == 'paper' and ai_move == 'scissors':
            print("You win")
        else:
            print("AI wins")

if __name__ == '__main__':
    rock_paper_scissors = RockPaperScissors()

    while True:
        rock_paper_scissors.play_game()