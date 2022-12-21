# Classic Battleship game
The old classic board game of battleship brought back to your screen.<br>
The game runs in Heroku terminal.<br>
<br>
The goal of the game is to sink your opponents ships before they sink yours.<br> 
<link future link when project is live on heroku>

## How to play
The game is based on classic paper-pen game. You can read more about it on <link wikipedia><br>
In my version of the game, at the start user will be asked to enter their username, followed by game rules.<br>
Computer then randomly place 5 ships on 8x8 board and display the two boards for the player.<br>
Player will be asked to type in shot row and shot column.<br>
After input the two boards will be printed again with marked shots.<br>
Winner of the game is who sinks all of opponents ships first.

## Existing Features
* Game board random generated 
    * Players and computers ships are randomly placed at the start of the game.
    * Computers ships are hidden from Player.

    Picture of game board

* User input validation
    * User input can not be empty
    * User input has to be within range stated
    * Guesses at same location are not valid

    Picture of game board 

## Features for future implementation 
* For player to place ships themselves
* Different size ships
* For player to decide on the size of the game board

## Testing
* Code has passed PEP8
* Game has been tested in gitpod terminal and Heroku terminal 
* Tested all variations of input to make sure it is accepted and game does not crash
from empty user input

## Bugs

### Solved Bugs