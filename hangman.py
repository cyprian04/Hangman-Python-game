import random

def choose_random_word():
    with open("all_words.txt", 'r') as file:
        all_words = file.read().splitlines()

    if not all_words:
        print("The file is empty. Please make sure it contains words.")
        return None

    return random.choice(all_words)

def draw_hangman(attempt):
    hangman_stages = [
        " -----\n |   |\n |\n |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |   |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |  / \n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |  / \\\n |\n_|___"
 ]
    print(hangman_stages[attempt])

def game():
    print("Welcome to hangman game!")

    guessing_word = choose_random_word().lower()
    guessing_word_set = set(guessing_word)
    guessed = set()
    attempt = 0
    max_attempts = 6

    while True:

        if attempt != 0:
            draw_hangman(attempt)

        if attempt == max_attempts:
            print("You have exceeded the maximum number of attempts. End of the game.")
            print("The correct word is: " + guessing_word)
            break

        stan = "".join([letter if letter in guessed else "_" for letter in guessing_word])
        print(stan)

        if set(stan) == guessing_word:
            print("Congratulations! You guessed the word: " + guessing_word)
            break

        letter = input("Enter a letter: ").lower()

        if letter in guessed:
            print("You've already entered the letter " + letter + ". try again.")
            attempt += 1
            print("remaining attempts: " + str(max_attempts - attempt))
        elif letter in guessing_word_set:
            print("Good job! The given letter is in the word.")
            guessed.add(letter)
        else:
            print("Unfortunately, the given letter does not appear in the word.")
            attempt += 1
            print("remaining attempts: " + str(max_attempts - attempt))

game()