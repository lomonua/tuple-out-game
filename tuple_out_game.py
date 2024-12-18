import random
import time

class TupleOutGame:
    def __init__(self, players, target_score):
        self.players = players  # List of player names
        self.target_score = target_score  # Score needed to win
        self.scores = {player: 0 for player in players}  # Track scores
        self.high_scores = 0  # Highest score achieved in any game
        self.game_wins = {player: 0 for player in players}  # Number of games won by each player
        self.game_log = []  # Log to store each game's results
    
    def roll_dice(self, num):
        return random.choices(range(1, 7), k=num)  # Simulates 'num' rolls of a 6-sided die
    
    def play_turn(self, player):
        start_time = time.process_time()  # Start time tracking
        print(f"\n{player}'s turn!")
        dice = self.roll_dice(3)
        print(f"Initial roll: {dice}")

        # Jackpot bonus for rolling three 6s
        if dice == [6, 6, 6]:  
            print("Jackpot! Triple six bonus! You earn 50 extra points!")
            elapsed_time = time.process_time() - start_time
            print(f"Time taken for {player}'s turn: {elapsed_time:.4f} seconds")  
            return 50  # Return bonus score

        # Penalty for rolling three 1s
        if dice == [1, 1, 1]:  
            print("Ouch! Triple ones! You lose 10 points.")
            elapsed_time = time.process_time() - start_time
            print(f"Time taken for {player}'s turn: {elapsed_time:.4f} seconds")  
            return -10  # Deduct penalty points
        
        # Regular "tuple out" logic: all dice are the same, but not triple 6s or 1s
        if len(set(dice)) == 1:
            print("Tuple out! No points this turn.")
            elapsed_time = time.process_time() - start_time
            print(f"Time taken for {player}'s turn: {elapsed_time:.4f} seconds")  
            return 0
        
        # Fixed dice and reroll mechanics
        while True:
            fixed_dice = [num for num in dice if dice.count(num) > 1]
            reroll_indices = [i for i, num in enumerate(dice) if dice.count(num) == 1]
            
            if not reroll_indices:  # All dice are fixed, stop turn
                break
            
            print(f"Fixed dice: {fixed_dice}")
            reroll = input("Do you want to re-roll? (yes/no): ").strip().lower()
            if reroll == "no":
                break
            
            # Re-roll the non-fixed dice using random.choices
            for i in reroll_indices:
                dice[i] = random.choice(range(1, 7))  # Roll one die per position
            print(f"Re-rolled dice: {dice}")
        
        total_score = sum(dice)
        print(f"{player} ends the turn with {total_score} points.")
        elapsed_time = time.process_time() - start_time  # End time tracking
        print(f"Time taken for {player}'s turn: {elapsed_time:.4f} seconds")  # Print processing time
        return total_score

    def play_game(self):
        while True:
            start_time = time.process_time()  # Start time tracking for the game
            for player in self.players:
                turn_score = self.play_turn(player)
                self.scores[player] += turn_score
                
                print(f"{player}'s total score: {self.scores[player]}")
                
                if self.scores[player] >= self.target_score:
                    print(f"\n{player} wins the game with {self.scores[player]} points!")

                    # Update high score if this player's score is the highest so far
                    if self.scores[player] > self.high_scores:
                        self.high_scores = self.scores[player]
                        print(f"New high score: {self.high_scores} points!")

                    # Update the player's win count
                    self.game_wins[player] += 1

                    # Record the game result
                    self.game_log.append({
                        "winner": player,
                        "scores": self.scores.copy()
                    })
                    
                    # Display overall stats
                    print("\nGame Over! Here are the overall stats:")
                    for p, wins in self.game_wins.items():
                        print(f"{p} has won {wins} game(s).")
                    print(f"Current high score: {self.high_scores} points.")

                    # Display game log
                    print("\nGame Log:")
                    for i, game in enumerate(self.game_log, 1):
                        print(f"Game {i}: Winner - {game['winner']}, Scores - {game['scores']}")
                    
                    # Ask if players want to play again
                    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                    if play_again == "yes":
                        self.scores = {player: 0 for player in self.players}
                        print("\nStarting a new game...")
                        break
                    else:
                        elapsed_time = time.process_time() - start_time  # End time tracking
                        print(f"Thanks for playing! Total game processing time: {elapsed_time:.4f} seconds")  # Print processing time
                        return

players = ["Player 1", "Player 2"]
target_score = 75
game = TupleOutGame(players, target_score)
game.play_game()
