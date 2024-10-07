# Bombsweeper Game

Welcome to my **Bombsweeper** game, developed from scratch using Python and pygame! This project is inspired by a puzzle mini-game I enjoyed playing, recreated based on my memory of the original. 

## Table of Contents
- [About the Game](#about-the-game)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

## About the Game
Bombsweeper is a fun puzzle mini-game where the goal is to flip over tiles that contain point multipliers while avoiding "bomb" tiles (which will reset your score to zero). The game mixes logic and chance, challenging the player to strategize and make the best choices with the given clues.

This version is based on my recollection of a similar mini-game, and has its own unique feel while maintaining the core puzzle mechanics.

## Features
- **Classic gameplay** inspired by a tile-flipping puzzle.
- **Dynamic tile grid** that randomly places point multipliers and bombs.
- **Score tracking** and **hint system** to help you make better guesses.
- **Simple and clean UI** built using pygame, making the game lightweight and enjoyable.
- **Randomized levels** with increasing difficulty for a new challenge every time.

## Installation
To play the game, you’ll need to have Python and pygame installed on your system.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flip-puzzle-game.git
    cd flip-puzzle-game
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## How to Play
1. The game grid consists of hidden tiles. Some tiles contain multipliers (1x, 2x, or 3x), while others contain bombs.
2. Use logic to flip over tiles that you think contain multipliers. Avoid the tiles with bombs as they will end the game!
3. Row and column hints indicate the number of bombs and the sum of the multipliers in that line.
4. Flip tiles and maximize your score until you clear the board or hit a bomb.
5. As you clear more levels, the difficulty increases, but so does your potential score.
6. You can progress up to a maximum of level 7, with a secret level 8. Be careful—hitting a bomb may cause the level to drop, adding an extra challenge to your progress.

## Future Improvements
- **Save/Load Feature:** Add functionality to save and resume games.
- **More Levels:** Introduce different levels with increasing complexity.
- **Leaderboard:** Introduce local leaderboard to beat your own highscores.

## Contributing
Contributions are welcome! If you have any ideas or find bugs, feel free to open an issue or submit a pull request. Let’s make this game even better together!

## Disclaimer
This project is a fan-made game inspired by a puzzle mini-game. It is not affiliated with, endorsed by, or connected to any official game developers or companies. All original assets, code, and design are created by the developer. The game and its mechanics are independently created and do not use any proprietary assets or code from the original inspiration.
