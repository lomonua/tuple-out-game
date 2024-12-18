# Tuple Out Game

## Overview
The **Tuple Out Game** is a dice-based game where players take turns rolling three dice, with the goal of reaching a target score. During each turn, players can either keep certain dice or re-roll others. The game ends when a player reaches the target score.

## Game Rules:
- On each turn, a player rolls 3 dice.
- If the initial roll is three 6's then the player gets a jackpot and rewarded 50 points
- If the initial roll is three 1's then the player gets a penalty and loses 10 points
- If no special condition applies, decide whether to reroll or keep your dice.
- If you choose to reroll, non-fixed dice will be rolled again.
- If all three dice are the same (a "tuple"), the player loses their turn and scores no points.
- Otherwise, the player can keep any dice that show the same value (fixed dice) and re-roll the others.
- The player can continue re-rolling the dice until they decide to stop or all dice are fixed.
- The player's score for the turn is the sum of the dice that were kept.
- The game continues until a player reaches or exceeds the target score and wins.

## How To Play:
-When you open the code it will automatically roll the first dice for you
-It will then ask if you want to reroll if you have not tupled Out
-If you get fixed dice it will show you what numbers are fixed and ask if you want to roll again
-If you stop or tuple out it tells you how much you scored that round and your current score
-It will then move on to the second player
-The game will continue until one of the two players reaches 50
-At the end of the game it will show how many games each player has one
-It will also show the high scores from each game

## Special Functions
Tracks and displays player scores for each turn.
Maintains a game log, including winners and scores for multiple rounds.
Tracks and announces high scores across all games.

## Advanced Function
Shows how long it takes for the computer to process the turn