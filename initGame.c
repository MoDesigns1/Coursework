#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "game.h"
#include "initGame.h"

/*
 * This module of code initialises the game data structure.
 */

Game *initGame( int boardSize, int winLength ) {

  Game *game;

  // checks if boardsize or win length is invalid.
  if (boardSize < 3 || winLength < 3 || winLength > boardSize || boardSize > 8 || winLength > 8) {
    printf("Incorrect parameter values for board size or win length. Exiting\n");
    return NULL;
  }

  // allocate the Game data structure
  game = (Game *)malloc(sizeof(Game));
  if (game == NULL) {
    return NULL;
  }

  // intialise the Game data structure values 
  game->boardSize = boardSize;
  game->winLength = winLength;
  game->maxTurns = boardSize * boardSize;
  game->turns = 0;

  // board values should be set to '.' (using strcpy)
  for (int i = 0; i < boardSize; i++) {
    for (int j = 0; j < boardSize; j++) {
      strcpy(&game->board[i][j], ".");
    }
  }

  return game;
}


