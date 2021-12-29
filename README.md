# Quoridor

Details about the game, validation rules, implementation, game play are below.

## Game

You can see the rules of the game in this [video](https://www.youtube.com/watch?v=6ISruhN0Hc0) and [Page 9 of this educative-sheet_quoridor-english.pdf](https://en.gigamic.com/files/media/fiche_pedagogique/educative-sheet_quoridor-english.pdf) 

The game is made for 2 players.  Each player will have 10 fences.

The board is formed by 9x9 cells, and the pawn will move on the cells.  The fence will be placed on the edges of the cells.  The four sides of the board are treated as fences and no more fence should be placed on top of it.

The board should be treated as the following picture shows:

![162-u21-portfolio-project-quorridor-board](https://user-images.githubusercontent.com/230170/127580651-5de99bfd-d7d4-4492-9ef2-a5615f0e8b3b.png)

 
The cell coordinates are expressed in `(x,y)` where `x` is the column number and `y` is the row numberThe board positions start with `(0,0)` and end at `(8,8)`. At the beginning of the game, player 1 places pawn 1 (P1) on the top center of the board and player 2 places pawn 2 (P2) on the bottom center of the board.  The position of P1 and P2 is `(4,0)` and `(4,8)` when the game begins.   

The four edges are labeled as fences. The row of the cells where the pawns are positioned at the start of the game are called base lines. A fence is 1 cell long in contrast to what you find the video and PDF saying.

When each player tries to place a fence on the board, the position of the fence is defined by a letter and coordinates.  For vertical fences, we use `v` and for horizontal fences, we use `h`.  As an example, for the blue fence (vertical) in the picture, we use the coordinate of the top corner to define it and for the red fence (horizontal), we use coordinate of the left corner to define it. 

## How to play the game?

Here's an example of how to play a game:

```
q = QuoridorGame()
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
q.move_pawn(1, (4,1)) #moves the Player1 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- out of turn move, returns False 
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- returns True
q.place_fence(2, 'v',(3,3)) #places Player2's fence -- returns True
q.is_winner(1) #returns False because Player 1 has not won
q.is_winner(2) #returns False because Player 2 has not won

```
