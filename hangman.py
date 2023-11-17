import random

def choose_random_word():
    with open("all_words.txt", 'r') as file:
        all_words = file.read().splitlines()

    if not all_words:
        print("The file is empty. Please make sure it contains words.")
        return None

    return random.choice(all_words)

def draw_hangman(proba):
    hangman_stages = [
        " -----\n |   |\n |\n |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |   |\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |\n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |  / \n |\n_|___",
        " -----\n |   |\n |   O\n |  /|\\\n |  / \\\n |\n_|___"
 ]

    print(hangman_stages[proba])

def game():
    print("Welcome to hangman game!")

    guessing_word = choose_random_word().lower();
    guessing_word_set = set(guessing_word)
    guessed = set()
    attempt = 0
    max_attempts = 6

    while True:

        if proba != 0:
            draw_hangman(attempt)

        if proba == max_attempts:
            print("Przekroczyłeś maksymalną liczbę prób. Koniec gry.")
            print("Poprawne słowo to: " + guessing_word)
            break

        stan = "".join([litera if litera in guessed else "_" for litera in guessing_word])
        print(stan)

        if set(stan) == guessing_word:
            print("Gratulacje! Zgadłeś słowo: " + guessing_word)
            break

        litera = input("Podaj literę: ").lower()

        if litera in guessed:
            print("Już podałeś literę " + litera + ". Spróbuj ponownie.")
            proba += 1
            print("Pozostało prób: " + str(max_attempts - proba))
        elif litera in guessing_word_set:
            print("Dobra robota! Podana litera jest w słowie.")
            guessed.add(litera)
        else:
            print("Niestety, podana litera nie występuje w słowie.")
            proba += 1
            print("Pozostało prób: " + str(max_attempts - proba))

game()