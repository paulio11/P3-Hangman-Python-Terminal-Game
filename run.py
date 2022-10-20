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


# ASCII art
GAME_HEADER = '''

    ▄█  █▄       ▄██████ ███▄▄▄      ▄████▄    ▄▄▄███▄▄▄      ▄██████ ███▄▄▄
   ███  ███     ███  ███ ███▀▀██▄   ███  ███ ▄██▀▀███▀▀██▄   ███  ███ ███▀▀██▄
   ███  ███     ███  ███ ███  ███   ███  █▀  ███  ███  ███   ███  ███ ███  ███
  ▄███▄▄███▄▄   ███  ███ ███  ███  ▄███      ███  ███  ███   ███  ███ ███  ███
 ▀▀███▀▀███▀  ▀█████████ ███  ███ ▀▀███ ███▄ ███  ███  ███ ▀█████████ ███  ███
   ███  ███     ███  ███ ███  ███   ███  ███ ███  ███  ███   ███  ███ ███  ███
   ███  ███     ███  ███ ███  ███   ███  ███ ███  ███  ███   ███  ███ ███  ███
   ███  █▀      ███  █▀   ▀█  █▀    ██████▀   ▀█  ███  █▀    ███  █▀   ▀█  █▀
'''
WIN_HEADER = '''

  ▄█   █▄     ▄██████  ▄█       ▄█       ██████▄   ▄████▄  ███▄▄      ▄██████
 ███   ███   ███  ███ ███      ███       ███ ▀███ ███  ███ ███▀▀██▄   ███  ███
 ███   ███   ███  █▀  ███      ███       ███  ███ ███  ███ ███  ███   ███  █▀
 ███   ███  ▄███▄▄    ███      ███       ███  ███ ███  ███ ███  ███  ▄███▄▄
 ███   ███ ▀▀███▀▀    ███      ███       ███  ███ ███  ███ ███  ███ ▀▀███▀▀
 ███   ███   ███  █▄  ███      ███       ███  ███ ███  ███ ███  ███   ███  █▄
 ███▄█▄███   ███  ███ ███▌   ▄ ███▌   ▄  ███ ▄███ ███  ███ ███  ███   ███  ███
  ▀██▀██▀    ████████ █████▄██ █████▄██  ██████▀   ▀████▀   ▀█  █▀    ████████
'''
FAIL_HEADER = '''

     ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒
         ░       ▒                 ░          ░         ░     ░      ░
'''
HANGMAN_STAGES = [
    '''


                                                          ▒▒▒▒▒▒▒▒
               █▄██▄█                                    ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█                            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███                               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''

                                             █
                                             █            ▒▒▒▒▒▒▒▒
               █▄██▄█                        █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                             █
                                             █            ▒▒▒▒▒▒▒▒
               █▄██▄█                        █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                             █            ▒▒▒▒▒▒▒▒
               █▄██▄█                        █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                        █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                   |    █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|    █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█         /     █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█         / \   █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
]


def set_word():
    '''
    Picks a random word from Google sheet.
    Makes string of _ based on length of random word.
    '''
    global game_word, hidden_word

    word_list = WORD_SHEET.col_values(1)
    game_word = random.choice(word_list)
    hidden_word = '_' * len(game_word)


def user_input():
    '''
    While game is running:
    - Displays guessed letters and player health.
    - Takes input from player as guess.
    - Passes valid guess to check_guess function.
    - Calls game_display to redraw game.
    '''
    global game_over, player_lives

    guessed_letters = []
    game_over = False
    player_lives = 9

    while game_over is False:

        guessed_letters_str = ' '.join(guessed_letters)
        life_bar = ' ♥' * player_lives

        print(f'Guessed letters: {guessed_letters_str : <43}{life_bar : >18}')
        print('-' * TERM_WIDTH)
        guess = input('Guess a letter: ').upper()

        def redraw():
            time.sleep(1)
            game_display(GAME_HEADER)

        if guess == 'HELP':
            print(game_word)
            redraw()
        elif not guess.isalpha() or len(guess) > 1:
            print('Invalid guess')
            redraw()
        elif guess in guessed_letters:
            print('Letter already guessed, try another')
            redraw()
        else:
            guessed_letters.append(guess)
            guessed_letters.sort()
            check_guess(guess)


def check_guess(guess):
    '''
    Checks for correct or incorrect guess.
    Updates varibles as necessary.
    Calls game_display to redraw game.
    '''
    global player_lives, game_stage, game_over

    if guess in game_word:
        print('Correct guess!')
        update_hidden_word(guess)
    elif guess not in game_word and game_stage != 8:
        print('Incorrect guess!')
        player_lives -= 1
        game_stage += 1
    else:
        # Game fail trigger
        print('Game over!')
        player_lives -= 1
        game_stage += 1
        game_over = True

    time.sleep(1)
    
    if game_over is False:
        game_display(GAME_HEADER)


def update_hidden_word(guess):
    '''
    Takes a correct guess and updates hidden_word.
    If hidden_word complete -> game_over = True.
    '''
    # to do - still only works for the first occurrence of letter in word
    global hidden_word, game_over

    hidden_word_arr = list(hidden_word)
    pos_of_guess = game_word.index(guess)
    hidden_word_arr[pos_of_guess] = guess
    hidden_word = ''.join(hidden_word_arr)

    # Game win trigger
    if '_' not in hidden_word:
        game_over = True
        game_display(WIN_HEADER)


def game_display(header):
    '''
    Prints the following:
    - Header based on current state.
    - Hangman word.
    - Current game stage.
    '''
    os.system('clear')

    print(header)
    print('Mystery word: '.center(TERM_WIDTH))
    print()
    print(f'{hidden_word} ({len(game_word)})'.center(TERM_WIDTH))
    print(HANGMAN_STAGES[game_stage])


def main():
    '''
    Main program function.
    '''
    set_word()
    game_display(GAME_HEADER)
    user_input()


main()
