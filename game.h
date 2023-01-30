
/*
 * data structure for the game
 */

typedef struct _game {
  int boardSize;        // board size 
  char board[9][9];    // board for storing the game state
  int winLength;       // length of a winning line
  int maxTurns;        // maximum possible moves
  int turns;           // current number of moves
} Game;


