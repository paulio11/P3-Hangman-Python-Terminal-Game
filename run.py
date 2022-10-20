# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time


# Constant Variables
TERM_WIDTH = 80


# Game Variables
game_stage = 0


# Variables for Google Sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')
WORD_SHEET = SHEET.worksheet('word_sheet')


def set_word():
    '''
    Picks a random word from Google sheet.
    Creates a string of _ to match length.
    '''
    word_list = WORD_SHEET.col_values(1)
    global game_word
    game_word = random.choice(word_list)


def user_input():
    '''
    Takes input from player
    '''
    guessed_letters = []
    global game_over, player_lives
    game_over = False
    player_lives = 9

    while game_over is False:

        guessed_letters_str = ' '.join(guessed_letters)
        life_bar = ' ♥' * player_lives

        os.system('clear')

        print(f'Guessed letters: {guessed_letters_str : <43}{life_bar : >18}')
        print('-' * TERM_WIDTH)
        guess = input('Guess a letter: ').upper()

        if guess == 'HELP':
            print(game_word)
        elif not guess.isalpha() or len(guess) > 1:
            print('Invalid guess')
        elif guess in guessed_letters:
            print('Letter already guessed, try another')
        else:
            guessed_letters.append(guess)
            guessed_letters.sort()
            check_guess(guess)

        time.sleep(1)


def check_guess(guess):
    '''
    Checks guess.
    '''
    global player_lives, game_stage, game_over

    if guess in game_word:
        print('Correct guess!')
    elif guess not in game_word and game_stage != 8:
        print('Incorrect guess!')
        player_lives -= 1
        game_stage += 1
    else:
        print('Game over!')
        player_lives -= 1
        game_stage += 1
        game_over = True
        # still shows one heart


set_word()
user_input()
