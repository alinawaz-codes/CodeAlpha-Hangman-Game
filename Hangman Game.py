"""
CodeAlpha Python Internship - Task 1: Hangman Game
Author: Ali Nawaz

How the game works:
1. The computer picks a random word from a small list.
2. The player guesses one letter at a time.
3. Each wrong guess uses up one of 6 lives.
4. The player wins by guessing all letters, and loses when lives reach 0.
"""

import random


WORDS = ["python", "program", "computer", "keyboard", "internet",
         "software", "network", "variable", "function", "database"]

MAX_LIVES = 6  


def show_word(word, guessed_letters):
    """Return the word with underscores for letters not guessed yet.
    Example: word = 'python', guessed = ['p', 'o'] -> 'p _ _ _ o _'
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    """Run one full round of Hangman."""
    word = random.choice(WORDS)   
    guessed_letters = []        
    lives = MAX_LIVES

    print("\n=== HANGMAN ===")
    print("Guess the word, one letter at a time. You have", lives, "lives.")

    while lives > 0:
        print("\nWord:", show_word(word, guessed_letters))
        print("Lives left:", lives)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower().strip()

      
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly ONE letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.append(guess)

       
        if guess in word:
            print("Good guess!", guess, "is in the word.")
        else:
            lives -= 1
            print("Wrong guess!", guess, "is not in the word.")

       
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You won! The word was:", word)
            return

    
    print("\nGame over! You ran out of lives. The word was:", word)


def main():
    """Ask the player if they want to play again after each round."""
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()