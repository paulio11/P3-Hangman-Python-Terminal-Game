# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
import math


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
SCOREBOARD_TITLE = '''
             _____                    _                         _
            / ____|                  | |                       | |
           | (___   ___ ___  _ __ ___| |__   ___   __ _ _ __ __| |
            \___ \ / __/ _ \| '__/ _ \ '_ \ / _ \ / _` | '__/ _` |
            ____) | (_| (_) | | |  __/ |_) | (_) | (_| | | | (_| |
           |_____/ \___\___/|_|  \___|_.__/ \___/ \__,_|_|  \__,_|
 '''
INSTRUCTIONS_TITLE = '''
            _   _                 _____      ______ _
           | | | |               |_   _|     | ___ \ |
           | |_| | _____      __   | | ___   | |_/ / | __ _ _   _
           |  _  |/ _ \ \ /\ / /   | |/ _ \  |  __/| |/ _` | | | |
           | | | | (_) \ V  V /    | | (_) | | |   | | (_| | |_| |
           \_| |_/\___/ \_/\_/     \_/\___/  \_|   |_|\__,_|\__, |
                                                             __/ |
                                                            |___/
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
MENU_ART = '''

                           __________   ▄▄▄▄▄▄
                          | HELP ME! |  |    █
                           ¯¯¯¯¯¯¯¯¯¯\       █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  \O/   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█          |    █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███         / \   █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''


def cprint(a):
    '''
    Take parameter and print it center aligned.
    '''
    terminal_width = 80

    print(a.center(terminal_width))


def reset_game():
    '''
    Resets variables.
    '''
    global player_lives, game_over, game_win, game_stage

    game_stage = 0
    game_win = False
    game_over = False
    player_lives = 9


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
    global game_over, player_lives, start_time

    guessed_letters = []
    start_time = time.time()

    while game_over is False:

        guessed_letters_str = ' '.join(guessed_letters)
        life_bar = ' ♥' * player_lives

        print(f'Guessed letters: {guessed_letters_str : <43}{life_bar : >18}')
        print('-' * 80)
        guess = input('Guess a letter: ').upper()

        def redraw():
            # time.sleep(1)
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
    global player_lives, game_stage, game_over, end_time

    if guess in game_word:
        print('Correct guess!')
        update_hidden_word(guess)
    elif guess not in game_word and game_stage != 8:
        print('Incorrect guess!')
        player_lives -= 1
        game_stage += 1
    else:
        # Game fail trigger
        end_time = time.time()
        player_lives -= 1
        game_stage += 1
        game_over = True
        game_display(FAIL_HEADER)

    # time.sleep(1)
    
    if game_over is False:
        game_display(GAME_HEADER)


def update_hidden_word(guess):
    '''
    Takes a correct guess and updates hidden_word.
    If hidden_word complete -> game_over = True.
    '''
    # to do - still only works for the first occurrence of letter in word
    global hidden_word, game_over, game_win, end_time

    hidden_word_arr = list(hidden_word)
    pos_of_guess = game_word.index(guess)
    hidden_word_arr[pos_of_guess] = guess
    hidden_word = ''.join(hidden_word_arr)

    # Game win trigger
    if '_' not in hidden_word:
        end_time = time.time()
        game_win = True
        game_over = True
        game_display(WIN_HEADER)


def calculate_score():
    '''
    Calculates and prints player score based on lives, word length, and time.
    '''
    global seconds, score

    seconds = math.floor(end_time - start_time)
    score = math.ceil((len(game_word) * 500) + (player_lives * 1000) / seconds)
    left_text = 'Congratulations!'
    mid_text = f'SCORE: {score}'
    right_text = f'TIME: {seconds}s'

    print(f'{left_text : <30}{mid_text : ^20}{right_text : >30}')


def scoreboard():
    '''
    Slices last 5 scores from sheet.
    Sorts scores in descending order.
    A for loop prints the array vaules line by line.
    '''
    score_sheet = SHEET.worksheet('scoreboard')
    score_data = score_sheet.get_all_values()
    score_slice = score_data[-1:-6:-1]
    score_slice = sorted(score_slice, key=lambda x: int(x[1]), reverse=True)
    rank = 1
    rank_h = 'RANK'
    name_h = 'NAME'
    score_h = 'SCORE'
    time_h = 'TIME'

    os.system('clear')

    print(SCOREBOARD_TITLE)
    cprint('Last 5 Scores')
    print()

    headers = f'{rank_h : <6}{name_h : <12}{score_h : <9}{time_h : <5}'

    cprint(headers)
    cprint('=================================')
    
    for line in score_slice:
        row = f'{rank : <6}{line[0] : <12}{line[1] : <9}{line[2] : <5}'
        cprint(row)
        cprint('---------------------------------')
        rank += 1

    print()
    input('Press ENTER to return to the menu...')
    main_menu()

def update_scoreboard():
    '''
    Updates scoreboard sheet.
    '''
    global name

    name = input('Please enter your name: ').capitalize()[:10]
    score_sheet = SHEET.worksheet('scoreboard')

    score_sheet.append_row([name, score, seconds, game_word])

    end_screen()


def game_display(header):
    '''
    Prints the following:
    - Header based on current state.
    - Hangman word.
    - Current game stage.

    At the end of a game shows text based on win or fail.
    '''
    global game_over

    os.system('clear')

    print(header)
    cprint('Mystery word: ')
    print()
    cprint(f'{hidden_word} ({len(game_word)})')
    print(HANGMAN_STAGES[game_stage])

    if game_win:
        calculate_score()
        print('-' * 80)
        update_scoreboard()
    elif game_over and game_win is False:
        left_text = 'Oh dear you died!'
        right_text = f'The mystery word was {game_word}.'
        print(f'{left_text : <40}{right_text : >40}')
        print('-' * 80)
        input('Press ENTER to return to the menu...')
        main_menu()


def end_screen():
    '''
    Confirms name entry into scoreboard.
    Thanks player and returns to menu after input.
    '''
    global name

    os.system('clear')

    print('\n' * 12)
    cprint(f'Thank you for playing {name}!')
    cprint('Your name and score have been uploaded.')
    print()    
    cprint('Press ENTER to return to the menu...')
    input('')
    main_menu()


def instructions():
    '''
    Print game instructions.
    '''
    os.system('clear')

    print(INSTRUCTIONS_TITLE)
    print('This is how to play.....')
    input('Press ENTER to return to the menu...')
    main_menu()


def main_menu():
    '''
    Draw main menu.
    Take user input and run relevant function.
    '''
    os.system('clear')

    print(GAME_HEADER)
    cprint('WELCOME TO HANGMAN!')
    cprint('===================')
    print(MENU_ART)
    left_text = '1. Play Hangman'
    middle_text = '2. How To Play'
    right_text = '3. Scoreboard'
    print(f'{left_text : <26}{middle_text : ^26}{right_text : >28}')
    print('-' * 80)
    choice = input('Select an option: ')

    if choice == '1':
        main()
    elif choice == '2':
        instructions()
    elif choice == '3':
        scoreboard()


def main():
    '''
    Main program function.
    '''
    reset_game()
    set_word()
    game_display(GAME_HEADER)
    user_input()


main_menu()
