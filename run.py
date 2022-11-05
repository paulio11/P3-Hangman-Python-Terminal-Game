'''
Hangman - A Python terminal game by Paul Young.
'''


# Imports
import random
import os
import time
import math
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials
from colorama import init, Fore
init(autoreset=True)


# Variables for gspread
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')
SCORE_SHEET = SHEET.worksheet('scoreboard')


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
    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░   ░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
     ░   ░   ▒   ▒▒ ░░  ░        ░ ░  ░     ░ ▒ ▒      ░░   ░ ░  ░  ░▒ ░ ▒
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
               █▄██▄█                  /|\\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                                        ▄▄▄▄▄▄
                                        |    █
                                        O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|\\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█         /     █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''',
    '''
                      _______________   ▄▄▄▄▄▄
                     | OUCH MY NECK! |  |    █
                      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\\  O    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  /|\\   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█         / \\   █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███               █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
]
MENU_ART = '''

                           __________   ▄▄▄▄▄▄
                          | HELP ME! |  |    █
                           ¯¯¯¯¯¯¯¯¯¯\\  °    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  \\O/   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█          |    █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███         / \\   █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''


# Game Variables
PLAYER_LIVES = 9
GAME_STAGE = 0
GAME_WIN = False
GAME_OVER = False
GAME_WORD = None
HIDDEN_WORD = None
CATEGORY = None
START_TIME = None
END_TIME = None
SECONDS = None
SCORE = None
NAME = None


# Print Function
def cprint(text):
    '''
    Take parameter and print it center aligned.
    '''
    terminal_width = 80

    print(text.center(terminal_width))


# Game Menu
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
    l_text = '1. Play Hangman'
    mid_text = '2. How To Play'
    mid_text_2 = '3. High Scores'
    r_text = '4. Last 5 Scores'
    print(f'{l_text : <20}{mid_text : ^20}{mid_text_2 : ^20}{r_text : >20}')
    print('-' * 80)
    choice = input('Select an option: ')
    valid_choices = ['1', '2', '3', '4']

    if choice not in valid_choices:
        print(f'{Fore.RED}Invalid selection, try again.')
        time.sleep(1)
        main_menu()
    elif choice == '1':
        start_game()
    elif choice == '2':
        instructions()
    elif choice == '3':
        print('Loading scoreboard...')
        highscores()
    elif choice == '4':
        print('Loading scoreboard...')
        last_five_scores()


# Game Instructions
def instructions():
    '''
    Print game instructions.
    '''
    os.system('clear')

    print()
    print(pyfiglet.figlet_format('How To Play', justify='center', width=80))
    cprint('The goal of Hangman is to solve the mystery word.\n')
    cprint('_ _ _ _ _ _ _\n')
    cprint('Guess one letter at the time.')
    cprint('If you guess correctly, the letter will appear in the word.\n')
    cprint('H A _ G _ A _\n')
    cprint('If you guess incorrectly, the stage will progress.')
    cprint('After 9 incorrect guesses the game will be over.\n')
    cprint('At any point you can guess the whole word.\n')
    cprint('H A N G M A N')
    print('\n')

    bottom_input()


# Scoreboard
def last_five_scores():
    '''
    Slices last 5 newest scores from sheet.
    Sorts scores in descending order.
    Passes to draw_table function.
    '''

    score_data = SCORE_SHEET.get_all_values()
    # Slices off last 5 rows.
    score_slice = score_data[-1:-6:-1]
    # Sorts data by second column (the score) descending.
    score_slice = sorted(score_slice, key=lambda x: int(x[1]), reverse=True)

    draw_table(score_slice, 'Latest Scores', 'Last 5 Scores:')


def highscores():
    '''
    Sorts scores in descending order.
    Passes top 5 to draw_table function.
    '''

    score_data = SCORE_SHEET.get_all_values()
    # Sorts data by second column (the score) descending.
    score_sorted = sorted(score_data, key=lambda x: int(x[1]), reverse=True)
    # The [:5] is the top five scores.
    draw_table(score_sorted[:5], 'High Scores', 'All Time Top 5 Scores:')


def draw_table(scores, heading, heading2):
    '''
    Draws score table with data from last_five_scores() and highscores().
    '''
    rank = 1
    rank_h = 'RANK'
    name_h = 'NAME'
    score_h = 'SCORE'
    time_h = 'TIME'

    os.system('clear')

    print()
    print(pyfiglet.figlet_format(heading, justify='center', width=80))
    cprint(heading2)
    print()
    headers = f'{rank_h : <6}{name_h : <12}{score_h : <9}{time_h : <5}'
    cprint(headers)
    cprint('=' * 33)

    for line in scores:
        row = f'{rank : <6}{line[0] : <12}{line[1] : <9}{line[2] : <5}'
        cprint(row)
        cprint('-' * 33)
        rank += 1

    print('\n' * 2)

    bottom_input()


# Main Game Functions
def start_game():
    '''
    Main game function.
    '''
    reset_game()
    set_word()
    game_display(GAME_HEADER)
    user_input()


def reset_game():
    '''
    Resets variables.
    '''
    global PLAYER_LIVES, GAME_STAGE, GAME_WIN, GAME_OVER

    PLAYER_LIVES = 9
    GAME_STAGE = 0
    GAME_WIN = False
    GAME_OVER = False


def set_word():
    '''
    Takes input from user to select a category.
    Picks a random word from Google sheet.
    Makes string of underscores based on length of random word.
    '''
    global GAME_WORD, CATEGORY, HIDDEN_WORD

    os.system('clear')

    print(pyfiglet.figlet_format('Category', justify='center', width=80))
    print('1: Halloween')
    print('2: Pokemon')
    print('3: Countries')
    print('4: Animals')
    print('5: Disney Movies')
    print('6: Video Games')
    print('\n' * 11)
    print('-' * 80)
    choice = input('Select a category: ')
    print('Loading game...')

    valid_choices = ['1', '2', '3', '4', '5', '6']
    word_sheet = SHEET.worksheet('word_sheet')

    if choice not in valid_choices:
        print(f'{Fore.RED}Invalid selection, try again.')
        time.sleep(1)
        set_word()
    elif choice == '1':
        word_list = word_sheet.col_values(1)
        CATEGORY = 'Halloween Word'
    elif choice == '2':
        word_list = word_sheet.col_values(2)
        CATEGORY = 'Pokemon'
    elif choice == '3':
        word_list = word_sheet.col_values(3)
        CATEGORY = 'Country'
    elif choice == '4':
        word_list = word_sheet.col_values(4)
        CATEGORY = 'Animal'
    elif choice == '5':
        word_list = word_sheet.col_values(5)
        CATEGORY = 'Disney Movie'
    elif choice == '6':
        word_list = word_sheet.col_values(6)
        CATEGORY = 'Video Game'

    GAME_WORD = random.choice(word_list)
    HIDDEN_WORD = '_' * len(GAME_WORD)


def game_display(header):
    '''
    Prints the following:
    - Header based on current state.
    - Hangman word.
    - Current game stage.
    At the end of a game, shows text based on win or fail.
    '''

    os.system('clear')

    print(header)
    cprint(f'Mystery {CATEGORY}:')
    print()
    cprint(f'{HIDDEN_WORD} ({len(GAME_WORD)})')
    print(HANGMAN_STAGES[GAME_STAGE])

    if GAME_WIN:
        calculate_score()
        print('-' * 80)
        update_scoreboard()
    elif GAME_OVER and GAME_WIN is False:
        left_text = 'Oh dear he died!'
        right_text = f'The Mystery {CATEGORY} was {GAME_WORD}.'
        print(f'{left_text : <40}{right_text : >40}')
        bottom_input()


def user_input():
    '''
    While game is running:
    - Displays guessed letters and player health.
    - Takes input from player as guess.
    - Passes valid guess to check_guess function.
    - Passes correct word guess to game_win_trigger function.
    - Calls game_display to redraw game.
    '''
    global START_TIME, HIDDEN_WORD

    guessed_letters = []
    START_TIME = time.time()

    while GAME_OVER is False:

        guessed_letters_str = ' '.join(guessed_letters)
        life_bar = ' ♥' * PLAYER_LIVES

        print(f'Guessed letters: {guessed_letters_str : <45}{life_bar : >18}')
        print('-' * 80)
        guess = input('Guess a letter OR the word: ').upper()

        def redraw():
            '''
            Redraws game area after a guess.
            '''
            time.sleep(1)
            game_display(GAME_HEADER)

        if guess == 'HELP':
            print(GAME_WORD)
            redraw()
        elif guess == GAME_WORD:
            HIDDEN_WORD = GAME_WORD
            game_win_trigger()
        elif not guess.isalpha() or len(guess) > 1:
            print(f'{Fore.RED}Invalid guess')
            redraw()
        elif guess in guessed_letters:
            print(f'{Fore.YELLOW}Letter already guessed, try another')
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
    global PLAYER_LIVES, GAME_STAGE, GAME_OVER, END_TIME

    if guess in GAME_WORD:
        print(f'{Fore.GREEN}Correct guess!')
        update_hidden_word(guess)
    elif guess not in GAME_WORD and GAME_STAGE != 8:
        print(f'{Fore.RED}Incorrect guess!')
        PLAYER_LIVES -= 1
        GAME_STAGE += 1
    else:
        # Game fail trigger.
        END_TIME = time.time()
        PLAYER_LIVES -= 1
        GAME_STAGE += 1
        GAME_OVER = True
        game_display(FAIL_HEADER)

    time.sleep(1)

    if GAME_OVER is False:
        # Redraws game area after checking guess.
        game_display(GAME_HEADER)


def update_hidden_word(guess):
    '''
    Takes a correct guess and updates hidden_word.
    If hidden_word complete -> game_over = True.
    '''
    global HIDDEN_WORD

    # Gets all postions of guess in word as an array.
    positions = [i for i, a in enumerate(GAME_WORD) if a == guess]
    # Turn the hidden word into an array.
    hidden_word_arr = list(HIDDEN_WORD)
    # Change value of position in array to guess.
    for num in positions:
        hidden_word_arr[num] = guess
    # Turns the hidden word array back into a string.
    HIDDEN_WORD = ''.join(hidden_word_arr)
    # If hidden word is complete, the game is won.
    if '_' not in HIDDEN_WORD:
        game_win_trigger()


def game_win_trigger():
    '''
    Function called when the player has won the game.
    From guessing the word, or guessing every letter.
    '''
    global END_TIME, GAME_WIN, GAME_OVER

    END_TIME = time.time()
    GAME_WIN = True
    GAME_OVER = True
    game_display(WIN_HEADER)


def calculate_score():
    '''
    Calculates and prints player score - based on lives, word length, and time.
    '''
    global SECONDS, SCORE

    SECONDS = math.floor(END_TIME - START_TIME)
    SCORE = math.ceil((len(GAME_WORD) * 500) + (PLAYER_LIVES * 1000) / SECONDS)
    left_text = 'Congratulations!'
    mid_text = f'SCORE: {SCORE}'
    right_text = f'TIME: {SECONDS}s'

    print(f'{left_text : <30}{mid_text : ^20}{right_text : >30}')


def update_scoreboard():
    '''
    Updates scoreboard sheet.
    '''
    global NAME

    while True:
        NAME = input('Please enter your name: ').capitalize()[:10]
        if not NAME.isalpha():
            print(f'{Fore.RED}Invalid name, try again...')
        else:
            break

    print('Updating scoreboard...')

    # Updates google sheet with new row.
    SCORE_SHEET.append_row([NAME, SCORE, SECONDS, GAME_WORD])

    end_screen()


def end_screen():
    '''
    Confirms name entry into scoreboard.
    Thanks player and returns to menu after input.
    '''
    os.system('clear')

    print('\n' * 12)
    cprint(f'Thank you for playing {NAME}!')
    cprint('Your name and score have been uploaded.')
    print('\n' * 9)

    bottom_input()


def bottom_input():
    '''
    Prints a line of '-' and waits for user input before returning to the menu.
    '''
    print('-' * 80)
    input('Press ENTER to return to the menu...')
    main_menu()


main_menu()
