from z3 import *
import puzzleParser
import puzzleOutput


grid_rows, grid_columns, trees, tent_counts_per_row, tent_counts_per_column = puzzleParser.parse_puzzle_file("puzzle.txt")


last_row_index = grid_rows - 1
last_column_index = grid_columns -1

# Number of trees
num_trees = len(trees)

# Tent variables
tents = [[Bool("tent_at_%d_%d" % (i, j)) for i in range(grid_columns)] for j in range(grid_rows)]

# Constraints
solver = Solver()

# Rule 1: Enforce equal number of trees and tents
solver.add(Sum([tents[i][j] for i in range(grid_rows) for j in range(grid_columns)]) == num_trees)

# Rule 2: No tent and tree in same position
for i, j in trees:
    solver.add(Not(tents[i][j]))

# Rule 3: Each tree must have a unique adjacent tent 
for i, j in trees:
    if grid_rows == 1:  # One row case
        # Check left and right neighbors (but avoid accessing outside the grid)        
        if j == 0:  # Leftmost cell: only check right neighbor
            solver.add(tents[i][j + 1])
        elif j == last_column_index:  # Rightmost cell: only check left neighbor
            solver.add(tents[i][j - 1])
        elif j > 0 and j < last_column_index:
            solver.add(Or(tents[i][j - 1], tents[i][j + 1]))
    elif grid_columns == 1:  # One column case
        # Check top and bottom neighbors (but avoid accessing outside the grid)
        if i == 0:  # Topmost cell: only check bottom neighbor
            solver.add(tents[i + 1][j])
        elif i == last_row_index:  # Bottommost cell: only check top neighbor
            solver.add(tents[i - 1][j])
        elif i > 0 and i < last_row_index:
            solver.add(Or(tents[i - 1][j], tents[i + 1][j]))
            
    elif i == 0 and j == 0:  # tree on bottom right corner
        solver.add(Or(tents[i][j+1], tents[i+1][j]))
    elif i == last_row_index and j == 0:  # tree on top right corner
        solver.add(Or(tents[i][j+1], tents[i-1][j]))
    elif i == 0 and j == last_column_index:  # tree on bottom left corner
        solver.add(Or(tents[i][j-1], tents[i+1][j]))
    elif i == last_row_index and j == last_column_index:  # tree on top left corner
        solver.add(Or(tents[i][j-1], tents[i-1][j]))
    elif i == 0:  # tree on first row
        solver.add(Or(tents[i][j+1], tents[i][j-1], tents[i+1][j]))
    elif i == last_row_index:  # tree on last row
        solver.add(Or(tents[i][j+1], tents[i][j-1], tents[i-1][j]))
    elif j == 0: # tree on first column
        solver.add(Or(tents[i + 1][j], tents[i - 1][j], tents[i][j + 1]))
    elif j == last_column_index:  # tree on last column
        solver.add(Or(tents[i + 1][j], tents[i - 1][j], tents[i][j - 1]))
    else:
        solver.add(Or(tents[i - 1][j], tents[i][j - 1], tents[i][j + 1], tents[i + 1][j]))

## Rule 4: Enforce non-adjacency of tents (horizontally, vertically, diagonally)
for i in range(grid_rows):
    for j in range(grid_columns):
        # Prevent horizontal adjacency (left and right)
        if j > 0:  # Check for left neighbor
            solver.add(Not(And(tents[i][j], tents[i][j - 1])))
        if j < last_column_index:  # Check for right neighbor
            solver.add(Not(And(tents[i][j], tents[i][j + 1])))

        # Prevent vertical adjacency (top and bottom)
        if i > 0:  # Check for bottom neighbor
            solver.add(Not(And(tents[i][j], tents[i - 1][j])))
        if i < last_row_index:  # Check for top neighbor
            solver.add(Not(And(tents[i][j], tents[i + 1][j])))

        # Prevent diagonal adjacency (all four corners)
        if i > 0 and j > 0:  # Check bottom-left corner
            solver.add(Not(And(tents[i][j], tents[i - 1][j - 1])))
        if i > 0 and j < last_column_index:  # Check bottom-right corner
            solver.add(Not(And(tents[i][j], tents[i - 1][j + 1])))
        if i < last_row_index and j > 0:  # Check top-left corner
            solver.add(Not(And(tents[i][j], tents[i + 1][j - 1])))
        if i < last_row_index and j < last_column_index:  # Check top-right corner
            solver.add(Not(And(tents[i][j], tents[i + 1][j + 1])))


# Rule 5: Enforce tent counts per row
for i in range(grid_rows):
    solver.add(Sum(tents[i]) == tent_counts_per_row[i])

# Rule 6: Enforce tent counts per column
for j in range(grid_columns):
    solver.add(Sum([tents[i][j] for i in range(grid_rows)]) == tent_counts_per_column[j])


# Define allowed differences for vertical and horizontal adjacency between tree and tent
allowed_diffs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Rule 7: Enforce tent-tree relationships
for i, j in trees:
    has_tent_with_two_trees = False
    adjacent_tents = []
    for di, dj in allowed_diffs:
        if 0 <= i + di < grid_rows and 0 <= j + dj < grid_columns:
            tent_i, tent_j = i + di, j + dj
            adjacent_tents.append(tents[tent_i][tent_j])

            # Count adjacent trees for the adjacent tent:
            num_adjacent_trees = 0
            for tree_i, tree_j in trees:
                if (tree_i == tent_i and abs(tree_j - tent_j) == 1) or (tree_j == tent_j and abs(tree_i - tent_i) == 1):  # Ensure only vertical or horizontal adjacency
                    num_adjacent_trees += 1
            # Set has_tent_with_two_trees if necessary:
            if num_adjacent_trees >= 2:
                has_tent_with_two_trees = True
                break  # No need to check further adjacent tents

    num_adjacent_tents = Sum(adjacent_tents)
    # Add implication: If a tree has 2 adjacent tents, at least one of these tents must have 2 adjacent trees
    solver.add(Implies(num_adjacent_tents == 2, has_tent_with_two_trees))  



resultTents =[]
# Solve and output solution
if solver.check() == sat:
    m = solver.model()
    for i in range(grid_rows):
        for j in range(grid_columns):
            if is_true(m[tents[i][j]]):
                resultTents.append((i,j))
    puzzleOutput.output_solved_puzzle(grid_rows, grid_columns, trees, tents, tent_counts_per_row, tent_counts_per_column, resultTents )
    

else:
    print("The problem is unsatisfiable.")


