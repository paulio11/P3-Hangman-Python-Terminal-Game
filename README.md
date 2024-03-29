# Hangman - Python Terminal Game

![Image of website](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/readme-title.png)

[Link to live site](https://py-hangman-py.herokuapp.com/)

## Contents 

1. [Introduction](#introduction)
2. [The User Experience](#the-user-experience)
    1. [User Goals](#user-goals)
    2. [Project Goals](#project-goals)
3. [Design and Flow](#design-and-flow)
    1. [Flow Chart](#flow-chart)
    2. [Flow Chart with Function Names and Variables](#flow-chart-with-function-names-and-variables)
    3. [Titles and Headings](#titles-and-headings)
    4. [Mock Terminal and Background](#mock-terminal-and-background)
4. [Google Sheet](#google-sheet)
5. [Features](#features)
    1. [Main Menu](#main-menu)
    2. [How To Play](#how-to-play)
    3. [High Scores and Last Five Scores](#high-scores-and-last-five-scores)
6. [The Game](#the-game)
    1. [Category Selection and The Game Word](#category-selection-and-the-game-word)
    2. [The Main Game Screen](#the-main-game-screen)
    3. [Updating the Hidden Word](#updating-the-hidden-word)
    4. [Game Over Screen](#game-over-screen)
    5. [Winning the Game](#winning-the-game)
    6. [Calculating the Score](#calcuating-the-score)
    7. [Updating the Scoreboard](#updating-the-scoreboard)
    8. [End of the Game](#end-of-the-game)
7. [Common Features](#common-features)
    1. [User Input and Feedback](#user-input-and-feedback)
    2. [Printing Center Aligned Text](#printing-center-aligned-text)
    3. [Loading Text](#loading-text)
    4. [Clearing the Terminal](#clearing-the-terminal)
8. [Unimplemented Features](#unimplemented-features)
    1. [Difficulty](#difficulty)
    2. [Guessing Whole Words Incorrectly](#guessing-whole-words-incorrectly)
    3. [More User Data](#more-user-data)
    4. [Further Word and Category Expansion](#further-word-and-category-expansion)
9. [Bugs and Development Issues](#bugs-and-development-issues)
10. [Technologies](#technologies)
    1. [Main Languages Used](#main-languages-used)
    2. [Other](#other)
    3. [Python Libraries](#python-libraries)
11. [Testing](#testing)
    1. [Testing User Goals](#testing-user-goals)
    2. [Manual Testing](#manual-testing)
    3. [Automated Testing](#automated-testing)
    4. [User Testing](#user-testing)
12. [Deployment](#deployment)
13. [Credits and Acknowledgements](#credits-and-acknowledgements)
    1. [Text](#text)
    2. [Images](#images)
    3. [Code](#code)
    4. [Acknowledgements](#acknowledgements)


## Introduction
Hangman is a Python terminal game. It runs on a mock terminal deployed to Heroku.

Hangman is the third milestone project required to complete my Diploma in Full Stack Software Development at The Code Institute. This project required me to showcase my newly learned Python skills to create a command-line application.

The goal of the game is to guess the mystery word one letter at a time. The time taken, the number of incorrect guesses and word length will determine their score and their position on the scoreboard.

[Back to top 🔺](#hangman---python-terminal-game)

## The User Experience

### User Goals
As a user I want:
- To have fun and be challenged.
- To learn how to play and understand the game.
- The game to offer replay value with a large number of words and categories to play with.
- To easily navigate through available options and have clear feedback on my inputs.
- To know how well I did and be able to compare myself to others.

### Project Goals
As the designer I want:
- Users to meet their goals (above).
- The game to be functional and without errors.

[Back to top 🔺](#hangman---python-terminal-game)

## Design and Flow

### Flow Chart
[Lucid Chart](https://www.lucidchart.com/) was used to plan the flow of the program, from functions to user input and variable checks.

![Flow chart](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/flowchart-updated.png)

### Flow Chart with Function Names and Variables

![Flow chart with Functions and Variables](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/flowchart-functions.png)

### Titles and Headings
- The titles for the scoreboard and category selection screens were made using [pyfiglet](https://pypi.org/project/pyfiglet/0.7/).
- The game over and hangman titles were made using [Text ASCII Art Generator](https://patorjk.com/software/taag/).

### Mock Terminal and Background
- The mock python terminal is from a template provided by Code Institute. You can find the original [here](https://github.com/Code-Institute-Org/python-essentials-template).
- The page background is taken from [Vecteezy](https://www.vecteezy.com/vector-art/1873000-old-vintage-computer-vector-illustration), edited to fit the aspect ratio of the terminal.

[Back to top 🔺](#hangman---python-terminal-game)

## Google Sheet
You can view the Google sheet that stores all data for this program [here](https://docs.google.com/spreadsheets/d/1FH9ukZ5724J87N3EWKTdVtXvJVdfYsBsIQK61SwxEy4/edit?usp=sharing). The sheet **word_sheet** contains all possible game words, sorted by category (each column). The second sheet **scoreboard** is self-explanatory, this is where all user scores are stored.

## Features

### Main Menu
![Main menu](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-mainmenu.png)

The first screen presented to the user is the main menu. It shows the game title, some ASCII art and a row of options. Below the dotted line is a python input field waiting to accept the user's choice.

Created by the `main_menu()` function. User input is verified by an if-else statement and an array of valid user inputs.

```
valid_choices = ['1', '2', '3', '4']
```

### How To Play
![How to play](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-howtoplay.png)

A simple text-only screen. Contains instructions for the user on how to play and win the game. 

Beneath is a dotted line and the text "Press ENTER to return to the main menu...". Input from the user here will run the `main_menu()` function and return them to the main menu. This is repeated throughout the program so to avoid repeated lines of code it is all part of a function called `bottom_input()` that is called when necessary.

```
def bottom_input():
    print('-' * 80)
    input('Press ENTER to return to the menu...')
    main_menu()
```

### High Scores and Last Five Scores
Using the `get_all_values()` function from the [gspread](https://docs.gspread.org/en/latest/) google sheets library, data is pulled from a spreadsheet containing all player scores. The data is sliced and sorted in different ways depending on the option selected by the user from the main menu. 

Last Five Scores `last_five_scores()` slices the bottom 5 rows from the spreadsheet and then sorts the arrays using a lambda function by the values in the second (score) column. This data is then passed to the `draw_table()` function.

```
def last_five_scores():
    score_data = SCORE_SHEET.get_all_values()
    score_slice = score_data[-1:-6:-1]
    score_slice = sorted(score_slice, key=lambda x: int(x[1]), reverse=True)
    draw_table(score_slice, 'Latest Scores', 'Last 5 Scores:')
```

![Last five scores](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-lastfive.png)

High Scores `highscores()` sorts all data pulled from the spreadsheet again with a lambda function by the values in the score column. Then passes just the first 5 arrays to the `draw_table()` function.

```
def highscores():
    score_data = SCORE_SHEET.get_all_values()
    score_sorted = sorted(score_data, key=lambda x: int(x[1]), reverse=True)
    draw_table(score_sorted[:5], 'High Scores', 'All Time Top 5 Scores:')
```

![High scores](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-highscores.png)

`draw_table()` takes the data and uses a for loop to print the arrays one at a time as a presentable table of scores.

```
def draw_table(scores, heading, heading2):
    rank = 1
    rank_h = 'RANK'
    name_h = 'NAME'
    score_h = 'SCORE'
    time_h = 'TIME'
    headers = f'{rank_h : <6}{name_h : <12}{score_h : <9}{time_h : <5}'
    print(headers)
    print('=' * 33)
    for line in scores:
        row = f'{rank : <6}{line[0] : <12}{line[1] : <9}{line[2] : <5}'
        cprint(row)
        cprint('-' * 33)
        rank += 1
```

[Back to top 🔺](#hangman---python-terminal-game)

## The Game

### Category Selection and The Game Word
![Category selection](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-category.png)

The game itself features several categories the user can select from. The selected category changes the variable `WORD_LIST`. Each column in the word_list spreadsheet contains the possible words for each category.

A random word is pulled using python [random](https://docs.python.org/3/library/random.html) and assigned as the variable `game_word`. This will be the word the user has to guess as the object of the game. 

```
game_word = random.choice(word_list)
```

During gameplay, this mystery word is represented by a line of underscores. This is the `hidden_word` variable, initially created by assigning it the value of one underscore multiplied by the length of the game word.

```
hidden_word = '_' * len(game_word)
```

### The Main Game Screen
![Main game screen](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-game.png)

The most prominent feature of the game screen is the ASCII art landscape showing a castle, the hangman platform, and a tree. This multiple line string the first index of an array called `HANGMAN_STAGES`. Throughout the game, if the user makes an incorrect guess the `game_stage` variable is iterated by 1, and then when the game screen is reprinted the next ASCII art landscape in the array is called.

```
print(HANGMAN_STAGES[game_stage])
```

Beneath the game stage is a line containing two pieces of important information for the user. First, is a list of letters already guessed. This information is useful to the player when making further guesses. 

```
guessed_letters = []
guessed_letters.append(guess)
guessed_letters_str = ' '.join(guessed_letters)
```

Second, is a string of hearts `♥` representing the number of incorrect guesses left before a game over. Upon an incorrect guess, the variable `player_lives` is iterated by -1.

```
life_bar = ' ♥' * player_lives
```

As with all screens so far, the user input is on the same line of the terminal, below a line of dashes. This is where the user will make their guess, either one letter at a time, or as a whole word.

The user input once validated by `user_input()` is passed to the `check_guess()` function. There are three outcomes of this function:
- The guess is correct and the function `update_hidden_word()` is called.
- The guess is incorrect and the user is out of guesses so the game is over.
- The guess is incorrect, the user has guesses remaining and the game stage is redrawn so the game can continue.

### Updating the Hidden Word
![Updating the word](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-updateword.png)

The `update_hidden_word()` function is fairly complex but it can be broken up into a few simple actions. 

1. It will take the user's guess and look for that letter in the `game_word` variable, returning an array of numbers, each representing the position of the guess in the word. 

```
positions = [i for i, a in enumerate(game_word) if a == guess]
```

2. Then it creates a new variable from `hidden_word` using the `list` function to return an array. 

```
hidden_word_arr = list(hidden_word)
```

3. A for loop then assigns the value of the user's guess to the correct positions in the array.

```
for num in positions:
    hidden_word_arr[num] = guess
```

4. `hidden_word` is then reassigned a value using the `join` function.

```
hidden_word = ''.join(hidden_word_arr)
```

At this point, it is possible the user has guessed correctly all the letters in the game word. If so the `game_win_trigger()` function can be called. An easy way to check for this is whether or not any underscores remain in the hidden word.

```
if '_' not in hidden_word:
    game_win_trigger()
```

### Game Over Screen

![Game over](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-gameover.png)

When the variable `game_stage` has a value of 9, the game is over. This will occur after that many incorrect guesses from the user. This check is at the bottom of an if statement in the `check_guess()` function.

```
Else:
    end_time = time.time()
    player_lives -= 1
    game_stage += 1
    game_over = True
    game_display(FAIL_HEADER)
```

When `game_over` is `True` and the game display is reprinted it will show the game over title instead, as well as the reveal of the game word to the player. `game_over` being `True` also stops the `While` loop within the `user_input()` function, and therefore will no longer ask the user to input a guess. 

```
while game_over is False:
```

```
elif game_over and game_win is False:
    left_text = 'Oh dear he died!'
    right_text = f'The Mystery {category} was {game_word}.'
    print(f'{left_text : <25}{right_text : >55}')
```

The function `bottom_input` is then called once again to return the user to the main menu.

### Winning the Game
There are two ways to trigger a game win state:
- If the user guesses the game word in its entirety.
- If there are no underscores left in the `hidden_word` variable.

Both of these outcomes will call the `game_win_trigger()` function.

```
elif guess == game_word:
    hidden_word = game_word
    game_win_trigger()
```
```
if '_' not in hidden_word:
    game_win_trigger()
```

The `game_win_trigger()` function will assign the variables `game_win` and `game_over` to `True`, set a variable called `end_time` (used to calculate the score later on) and call the `game_display()` function.

```
def game_win_trigger():
    end_time = time.time()
    game_win = True
    game_over = True
    game_display(WIN_HEADER)
```

When the game screen is reprinted with the variable `game_win` as `True` two functions are called, first `calculate_score()` and then `update_scoreboard()`.

### Calcuating the Score
The `calculate_score()` function has three parts. First, the variable `seconds` is assigned the value of `end_time` subtracted from `start_time` to get the seconds taken to win the game. Python [math](https://docs.python.org/3/library/math.html) is used to round down the value to a whole number.

```
seconds = math.floor(end_time - start_time)
```

Then the score is calculated using an algorithm that takes into account the length of the word, the number of player lives remaining and the time taken. This is then rounded up using the `math.ceil()` function.

```
score = math.ceil((len(game_word) * 500) + (player_lives * 1000) / seconds)
```

The values assigned have very little thought and design put into them, but basically; this makes longer words solved with a low number of incorrect guesses in a short time score higher than short words solved with many incorrect guesses in a longer amount of time. As the game time progresses the effect of the time taken has a diminishing effect on the final score.

### Updating the Scoreboard
![Game win screen](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-gamewin.png)

The user is presented with an input asking for their name upon winning the game. The input is validated with a `while` loop that checks the input with the `isalpha()` function. Invalid inputs will restart the loop asking the user once again for input. Any input is also reduced to just 10 characters. This is to help maintain the desired spacing of columns on the scoreboard.

``` 
while True:
    name = input('Please enter your name: ').capitalize()[:10]
    if not name.isalpha():
        print(f'{Fore.RED}Invalid name, try again...')
    else:
        break
```

The user's name, their score, time taken, and (for my own curiosity) the game word, are passed as parameters into the `append_row()` function from gspread.

```
SCORE_SHEET.append_row([name, score, seconds, game_word])
```

### End of the Game
![Game end screen](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-gameend.png)

Just for user feedback purposes, once the scoreboard has been updated the user is presented with a simple screen thanking them for playing, this includes the name they provided previously and the option to return to the main menu.

```
def end_screen():
    print(f'Thank you for playing {name}!')
    print('Your name and score have been uploaded.')
```

[Back to top 🔺](#hangman---python-terminal-game)

## Common Features
### User Input and Feedback
- This user input design and positioning are constant throughout the program. Always below a dotted line and on the same line in the terminal.
- Positive feedback is represented with green text. Negative feedback or invalid input is represented with red text. This functionality is part of [colorama](https://pypi.org/project/colorama/). 
- Consistency of position and colour improves the experience for the user, hopefully producing a positive emotional response.

![Coloured feedback](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/screenshot-feedback.png)

### Printing Center Aligned Text
I created a function called `cprint()` to center align text. This was to help with line length issues. 

```
def cprint(text):
    terminal_width = 80
    print(text.center(terminal_width))
```

### "Loading" Text
I have loading text where necessary to give the user feedback when the following takes place:
- Loading either scoreboard
- Updating the scoreboard
- Retrieving the word list after category selection

All three of these require information to be pushed to or pulled from the spreadsheet and can take a few seconds. The loading text reassures the user something is happening.

### Clearing the Terminal
A function called `clear_terminal()` is called throughout to clear the screen before printing what is required at that point in the program. This was essential to make sure all user input is on the same line - a key part of my design. This was a suggestion from [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python).

```
def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')
```

[Back to top 🔺](#hangman---python-terminal-game)

## Unimplemented Features

### Guessing Whole Words Incorrectly
Currently, the game will not penalise the user if they guess incorrectly when inputting an incorrect whole word. This will just show as an invalid guess. I would like the game to be able to distinguish between an invalid guess and an incorrect whole word guess. This would require a more complex if-else statement that I did not have the time to implement.

### Difficulty
An option to select difficulty would be a good addition. The random selection of the game word means that sometimes the length is short, sometimes the length is long. Longer words are inherently harder and more fun to guess. A selectable difficulty would allow the user to choose a minimum length of word that they have to guess.

### More User Data
This would provide no extra functionality but there are many more values and details I can upload to the spreadsheet upon scoreboard entry. Things like the order of letters guessed, the time between guesses, whole words guessed and so on. All would benefit me as the designer from a gameplay perspective. This feedback could lead to improvements in word choice or difficulty. To implement this, new variables would have to be created throughout the program, and then each appended to the spreadsheet in the same way as the user's name and score currently are.

### Further Word and Category Expansion
And of course more obvious things such as a larger word list and category choice. This is simple to implement but would add no extra value to this program as a portfolio project. 

[Back to top 🔺](#hangman---python-terminal-game)

## Bugs and Development Issues
- The most common issue a user will come across is after a guessed letter. There is a second delay in place so the user can see feedback in the form of "Correct guess", "Incorrect guess" etc. During this second, any input such as another letter guess will be invisible and then cause the next input to be invalid.  To provide some context to the user the invalid guess error message was changed to **"Invalid guess, OR you guessed too fast"**. Ideally, a solution to this would have been good. A way to clear any unwanted inputs before asking the user for their next guess would be necessary to achieve this.
- For a while early in development if a letter appeared in the game word more than once, only the first instance would reveal itself to the user after a correct guess. This was due to the if statement only applying to the first instance of the guessed letter it came across. This meant I could not use words with repeated letters. I later fixed this by using the `enumerate` object to return every position as an array, then a for loop to loop through the word to fill it in correctly. This is part of the `update_hidden_word()` function.

[Back to top 🔺](#hangman---python-terminal-game)

## Technologies

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
    - You can see all my python code [here](https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py).

### Other
- [GitHub](https://github.com/)
    - Used to store files, changes, and host page assets.
- [GitPod](https://www.gitpod.io/)
    - Used to write, comment code, and commit to GitHub.
- [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - Used as the basis of the project, helped to set up GitPod workspace.
- [Affinity Photo](https://affinity.serif.com/en-gb/photo/)
    - Used to edit images, resizing and optimizing them for use on a website.
- [Am I Responsive](https://ui.dev/amiresponsive)
    - Used to create the hero image at the top of this readme.
- [Google Sheets](https://www.google.co.uk/sheets/about/)
    - Used to store the database of words and categories, as well as user scores.
- [Heroku](https://www.heroku.com/)
    - Used to deploy the project.
- [Lucid Chart](https://www.lucidchart.com/)
    - Used to create flowcharts.

### Python Libraries
- [random](https://docs.python.org/3/library/random.html)
    - Used to randomly select the word for the game.
- [os](https://docs.python.org/3/library/os.html)
    - Used for its `clear` tool, to clear the terminal window.
- [time](https://docs.python.org/3/library/time.html)
    - Used to calculate the time taken to complete the game.
- [math](https://docs.python.org/3/library/math.html)
    - Used to round down and round up variables.
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
    - Used to create ASCII art titles for the scoreboard, how to play screen, etc.
- [gspread](https://docs.gspread.org/en/latest/)
    - Used to pull from and push to a Google Sheet.
- [oauth2](https://pypi.org/project/python-oauth2/)
    - Used for authentication.
- [colorama](https://pypi.org/project/colorama/)
    - Used to colour feedback messages for the user.
- [pycodestyle](https://pypi.org/project/pycodestyle/)
    - An alternative to PEP8Online, a PEP8 validator.

[Back to top 🔺](#hangman---python-terminal-game)

## Testing

### Testing User Goals

**User's want:**
- To have fun and be challenged.
    - Obiously you can't test to see if a user is having fun, but users that have played the game have given me positive feedback.
    - The game sometimes can be challenging, likely when the user is unfamiliar with the game word or due to it's length. Selectable difficulty levels are currently unimplemented. See [Unimplemented Features](#unimplemented-features) above.
- To learn how to play and understand the game.
    - The How To Play screen avaiable to the user from the main menu helps them understand.
    - Feedback to the user throughout the game further aids this.
- The game to offer replay value with a large number of words and categories to play with.
    - Currently the game offers the user 6 categories to choose from, each with 30+ words to guess. This isn't a huge ammount but is easily expandable.
- To easily navigate through available options and have clear feedback on my inputs.
    - The main menu is clear and simple to use.
    - Throughout the game and other screens, user input is always requested on the same line in the terminal. Making it clear and consistent.
- To know how well I did and be able to compare myself to others.
    - Users that get a game over are show the game word at the end so they can see how close they got to winning.
    - Winners are presented with a score and a time taken statistic. They can then compare themselves with others by viewing the scoreboard.

### Manual Testing

<details>
    <summary>Making invalid inputs on the main menu</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/01-main-menu-invalid.gif">
</details>
<details>
    <summary>Navigating to the How To Play screen and returning to the main menu</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/02-howtoplay.gif">
</details>
<details>
    <summary>Navigating to the High Scores screen and returning to the main menu</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/03-highscores.gif">
</details>
<details>
    <summary>Navigating to the Last 5 Scores screen and returning to the main menu</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/04-last5scores.gif">
</details>
<details>
    <summary>Starting the game</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/05-startgame.gif">
</details>
<details>
    <summary>Selecting the Halloween category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/06-cat-halloween.gif">
</details>
<details>
    <summary>Selecting the Pokémon category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/07-cat-pokemon.gif">
</details>
<details>
    <summary>Selecting the Countries category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/08-cat-country.gif">
</details>
<details>
    <summary>Selecting the Animals category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/09-cat-animals.gif">
</details>
<details>
    <summary>Selecting the Disney Movies category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/10-cat-disney.gif">
</details>
<details>
    <summary>Selecting the Video Games category</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/11-cat-videogames.gif">
</details>
<details>
    <summary>Making incorrect guesses</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/12-incorrectguess.gif">
</details>
<details>
    <summary>Making correct guesses</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/13-correctguess.gif">
</details>
<details>
    <summary>Making repeat guesses</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/14-repeatedguess.gif">
</details>
<details>
    <summary>Failing the game (running out of lives/guesses)</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/15-failing.gif">
</details>
<details>
    <summary>Returning to the main menu after failing the game</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/16-failingbacktomenu.gif">
</details>
<details>
    <summary>Winning the game (completing the word)</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/17-finishingword.gif">
</details>
<details>
    <summary>Winning the game (guessing the word)</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/18-guessingword.gif">
</details>
<details>
    <summary>Entering name</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/19-nameentry.gif">
</details>
<details>
    <summary>Entering an invalid name</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/22-invalidname.gif">
</details>
<details>
    <summary>Entering a long name</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/23-longname.gif">
</details>
<details>
    <summary>Entering no name</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/24-noname.gif">
</details>
<details>
    <summary>Returning to the main menu after name entry</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/20-returningtomenu.gif">
</details>
<details>
    <summary>Checking score in scoreboard after winning the game</summary>
    <img src="https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/21-checkingscore.gif">
</details>

### Automated Testing
For automated testing, an alternative to PEP8Online had to be used as there are ongoing issues with this python validator. [Pycodestyle](https://pypi.org/project/pycodestyle/) (a PEP8 validator) was added directly to my workspace in Gitpod. Once enabled pycodestyle highlights any warnings and errors within your code. My code is contains no errors or warnings at point of project submission.

### User Testing

Throughout all stages of this project, the application was tested by several Code Institute students as well as other friends. Weekly testing was carried out my by mentor [Oluwaseun Owonikoko](https://github.com/seunkoko).

[Back to top 🔺](#hangman---python-terminal-game)

## Deployment

This program was deployed to [Heroku](https://heroku.com/). You can visit the live site [here](https://py-hangman-py.herokuapp.com/).

**To deploy a copy of this project for your self follow these steps:**
1. Fork or clone this repository.
2. Create a new app on Heroku.
3. Ensure that the buildpacks are set to `Python` and `NodeJS`.
4. Link the app on Heroku to the repository.

**Setting up credentials and Google Sheets:**
1. Make a copy (File > Make a copy) of the Google sheet for this game [here](https://docs.google.com/spreadsheets/d/1FH9ukZ5724J87N3EWKTdVtXvJVdfYsBsIQK61SwxEy4/edit#gid=0).
2. Create a new project on [Google Could Platform](https://console.cloud.google.com/projectcreate).
3. Enable the [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com).
4. Create your credentials for accessing **Application Data** [here](https://console.cloud.google.com/apis/credentials/wizard?api=drive.googleapis.com).
5. Grant permissions of of **Basic > Editor**.
6. Create new service account keys (type: JSON).
7. Copy the email address under **Service Accounts** and add this as an **Editor** to your copy of my Google sheet.
8. Enable the [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com).

**Config Vars:**
1. Download your key file then navigate back to your [Heroku Dashboard](https://dashboard.heroku.com/apps) and select your app.
2. Under Settings, look for **Config Vars** and add the following:

![Image of config vars](https://raw.githubusercontent.com/paulio11/P3-Hangman-Python-Terminal-Game/main/documentation/configvars.png)

**Deployment:**
1. Once the Config Vars are set, click Deploy.
2. Scroll to the bottom of the deploy options and click the **Deploy Branch** button. Optionally you can also **Enable Automatic Deploys**.
3. The site will now be live.


[Back to top 🔺](#hangman---python-terminal-game)

## Credits and Acknowledgements

### Text
This project contains a list of Disney movies, and Pokémon names, all belong to their respective owners Disney and The Pokémon Company.

### Images
A single image is used in this project. See [above](#images).

### Code
- Information provided in [this thread](https://stackoverflow.com/questions/30076145/how-to-sort-list-of-lists-by-highest-number) on Stack Overflow was used to sort data pulled from my scoreboard spreadsheet.
- Information provided in [this thread](https://stackoverflow.com/questions/44307988/find-all-occurrences-of-a-character-in-a-string) on Stack Overflow was used to find all the occurrences of the guessed letter in the game word.
- Information provided in [this thread](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) on Stack Overflow was used to better understand how to clear the terminal window.

### Acknowledgements
Thanks to my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) and the students from class June 2022 for their help and suggestions throughout the project.

[Back to top 🔺](#hangman---python-terminal-game)