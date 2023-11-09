# Tic Tac Toe Game with Tkinter

## Introduction
This Python program implements a Tic Tac Toe game using the Tkinter library. The game supports both two-player and one-player modes. In one-player mode, the computer uses a predefined function for its moves.

## Requirements
- Python 3.x
- Tkinter library

## How to Run
1. Ensure you have Python installed on your system.
2. Run the following command in your terminal or command prompt:
   ```
   python tictactoemain.py
   ```

## Features
- **Two-Player Game:**
  - Players take turns clicking on the grid to place their X or O.
  - The game declares the winner when a player gets three in a row.
  - If the grid is filled without a winner, the game ends in a draw.

- **One-Player Game:**
  - Player faces off against the computer.
  - The computer's moves are determined by a predefined function.
  - Enjoy a challenging game against an AI opponent.

## Customization
- You can easily modify the predefined function for the computer's moves by editing the `nextpos()` function in singleplayer.py.

## Code Structure
- `tictactoemain.py`: Main Python script containing the game logic and Tkinter GUI setup.

Feel free to explore and modify the code to suit your preferences. Enjoy playing Tic Tac Toe!
