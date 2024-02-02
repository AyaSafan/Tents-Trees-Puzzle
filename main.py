from z3 import *
import puzzleParser
import puzzleOutput
import puzzleConstraints

grid_rows, grid_columns, trees, tent_counts_per_row, tent_counts_per_column = puzzleParser.parse_puzzle_file("puzzle.txt")


# Tent variables
tents = [[Bool("tent_at_%d_%d" % (i, j)) for i in range(grid_columns)] for j in range(grid_rows)]

solver = Solver()

puzzleConstraints.addConstraints(grid_rows, grid_columns, trees, tent_counts_per_row, tent_counts_per_column,  tents, solver)  

resultTents =[]
# Solve and output solution
if solver.check() == sat:
    m = solver.model()
    for i in range(grid_rows):
        for j in range(grid_columns):
            if is_true(m[tents[i][j]]):
                resultTents.append((i,j)) 
    print("The result tents: ") 
    print (resultTents) 
else:
    print("The problem is unsatisfiable.")

print("")
puzzleOutput.output_solved_puzzle(grid_rows, grid_columns, trees, tents, tent_counts_per_row, tent_counts_per_column, resultTents )



