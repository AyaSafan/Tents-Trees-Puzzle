Tents (sometimes known as "Tents and Trees") is a popular logic puzzle.  
It was first published by Léon Balmaekers with the Dutch name "Alle Ballen Verzamelen" in 1989.

Some webpages with Tent puzzles:

https://www.puzzle-tents.com/
https://www.brainbashers.com/tents.asp
https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/tents.html

Here is a summary of the rules

- Place tents on the grid so each tree has a unique horizontally or vertically adjacent tent. This also means that no tent can "serve" more than one tree.
- Tents should not be adjacent to each other (neither horizontally, nor vertically, and also not diagonally).
T- he given numbers for rows and columns have to be equal to the number of tents placed in the respective row or column.

Use the following file format for puzzles:

5 10
.......... 0
......T... 2
..T...T... 0
.......... 1
.......... 0
0 0 1 0 0 0 1 1 0 0
The first line provides the dimensions of the puzzle (rows and columns). Then one line per row representing the puzzle, a dot for an empty cell or a T for a tree, after the line, separated by a space, follows the number of tents in the row. After the last line of the puzzle follow the numbers of tents for each column (separated by spaces).
