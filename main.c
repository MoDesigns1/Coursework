#include <stdio.h>
#include <stdlib.h>
#include "game.h"
#include "initGame.h"
#include "playGame.h"

/*
 * main function: program entry point
 */

int main( int argc, char *argv[] ) {

  Game *game; // pointer for the game structure

  if (argc != 3) {
    printf("Incorrect parameter values for board size or win length. Exiting\n");
    return 0;
  }
  else {
    int boardSize = atoi(argv[1]);
    int winLength = atoi(argv[2]);
    game = initGame(boardSize, winLength);
    if (game == NULL) {
      return 0;
    }
    else {
      playGame(game);
      free(game);
    }
  }
  
  return 0;
}

