# Hangman - Python Terminal Game

![Image of website on multiple devices](#)

[Link to live GitHub deployment](#)

## Contents 



## Introduction
Hangman is a Python terminal game. It runs on a mock terminal on Heroku.

Hangman is my third milestone project required to complete my Diploma in Full Stack Software Development at The Code Institute. This project required me to showcase my newly learned Python skills to create a command-line application.

The goal of the game is to guess the mystery word one letter at a time. The time taken, the number of incorrect guesses and word length will determine their score and their position on the scoreboard.

[Back to top 🔺](#)

## The User Experience

### User Goals
As a user I want:
- To have fun and be challenged.
- To learn how to play and understand the game.
- The game to offer replay value with a large number of words and categories to play with.
- To easily navigate through available options and have clear feedback on my inputs.
- To know how weel I did and be able to compare myself to others.


### Project Goals
As the designer I want:
- Users to meet their goals (above).
- The game to be functional and without errors.


[Back to top 🔺](#)

## Design and Flow

### Flow Chart
[Lucid Chart](https://www.lucidchart.com/) was used to plan out the flow of the program, from functions to user input/variable checks.

### Strategy
The strategy will include all the user needs and my objectives. The website will target the following audience:

**Roles:**
- New employees.
- Current employees.

**Personality:**
- Employees seeking further information.
- Curious forward-thinking employees.
- Employees who track and value pay.

The website needs to enable users to:
- Find out about payday.
- Learn more about their payslip.
- Understand what the different deductions and payments mean.
- Test their knowledge.
- Help calculate their pay.

Taking the above into account, I created this chart to show what is essential and what is actually viable.

| Feature | Importance | Viability | Notes |
| ----------- | ----------- | ----------- | ----------- |
| Payday Calculator | 5 | 5 | Ranked high in importance as this would be the necessary interactive element of the website. |
| Deductions and paymenents explaination | 4 | 5 | Easy to add information - plain text. |
| Payslip information | 3 | 5 | Easy to add information - plain text. |
| User Quiz | 2 | 2 | Futher interactivity - more challenging to implement. |
| Payday Countdown | 1 | 3 | Extended javascript fuctionality.

### Site Map
With the information above, I came up with the website hierarchical structure. The site map below shows how employees would navigate around the website.

![Site map](https://paulio11.github.io/project-2/documentation/site-map.png)

### Wireframes
[Balsamiq for Desktop](https://balsamiq.com/wireframes/) was used ahead of development to plan the basic skeleton of all pages. You can download my wireframes file [here](https://paulio11.github.io/project-2/documentation/wireframe.bmpr).

![Website wireframes](https://paulio11.github.io/project-2/documentation/wireframe.jpg)

[Back to top 🔺](#co-op-your-pay)

## Design

### Color Scheme
The site uses a restrained and on-brand colour scheme. The design is professional and fits with existing Co-op employee websites. The idea is that one day it could be a part of it. I am demonstrating my ability to create a potential and seamless addition to what is currently available to employees. The few colours chosen are featured throughout the entire site, from the home page to each page after that - providing a cohesive experience for the user.

#### Color Palette
![Color Palette](https://paulio11.github.io/project-2/documentation/color-palette.png)

### Typography
Fonts are imported from [Google Fonts](https://fonts.google.com/). The font used for all elements is [Roboto](https://fonts.google.com/specimen/Roboto). Roboto is a clear, versatile font. Simply increasing the font-weight creates enough contrast between titles and body text.

### Images
A single image is used - the Co-op logo, shown on the home page and in the header of every other page.

### Lightweight Design
The whole site is minimal and lightweight. A single font import keeps the required resources low. A single image ensures the combined filesizes remain small. Together they will enable more users and devices to use the website, even on a mobile connection.

[Back to top 🔺](#co-op-your-pay)

## Features
The Calculator, Understand, Problems, Quiz, and about pages have a consistent style. They are built from the ground up to be simple and responsive. Viewable on all screen sizes with a `min-width` of 300px.

These pages contain the following common features:

**Header**
- An area at the top of each page containing the logo, a username and a button to open the navigation menu.
- The icons for the user and menu are from [Font Awesome](https://fontawesome.com/).
- Within the header, if the user clicks on "Hello Employee" a JavaScript prompt appears asking for the user's name. This will save the input in local storage and display on each future page visit. Just a little easter egg - local storage fun!

**Sidebar**
- Clicking the menu button in the header will open the navigation menu. Sliding in from the right of the screen using css translation. The button for the menu and the menu’s close button are controlled by javascript.
- Links to all pages on the website. Communicated to the user by a `:hover` effect that changes the `background-colour` and the cursor to pointer.
- The JavaScript used to make this work can be found in [sidebar.js](https://github.com/paulio11/project-2/blob/main/assets/js/sidebar.js).

![Sidebar Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-sidebar.png)

**The Page Title**
- A `<h1>` element.

**Style**
- All fonts, margins, padding and colours match throughout all pages.

**Footer**
- A footer at the bottom of each page containing the site title and author.
- Placed at the bottom of the viewport using `display: flex;`, `flex-direction: column;`, and `flex-grow: 1;` on a container `<div>` that holds the page content above the `<footer>`.

Neither the `<header>` nor `<footer>` are fixed to the top/bottom of the screen, as I believed it would have taken up too much screen space - especially on a smaller device. To remedy the navigation issues caused on the taller home page, I added a simple javascript scroll back to the top button. The javascript code for this is in the sidebar.js file, as it is loaded on every page.

**Scrolling**
- On longer pages (calculator.html, understand.html and problems.html) the css rule `scroll-behavior: smooth;` allows the user to better understand where they are navigating to when using links within the page.
- A *back to top* button appears when scrolling below the header to further assist navigation. The JavaScript code that makes this work can be seen in the file [top.js](https://github.com/paulio11/project-2/blob/main/assets/js/top.js).

![Back to Top Button Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-topbutton.png)

**[Home Page](https://paulio11.github.io/project-2)**

A simple landing page is all that is needed for a visiting user: the Co-op logo, website title, and a small sentence describing the purpose of the website. Below is the main navigation menu, a copy of what is in the sidebar on other pages.

![Home Page Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-index.png)

**[Payday Calculator](https://paulio11.github.io/project-2/calculator.html)**

The main interactive part of the whole website. This page consists of:
- User instructions.
- A link to fill the form with data - useful for testing. This would not be there in a final shipping product. The link calls the `fillForm()` function in [calculator.js](https://github.com/paulio11/project-2/blob/main/assets/js/calculator.js).
- Three user input sections:
    - **About You** - questions about the employee.
    - **About This Period** - questions about the current pay period. The dropdown box populates the calendar with the correct dates. An event listener calls the `populateCalendar()` function whenever this dropdown menu value is changed by the user.
    - **Hours You Have Worked** - Four tables, one for each week, where the user can input how many hours they have worked this period. Each week is calculated separately because of how overtime is computed.
- A reset button which clears the form.
- A calculate pay button calls the `handeSubmit()` functions. This shows the results below.
- Calculator Results. Shown once the user fills out the form and submits. This contains several `<span>` elements that are filled by calculator.js.

![Payday Calculator Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-calculator.png)

**[Understand Your Pay](https://paulio11.github.io/project-2/understand.html)** and **[Problems With Your Pay](https://paulio11.github.io/project-2/problems.html)**

Both the *Understand Your Pay* and *Problems With Your Pay* pages start with page contents. An unordered list with a left border to connect them stylistically. Every list item links to a section within each page.

Below is a simple display of information. Each bit of information or frequently asked question is in its own `<div>` container so it can be navigated to via the page contents and styled to stand apart from each other.

At the top of the *Understand Your Pay* page is a countdown to the next payday. This is is the output of an if statement comparing the current date with a list of paydays from an array within [payday.js](https://github.com/paulio11/project-2/blob/main/assets/js/payday.js).

![Understand Your Pay Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-understand.png)

![Problems With Your Pay Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-problems.png)

**[Quiz](https://paulio11.github.io/project2/quiz.html)**

Most of the content on this page is generated by JavaScript in [quiz.js](https://github.com/paulio11/project-2/blob/main/assets/js/quiz.js) and [questions.js](https://github.com/paulio11/project-2/blob/main/assets/js/questions.js).

The instruction box uses the same styles as the information on the *Understand Your Pay* and *Problems With Your Pay* pages. All content below is created using `document.createElement` within the javascript code. 

The innerText of the created elements comes from reading the value of the (question) `number` variable to get the question text. A `for` loop creates multiple elements with `click` event listeners to show the multiple choice answers. Styles are applied when the choices are created, giving them a `:hover` style. When an option is clicked, the hover style is removed and then the relevant style is applied, whether the selected answer was correct or incorrect. Additionally, the click event displays a continue button, either functioning as the *Next Question*, or *Check My Score* buttons based on the progress through the quiz defined by `questions.length`. This enables more questions to be added beyond what is currently available, and the quiz will still function correctly.

<details>
  <summary>Quiz Answers</summary>
  <ol>
    <li>Every four weeks</li>
    <li>Thursday</li>
    <li>PACE Salary Sacrifice</li>
    <li>Net Pay</li>
    <li>MyHR</li>
    <li>Paul's payday calculator is awesome</li>
    <li>Two 15 minute paid breaks and a 30 minute unpaid break</li>
  </ol>
</details>

![Quiz Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-quiz.png)

**[About](https://paulio11.github.io/project-2/about.html)**

Using the same `<div class="box">` for the information presented in understand.html and problems.html to display a simple about this website box.

![About Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-about.png)

**[Error 404](https://paulio11.github.io/project-2/404.html)** and **[Error 500](https://paulio11.github.io/project-2/500.html)**

The error pages are a copy of the design used for the home page. Containing the website logo, title, an explanation of the error and a Go Back button. The go back button jumps the user 1 page back in their history using JavaScript. The left arrow is from [Font Awesome](https://fontawesome.com/).

![Error Page Screenshot](https://paulio11.github.io/project-2/documentation/screenshot-error.png)

### Unimplemented Features
There were just a few things I would have liked to have added.

- **A more comprehensive source of information for employees** - I decided this wouldn’t be an effective use of my time, as it would just be more basic HTML and not display the required interactivity. Hopefully, you can see how you could quickly expand a website like this.
- **Calculator Improvemenets** - An easier way for employees to use the calculator would be to use what they already know, i.e. the shift *Start Time* and *End Time*. This way, a user wouldn’t have to calculate the length of the shift and instead just input what time they started and finished work. Ultimately the javascript calculation would remain the same but would have required an extra step at the start - working out the difference in the two date (time) values and using that instead of a simple hours value.
- **Payslip Information** - Another idea I wanted to implement was to explain the payslip in more detail - to expand the information available to the user further. A page dedicated to the payslip layout where a clickable, interactive example is shown. Clicking elements of the payslip would reveal more detailed information. I passed on this idea early on as it would have proven to be a relatively large amount of work to make something look like this clearly viewable on a smaller screen.

[Back to top 🔺](#co-op-your-pay)

## Bugs and Development Issues

Empty inputs on the calculator, specifically the hours worked when left blank, would cause errors while adding up the total hours worked. To fix this, I had to add an `if` statement into the `for` loop in the `addWeek()` function. This would skip the input if there was not a number (`isNaN`) and therefore bypass the issue.

Initially, I wanted to use start and end times instead of hours worked for the calculator - see [Unimplemented Features](#unimplemented-features). This would have made it easier for the user but would have been more work for me. As I am new to JavaScript, I settled on using a single hours input per shift. Deeper study into JavaScript, the `Date` function and the ways you can compare two dates, shows this would have likely have been very possible. 

Foolishly a lot of development time was spent on the username easter egg. Having just learnt about Local Storage, I wanted to try and implement something in this project. Turns out a `prompt`, even if cancelled or left blank, will have a variety of outcomes. To ensure I got what I wanted from it (and after much trial and error), an `if` statement was used to ignore all undesired outputs - `if (namePrompt === 'null' || namePrompt === null || namePrompt === '')`.

[Back to top 🔺](#co-op-your-pay)

## Technologies

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
    - You can see my stylesheet [here](https://github.com/paulio11/project-2/blob/main/assets/css/style.css).
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - You can see all my JavaScript files [here](https://github.com/paulio11/project-2/tree/main/assets/js).

### Other
- [Google Fonts](https://fonts.google.com/)
    - Fonts were imported from Google Fonts, see Typography section of readme above.
- [Font Awesome](https://fontawesome.com/)
    - Icons used in my project taken from Font Awesome.
- [GitHub](https://github.com/)
    - Used to store files, changes, and host the page.
- [GitPod](https://www.gitpod.io/)
    - Used to write, comment code, and commit to GitHub.
- [Balsamiq](https://balsamiq.com/)
    - Used to plan the layout of the pages before development.
- [Code Institute Student Template](https://github.com/Code-Institute-Org/gitpod-full-template)
    - Used as the basis of the project, helped to set up GitPod workspace.
- [Affinity Photo](https://affinity.serif.com/en-gb/photo/)
    - Used to edit images, resizing and optimizing them for use on a website.
- [Am I Responsive](https://ui.dev/amiresponsive)
    - Used to create the hero image at the top of this readme.
- [Free Formatter](https://www.freeformatter.com/html-formatter.html)
    - Recommended by my mentor and used to format my code before project submission.
- [W3C Markup Validation Service](https://validator.w3.org)
    - Used to validate HTML code.
- [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - Used to validate CSS code.
- [JSHint JavaScript Code Quality Tool](https://jshint.com)
    - Used to validated JavaScript code.

[Back to top 🔺](#co-op-your-pay)

## Testing

### Testing User Stories

**New Employee/User Goals**
- As a new employee, I want to quickly navigate to what I need.
    - Website navigation is forefront; the first thing the user sees when visiting the site, and available throughout each page via the overlay and sidebar menu, making it always clear and fast to navigate.
- As a new employee, I want the information to be clear, relevant and accurate.
    - Whether the user wants to find out more information or troubleshoot a problem, they can do just that. 
    - Clearly defined pages contain the information needed. Presented in separate sections and are navigable by page contents at the top of the page.
    - Information is accurate and taken directly from official Co-op employee resources.

**Current Employee/User Goals**
- As a current employee, I want help with the problems I have with my pay.
    - A whole page is dedicated to problems an employee might possibly have. Containing explanations and solutions.
- As a current employee, I want to know when payday is.
    - Using the JavaScript `Date` function and an array containing future paydays, the website can show the next payday and a countdown.
- As a current employee, I want help keeping track and calculating my pay.
    - The payday calculator is the main interactive element of the website. Clear and simple to use. An employee can enter their details here and see their estimated pay.

### Manual Testing

**Common Elements**
<details>
    <summary>Navigation and hover effects</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-sidebar.gif">
</details>
<br>

**[Home Page](https://paulio11.github.io/project-2)**
<details>
    <summary>Navigation and hover effects</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-homepage.gif">
</details>
<br>

**[Payday Calculator](https://paulio11.github.io/project-2/calculator.html)**
<details>
    <summary>Form Validation</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-calc-validation.gif">
</details>
<details>
    <summary>Reset Form Button</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-calc-reset.gif">
</details>
<details>
    <summary>populateCalendar Function</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-calc-calendar.gif">
</details>
<details>
    <summary>calculatePay Function</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-calc-calculate.gif">
</details>
<details>
    <summary>Responsive layout</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-calc-responsive.gif">
</details>
<br>

**[Understand Your Pay](https://paulio11.github.io/project-2/understand.html)**
<details>
    <summary>Page contents navigation</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-understand.gif">
</details>
<br>

**[Problems With Your Pay](https://paulio11.github.io/project-2/problems.html)**
<details>
    <summary>Page contents navigation</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-problems.gif">
</details>
<br>

**[Quiz](https://paulio11.github.io/project-2/quiz.html)**
<details>
    <summary>Starting the quiz</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-quiz-start.gif">
</details>
<details>
    <summary>Failing the quiz</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-quiz-failing.gif">
</details>
<details>
    <summary>Restarting the quiz</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-quiz-restarting.gif">
</details>
<details>
    <summary>Passing the quiz</summary>
    <img src="https://paulio11.github.io/project-2/documentation/testing/testing-quiz-passing.gif">
</details>
<br>

### Automated Testing

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate my HTML and CSS code. The [JSHint JavaScript Code Quality Tool](https://jshint.com) was also used to validate my JavaScript code. 

| File | Automated Testing Result | Notes
| ----------- | ----------- |----------- |
| 404.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-404.png) | Pass |
| 500.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-500.png) | Pass |
| about.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-about.png) | Pass |
| calculator.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-calculator.png) | Pass |
| index.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-index.png) | Pass |
| problems.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-problems.png) | Pass |
| quiz.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-quiz.png) | Pass |
| understand.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-understand.png) | Pass |
| style.css | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-css.png) | Pass |
| calculator.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-calculatorjs.png) | Pass |
| payday.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-payday.png) | Pass |
| questions.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-questions.png) | `questions` variable is used in `quiz.js` |
| quiz.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-quizjs.png) | `questions` variable defined in `questions.js` |
| sidebar.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-sidebar.png) | Pass |
| top.js | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-top.png) | Pass |

Also included are the results of Lighthouse. Scoring 100 in every category on every page.

| Page | Lighthouse Result|
| ----------- | ----------- |
| Error pages | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-error.png) |
| index.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-index.png) |
| understand.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-understand.png) |
| problems.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-problems.png) |
| quiz.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-quiz.png) |
| calculator.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-calculator.png) |
| about.html | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/lighthouse-about.png) |

### Browser Validation

| Browser | Screenshot |
| ----------- | ----------- |
| Google Chrome | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-chrome.png) |
| Microsoft Edge | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-edge.png) |
| Safari | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-safari.png) |
| Safari Mobile | [Screenshot](https://paulio11.github.io/project-2/documentation/testing/testing-safarimobile.jpeg) |

### User Testing

Many fellow Code Institute helped test the site during various stages of development. Nothing major was reported besides spelling and grammatical errors. 

My mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) helped point out issues with the outputs of the username prompt when the user would either cancel out or hit okay with a blank input. Other numerous suggestions were made throughout the project, too many to remember.

[Back to top 🔺](#co-op-your-pay)

## Deployment

Project written and developed in GitPod, which was then used to commit changes and push to GitHub. The site is hosted using GitHub Pages. 

### Download Code

To download a copy of this project and all required assets click the green **Code** button above the file tree at the top. Then **Download ZIP**. Alternatively click [here](https://github.com/paulio11/project-2/archive/refs/heads/main.zip).

### GitHub Pages Deployment Procedure

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate this [GitHub Repository](https://github.com/paulio11/project-2 "Link to GitHub Repo").
3. At the top of the repository, select Settings from the menu items.
4. Scroll down the Settings page to the "Pages" section.
5. Under "Source" click the drop-down menu labelled "None" and select "Main".
6. Upon selection, the page will automatically refresh meaning that the website is now deployed.
7. Scroll back down to the "Pages" section to retrieve the deployed link.

**Note:** when this website is hosted at a different URL - the image source for the logo, and the head link to the stylesheet and favicon will need to be manually changed to correctly style the error pages 404.html and 500.html.

[Back to top 🔺](#co-op-your-pay)

## Credits and Acknowledgements 

### Text
- Employee paydays taken from [Co-op Colleagues - See next paydays](https://colleagues.coop.co.uk/see-next-pay-days).
- Problems with your pay text taken from [Co-op Colleagues - Problems with your pay](https://colleagues.coop.co.uk/problems-with-your-pay).
- Understand your pay text taken from [Co-op Colleagues - Understand your payslip and pay deductions](https://colleagues.coop.co.uk/understand-your-payslip-and-pay-deductions).

### Images
- Co-op logo taken from [Co-op Assets](https://www.co-operative.coop/media/assets).

### Code
- Code for the [scroll to top button](https://github.com/paulio11/project-2/blob/main/assets/js/top.js) is based on a [How To tutorial at W3 Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp).
- Lines 112 to 125 in `calculator.js` created with help from a friend Dan Oak, adjusted to suit my needs and to fix an oversight of his.

### Acknowledgements

Thanks to my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) and the students from class June 2022 for their help and suggestions throughout the project.

I would also like to thank fellow CI student [Rebecca Rayner](https://github.com/Irishbecky91). Her excellent project readme was the basis of my own readme's structure.

[Back to top 🔺](#co-op-your-pay)