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
    print("Witaj w grze w wisielca!")

    slowo_do_odgadniecia = choose_random_word().lower();
    slowo_do_odgadniecia_set = set(slowo_do_odgadniecia)
    odgadniete = set()
    proba = 0
    max_prob = 6

    while True:

        if proba != 0:
            draw_hangman(proba)

        if proba == max_prob:
            print("Przekroczyłeś maksymalną liczbę prób. Koniec gry.")
            print("Poprawne słowo to: " + slowo_do_odgadniecia)
            break

        stan = "".join([litera if litera in odgadniete else "_" for litera in slowo_do_odgadniecia])
        print(stan)

        if set(stan) == slowo_do_odgadniecia_set:
            print("Gratulacje! Zgadłeś słowo: " + slowo_do_odgadniecia)
            break

        litera = input("Podaj literę: ").lower()

        if litera in odgadniete:
            print("Już podałeś literę " + litera + ". Spróbuj ponownie.")
            proba += 1
            print("Pozostało prób: " + str(max_prob - proba))
        elif litera in slowo_do_odgadniecia_set:
            print("Dobra robota! Podana litera jest w słowie.")
            odgadniete.add(litera)
        else:
            print("Niestety, podana litera nie występuje w słowie.")
            proba += 1
            print("Pozostało prób: " + str(max_prob - proba))

game()