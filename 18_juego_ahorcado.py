# -*- coding: utf-8 -*-

#ascci art
# https://en.wikipedia.org/wiki/ASCII_art
#Con mayusculas se definen las constantes como buena ptactica

import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']



WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'democracia',
    'teclado'
]

def random_word():
    idx = random.ranint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- *')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra'))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perditse! la palabra correcta era {}'.format(word))
                break

        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []
        try:
            hidden_word.index('-') #sino encuentra genera un error
        except ValueError:
            print('')
            print('Felicidades! Ganaste, La palabra es: {}'.format(word))
            break

if __name__ == '__main__':
    print('Bienvenidos A H O R C A D O S')
    run()