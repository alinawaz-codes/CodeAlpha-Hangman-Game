# CodeAlpha-Hangman-Game

A classic **Hangman game** in Python, built as **Task 1** of the **CodeAlpha Python Programming Internship**.

**Author:** Ali Nawaz

## How it works

The program chooses a secret word and shows it as underscores. The player guesses one letter at a time. Correct letters are revealed, and wrong guesses use up the limited attempts. The player wins by guessing the full word before the attempts run out.

## Features

- Chooses a secret word from a list
- Shows the word progress with underscores
- Tracks wrong guesses and remaining attempts
- Shows a win or lose message at the end

## How to Run

```
python hangman_game.py
```

## Example

```
Word: _ _ _ _ _ _
Guess a letter: a
Correct!
Word: _ a _ _ _ _
Guess a letter: z
Wrong! Attempts left: 5
```

## Concepts Used

- Loops and conditions
- Strings and lists
- User input
