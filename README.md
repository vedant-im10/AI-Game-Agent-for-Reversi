# 🤖 AI - Game Agent for Reversi (Othello) Strategy

This project implements a game-playing agent to compete in the strategic game of Reversi (Othello) using AI techniques like the Minimax algorithm and Alpha-Beta pruning. The agent was designed to compete against other bots in a controlled environment and ranked in the **top 50** out of approximately 600 participants based on its performance in head-to-head matches.

## 🧠 Features

- **Minimax Algorithm**: The agent uses the minimax algorithm to make optimal moves by evaluating possible future game states.
- **Alpha-Beta Pruning**: Implements alpha-beta pruning to optimize the minimax algorithm, reducing the number of nodes evaluated and speeding up the decision-making process.
- **Iterative Deepening**: Enhances time efficiency by performing depth-limited searches, ensuring that the agent operates within the given time constraints.
- **Heuristic Evaluation**: Uses a custom evaluation function that prioritizes board positions based on strategic importance, such as corners and edges.

## 🎮 Game Rules

- **Board Size**: The game is played on a 12x12 grid, which is larger than the standard Othello board size.
- **Player Roles**: Two players (X and O) compete to control the majority of the board. Player X always plays second but receives a +1 bonus at the end of the game for balancing purposes.
- **Valid Moves**: A move must surround one or more of the opponent’s pieces in any direction (horizontal, vertical, or diagonal).
- **Winning Condition**: The game ends when no more valid moves are available for both players. The player with the most pieces on the board wins, with player X receiving a +1 bonus. In case of a tie in piece count, the player with more time left wins.

## 🚀 Performance

The agent was tested in a large-scale competition, achieving a **top 50 rank** among nearly 600 other agents by playing multiple rounds of Reversi against other students' bots.
