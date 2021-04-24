# funge-bot
A bot for playing befunge chess on a discord server.

## Rules

[courtesy of Lyxal's gist](https://gist.github.com/Lyxal/b1ebdbbd8deb5b4c7911b8bd0d5707e6)

The general gist of **Befunge Chess** is to make the instruction pointer land on a specific target cell while avoiding the opponent's target cell.

Befunge chess is a 2-player game. The players are called A and B At the start of the game, a board is randomly generated with two cells already filled, like so:

```
.....
.....
.A...
.....
...B.
```

The A and the B can go anywhere on the board - their position is arbitrary. However, they cannot go in the top left corner where the instruction pointer would start.

Players take turns placing commands from a modified subset of Befunge commands onto the board in an attempt to make the instruction pointer reach their target square. These commands will be described in their own section. The board is not executed during this phase.

On a player's turn, if they feel that the instruction pointer will land on their target cell, they can choose to execute the board instead of placing a command. This initiates the end sequence of the game. If the instruction pointer does reach the executing player's target piece they win. If it doesn't (i.e. it a) reaches the opponent's target piece, b) reaches a cell it's already passed or c) errors), then the other player wins. Note: stop condition b means that there aren't any infinite loops - hence there will always be an outcome for every possible board

If the board is completely full, then execution is automatic. Errors/reaching an already passed square lead to a tie.

### The Pieces

```
<>^v|_?# all do the same as regular befunge
. is a nop
A and B are the target cells
+-*/% all impact the side stack (add, sub, mul, div, mod) 
\ swaps top two side stack values
@ is a double jump
" toggles string mode
0-9 impact side stack
```

On each turn, the player is given 4 pieces chosen at random. The pieces have a board effect and a stack effect, and can be played as either but not both.

The side stack is a stack of numbers that, upon execution of the board, is used as the primary stack.

The general gist of **Befunge Chess** is to make the instruction pointer land on a specific target cell while avoiding the opponent's target cell.

Befunge chess is a 2-player game. The players are called A and B At the start of the game, a board is randomly generated with two cells already filled, like so:

```
.....
.....
.A...
.....
...B.
```

The A and the B can go anywhere on the board - their position is arbitrary. However, they cannot go in the top left corner where the instruction pointer would start.

Players take turns placing commands from a modified subset of Befunge commands onto the board in an attempt to make the instruction pointer reach their target square. These commands will be described in their own section. The board is not executed during this phase.

On a player's turn, if they feel that the instruction pointer will land on their target cell, they can choose to execute the board instead of placing a command. This initiates the end sequence of the game. If the instruction pointer does reach the executing player's target piece they win. If it doesn't (i.e. it a) reaches the opponent's target piece, b) reaches a cell it's already passed or c) errors), then the other player wins. Note: stop condition b means that there aren't any infinite loops - hence there will always be an outcome for every possible board

If the board is completely full, then execution is automatic. Errors/reaching an already passed square lead to a tie.

### The Pieces

```
<>^v|_?# all do the same as regular befunge
. is a nop
A and B are the target cells
+-*% all impact the side stack (add, sub, mul, div, mod) 
/\ move the instruction pointer diagonally
@ is a double jump
" toggles string mode
0-9 impact side stack
```

On each turn, the player is given 4 pieces chosen at random. The pieces have a board effect and a stack effect, and can be played as either but not both.

The side stack is a stack of numbers that, upon execution of the board, is used as the primary stack.

