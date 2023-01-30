#include <stdio.h>
#include "game.h"
#include "endGame.h"

/*
  This module of code tests if the game has been won or drawn.
*/

// test all possible ways the game can be won for one player
int winGame( Game *game, char symbol ) {

  // Games can be won with horizontal, vertical or diagonal lines

  // check for a horizontal win
  for (int i = 0; i < game->boardSize; i++) {
    for (int j = 0; j < game->boardSize - game->winLength + 1; j++) {
      if (game->board[i][j] == symbol) {
        int win = 1;
        for (int k = 1; k < game->winLength; k++) {
          if (game->board[i][j + k] != symbol) {
            win = 0;
            break;
          }
        }
        if (win == 1) {
          return 1;
        }
      }
    }
  }

  // check for a vertical win
  for (int i = 0; i < game->boardSize - game->winLength + 1; i++) {
    for (int j = 0; j < game->boardSize; j++) {
      if (game->board[i][j] == symbol) {
        int win = 1;
        for (int k = 1; k < game->winLength; k++) {
          if (game->board[i + k][j] != symbol) {
            win = 0;
            break;
          }
        }
        if (win == 1) {
          return 1;
        }
      }
    }
  }

  // check for a diagonal win
  for (int i = 0; i < game->boardSize - game->winLength + 1; i++) {
    for (int j = 0; j < game->boardSize - game->winLength + 1; j++) {
      if (game->board[i][j] == symbol) {
        int win = 1;
        for (int k = 1; k < game->winLength; k++) {
          if (game->board[i + k][j + k] != symbol) {
            win = 0;
            break;
          }
        }
        if (win == 1) {
          return 1;
        }
      }
    }
  }

  // check for a reverse diagonal win
  for (int i = game->winLength - 1; i < game->boardSize; i++) {
    for (int j = 0; j < game->boardSize - game->winLength + 1; j++) {
      if (game->board[i][j] == symbol) {
        int win = 1;
        for (int k = 1; k < game->winLength; k++) {
          if (game->board[i - k][j + k] != symbol) {
            win = 0;
            break;
          }
        }
        if (win == 1) {
          return 1;
        }
      }
    }
  return 0;  // continue
  }
return 0;
}

// test for a draw
int drawGame( Game *game, char symbol ) {

  // game is drawn if all squares are filled and no player has won

  for (int i = 0; i < game->boardSize; i++) {
    for (int j = 0; j < game->boardSize; j++) {
      if (game->board[i][j] == '.') {
        return 0;
      }
    }
  }
  return 1;
}

