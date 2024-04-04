# Number Guessing Game

## Overview

This Python script implements a simple number guessing game. The user is prompted to enter a lower and upper bound for the range of numbers they want to guess from. The script then randomly selects a number within that range, and the user has a limited number of attempts to guess the correct number.

## Instructions

1. Run the script.
2. Enter the lower and upper bounds for the range of numbers you want to guess from.
3. The script will inform you of the minimum number of attempts you have to guess the correct number based on the range.
4. Start guessing numbers within the range.
5. If your guess is correct, the script will congratulate you and display the number of attempts it took.
6. If you exhaust all your attempts without guessing the correct number, the script will reveal the correct number.

## Usage

```bash
python number_guessing_game.py
```

## Dependencies

- Python 3.x

## Notes

- The number of attempts is limited to the minimum required based on the range provided by the user.
- The script utilizes the `random` module to generate random numbers and the `math` module for mathematical operations.

---
