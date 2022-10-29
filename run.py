'''
Hangman python terminal game by Paul Young
'''


# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
import math
import pyfiglet
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

score_sheet = SHEET.worksheet('scoreboard')
score_data = score_sheet.get_all_values()


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


# Print functions
def cprint(a):
    '''
    Take parameter and print it center aligned.
    '''
    terminal_width = 80

    print(a.center(terminal_width))


# Game functions
def reset_game():
    '''
    Resets variables.
    '''
    global player_lives, game_over, game_win, game_stage

    game_stage = 0
    game_win = False
    game_over = False
    player_lives = 9


def game_win_trigger():
    '''
    Function called when the player has won the game.
    From guessing the word, or guessing every letter.
    '''
    global player_lives, game_stage, game_over, end_time, game_win

    end_time = time.time()
    game_win = True
    game_over = True
    game_display(WIN_HEADER)


def set_word():
    '''
    Takes input from user to select a category.
    Picks a random word from Google sheet.
    Makes string of _ based on length of random word.
    '''
    global game_word, hidden_word, category

    os.system('clear')

    print(pyfiglet.figlet_format('Category', justify='center', width=80))
    print('1: Halloween')
    print('2: Pokemon')
    print('3: Countries')
    print('4: Animals')
    print('5: Disney Movies')
    print('\n' * 12)
    print('-' * 80)
    category = input('Select a category: ')

    valid_choices = ['1', '2', '3', '4', '5']
    word_sheet = SHEET.worksheet('word_sheet')

    if category not in valid_choices:
        print(f'{Fore.RED}Invalid selection, try again.')
        time.sleep(1)
        set_word()
    elif category == '1':
        word_list = word_sheet.col_values(1)
        category = 'Halloween Word'
    elif category == '2':
        word_list = word_sheet.col_values(2)
        category = 'Pokemon'
    elif category == '3':
        word_list = word_sheet.col_values(3)
        category = 'Country'
    elif category == '4':
        word_list = word_sheet.col_values(4)
        category = 'Animal'
    elif category == '5':
        word_list = word_sheet.col_values(5)
        category = 'Disney Movie'

    game_word = random.choice(word_list)
    hidden_word = '_' * len(game_word)

    print('Loading game...')


def user_input():
    '''
    While game is running:
    - Displays guessed letters and player health.
    - Takes input from player as guess.
    - Passes valid guess to check_guess function.
    - Calls game_display to redraw game.
    '''
    global game_over, game_win, player_lives, start_time

    guessed_letters = []
    start_time = time.time()

    while game_over is False:

        guessed_letters_str = ' '.join(guessed_letters)
        life_bar = ' ♥' * player_lives

        print(f'Guessed letters: {guessed_letters_str : <45}{life_bar : >18}')
        print('-' * 80)
        guess = input('Guess a letter OR the word: ').upper()

        def redraw():
            time.sleep(1)
            game_display(GAME_HEADER)

        if guess == 'HELP':
            print(game_word)
            redraw()
        elif guess == game_word:
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
    global player_lives, game_stage, game_over, end_time

    if guess in game_word:
        print(f'{Fore.GREEN}Correct guess!')
        update_hidden_word(guess)
    elif guess not in game_word and game_stage != 8:
        print(f'{Fore.RED}Incorrect guess!')
        player_lives -= 1
        game_stage += 1
    else:
        game_win_trigger()

    time.sleep(1)

    if game_over is False:
        game_display(GAME_HEADER)


def update_hidden_word(guess):
    '''
    Takes a correct guess and updates hidden_word.
    If hidden_word complete -> game_over = True.
    '''
    global hidden_word, game_over, game_win, end_time

    positions = [i for i, a in enumerate(game_word) if a == guess]
    hidden_word_arr = list(hidden_word)

    for num in positions:
        hidden_word_arr[num] = guess

    hidden_word = ''.join(hidden_word_arr)

    if '_' not in hidden_word:
        game_win_trigger()


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


def bottom_input():
    '''
    Prints a line of '-' and waits for user input before returning to the menu.
    '''
    print('-' * 80)
    input('Press ENTER to return to the menu...')
    main_menu()


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


def last_five_scores():
    '''
    Slices last 5 scores from sheet.
    Sorts scores in descending order.
    A for loop prints the array values line by line.
    '''

    score_slice = score_data[-1:-6:-1]
    score_slice = sorted(score_slice, key=lambda x: int(x[1]), reverse=True)

    draw_table(score_slice, 'Latest Scores', 'Last 5 Scores:')


def highscores():
    '''
    Slices last 5 scores from sheet.
    Sorts scores in descending order.
    A for loop prints the array values line by line.
    '''

    score_sorted = sorted(score_data, key=lambda x: int(x[1]), reverse=True)

    draw_table(score_sorted[:5], 'High Scores', 'All Time Top 5 Scores:')


def update_scoreboard():
    '''
    Updates scoreboard sheet.
    '''
    global name

    while True:
        name = input('Please enter your name: ').capitalize()[:10]
        if not name.isalpha():
            print(f'{Fore.RED}Invalid name, try again...')
        elif name == '':
            print(f'{Fore.RED}Invalid name, try again...')
        else:
            break

    print('Updating scoreboard...')

    score_sheet = SHEET.worksheet('scoreboard')
    score_sheet.append_row([name, score, seconds, game_word])

    end_screen()


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
    cprint(f'Mystery {category}:')
    print()
    cprint(f'{hidden_word} ({len(game_word)})')
    print(HANGMAN_STAGES[game_stage])

    if game_win:
        calculate_score()
        print('-' * 80)
        update_scoreboard()
    elif game_over and game_win is False:
        left_text = 'Oh dear he died!'
        right_text = f'The Mystery {category} was {game_word}.'
        print(f'{left_text : <40}{right_text : >40}')
        bottom_input()
        

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
    print('\n' * 9)
    bottom_input()


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
        main()
    elif choice == '2':
        instructions()
    elif choice == '3':
        print('Loading scoreboard...')
        highscores()
    elif choice == '4':
        print('Loading scoreboard...')
        last_five_scores()


def main():
    '''
    Main program function.
    '''
    reset_game()
    set_word()
    game_display(GAME_HEADER)
    user_input()


main_menu()
