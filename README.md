## Z3 Automated Tent Puzzle Solver

Tents ("Tents and Trees") puzzle is a logic grid-based puzzle invented by Léon Balmaekers [1]. Some squares within the grid contain trees, as shown in Figure 1, and the objective is to strategically place tents in the remaining squares under the following constraints:

- Each tree is connected to a tree horizontally or vertically, not diagonally. While a tree can be adjacent to two tents and a tent can be adjacent to two trees, the connections are 1:1 - a tent connects to only one tree, and vice versa.

- There are exactly as many tents as trees on the grid.

- No two tents are adjacent horizontally, vertically, or diagonally.

- Numbers positioned around the grid's perimeter indicate the required number of tents in each row and column, offering clues to their placement.


The provided solver uses the following file format for puzzles:

5 10 <br>
.......... 0 <br>
......T... 2 <br>
..T...T... 0 <br>
.......... 1 <br>
.......... 0 <br>
0 0 1 0 0 0 1 1 0 0 

The first line provides the dimensions of the puzzle (rows and columns). Then one line per row representing the puzzle, a dot for an empty cell or a T for a tree, after the line, separated by a space, follows the number of tents in the row. After the last line of the puzzle follow the numbers of tents for each column (separated by spaces).



## Requirmnets
Run  `pip install -r requirements.txt`

Edit `puzzle.txt` to provide input.

Run `python main.py` for puzzle solution.
