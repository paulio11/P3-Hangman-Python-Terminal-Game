# Imports
import gspread
from google.oauth2.service_account import Credentials
import random

# Constant Variables
TERMINAL_WIDTH = 80


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
    game_word = random.choice(word_list)
    hidden_word = '_' * len(game_word)