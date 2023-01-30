#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include "game.h"
#include "playGame.h"
#include "endGame.h"

/*
 * Controls the game logic from start to end
 */

void playGame( Game *game ) {

  // initialize variables
  char symbols[2] = { 'X','O' };
  int player = 0;

  // starting board
  printf("New game starting\n");
  showGame(game);

  while (game->turns < game->maxTurns) {
    // initialize variables
    int row, col;
    int index1, index2;
    int start = 0;
    int invalid;
    int BUFFER = 500;
    char input[BUFFER];

    // loop through inputs until valid one is entered
    printf("Player %c: Enter your move as row column values:\n",symbols[player]);
    do {
      invalid = 0;
      fgets(input, BUFFER, stdin);
      // loops through input to find digits.
      if (strlen(input) < 3) {
        row = -1;
        col = -1;
        invalid = 1;
      }
      for (int j = 0; j < strlen(input)-1; j++) {
        // if input is not a digit or space then it is invalid.
        if (invalid){
          j = strlen(input);
          break;
        }
        if (!(isspace(input[j])) && !(isdigit(input[j]))) {
          row = -1;
          col = -1;
          invalid = 1;
        }
        else if (isdigit(input[j])) {
          // if input is a digit then it's index is stored in index1.
          index1 = j;
          // loops through input to find second digit.
          for (int k = index1+1; k < strlen(input)-1; k++){
            if (invalid) {
              k = strlen(input);
              break;
            }
            // if input is not a digit or space then it is invalid.
            if (!(isspace(input[k])) && !(isdigit(input[k]))) {
              row = -1;
              col = -1;
              invalid = 1;
            }
            else if (isdigit(input[k])) {
              // if input is a digit then it's index is stored in index2.
              index2 = k;
              start = k;
              // breaks both for loops.
              k = strlen(input);
              j = strlen(input);
              break;
            }
          }
        }
      }
      if (!invalid) {
        row = atoi(&input[index1]);
        col = atoi(&input[index2]);
        if (!(checkWhite(input, start))) {
        row = -1;
        col = -1;
        invalid = 1;
        }
      }
      if (row < 0 || row >= game->boardSize || col < 0 || col >= game->boardSize || invalid == 1) {
        printf("Move rejected. Please try again\n");
      }
    } while (row < 0 || row >= game->boardSize || col < 0 || col >= game->boardSize || invalid == 1);

    // Calls on makeMove to try the move, if its not possible then an error message appears.
    if (makeMove(game, symbols[player], row, col) != 1) {
      printf("Move rejected. Please try again\n");
      continue;
    }

    showGame(game); // Game board is shown after every move.

    // Checks if the current player has won the game.
    if (winGame(game, symbols[player]) == 1) {
      printf("Player %c has won\n", symbols[player]);
      break;
    }

    // Checks if match ended as a draw.
    if (drawGame(game, symbols[player] == 1)) {
      printf("Match is drawn\n");
      break;
    }

    player = 1 - player; // Switches player.

  }
  return;
}

int checkWhite(char *input, int start) {
  for (int x = start+1; x < strlen(input); x++) {
    if (!(isspace(input[x]))) {
      return 0;
    }
  }
  return 1;
}

/*
 * Display the game board
 */

void showGame( Game *game ) {
  // prints the game board.
  printf("\n");
  printf("      ");
  // uses for loop to dynamically print board in relation to size.
  for (int i = 0; i < game->boardSize; i++) {
    printf("%d  ", i);
  }
  printf("\n");
  printf("\n");
  for (int i = 0; i < game->boardSize; i++) {
    printf(" %d    ", i);
    for (int j = 0; j < game->boardSize; j++) {
      printf("%c  ", game->board[i][j]);
    }
    printf("\n");
  }
  printf("\n");
  return;
}


int makeMove( Game *game, char symbol, int row, int col) {
  // check the move is valid
  if (game->board[row][col] == 'X' || game->board[row][col] == 'O') {
    return 0;
  }
  
  // if valid update the board and return 1
  game->board[row][col] = symbol;
  game->turns++;
  return 1;
}

  

