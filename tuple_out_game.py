import random

class TupleOutGame:
    def __init__(self, players, target_score):
        self.players = players  # List of player names
        self.target_score = target_score  # Score needed to win
        self.scores = {player: 0 for player in players}  # Track scores
    
    def roll_dice(self, num):
        # Use random.choices to simulate rolling 'num' dice
        return random.choices(range(1, 7), k=num)

    
    def play_turn(self, player):
        print(f"\n{player}'s turn!")
        dice = self.roll_dice(3)
        print(f"Initial roll: {dice}")
        
        while True:
            if len(set(dice)) == 1:  # Check for "tuple out"
                print("Tuple out! No points this turn.")
                return 0
            
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
                dice[i] = random.choices(range(1, 7), k=1)[0]
            print(f"Re-rolled dice: {dice}")
    
        total_score = sum(dice)
        print(f"{player} ends the turn with {total_score} points.")
        return total_score

def play_game(self):
    while True:
        for player in self.players:
            turn_score = self.play_turn(player)
            self.scores[player] += turn_score
            
            print(f"{player}'s total score: {self.scores[player]}")
            
            if self.scores[player] >= self.target_score:
                print(f"\n{player} wins the game with {self.scores[player]} points!")
                return



players = ["Player 1", "Player 2"]
target_score = 50
game = TupleOutGame(players, target_score)
game.play_game()
