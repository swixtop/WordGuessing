# Word Prediction Game

This Python script implements a simple word prediction game where the player needs to guess a word chosen randomly from a predefined list. The player has a limited number of guesses and points to make correct guesses or purchase letters from the word.

## How to Play

1. The game randomly selects a word from a list of predefined words.
2. The word is represented with underscores, indicating the number of letters in the word.
3. The player starts with a total of 12 points.
4. The player can choose to:
   - Make a guess: The player has a limited number of guesses (3) to guess the word. Each incorrect guess deducts 2 points.
   - Buy a letter: The player can buy a letter from the word by spending 2 points. The player can buy a maximum of 4 letters.
5. The game ends when the player correctly guesses the word, runs out of points, or exceeds the maximum number of guesses.

## Script Overview

- `word`: A random word selected from a predefined list.
- `unknown`: A string representing the word with underscores for unrevealed letters.
- `points`: Total points available to the player.
- `guess_count`: Number of guesses remaining.
- `word_count`: Number of letters the player can buy.
- `previous_letters`: List to keep track of previously purchased letters.

## Usage

1. Run the script.
2. Follow the prompts to make guesses or buy letters.
3. Try to guess the word correctly before running out of points or guesses.
