def output_solved_puzzle(grid_rows, grid_columns, trees, tents, tent_counts_per_row, tent_counts_per_column, resultTents):
    puzzle_rows = []
    for i in range(grid_rows - 1, -1, -1):  # Iterate from bottom to top
        row = ""
        for j in range(grid_columns):
            if (i, j) in trees:
                row += "T "
            elif (i, j) in resultTents:
                row += "# "
            else:
                row += ". "
        puzzle_rows.append(row)

    # Print the puzzle and counts (unchanged):
    print(grid_rows, grid_columns)
    for row in puzzle_rows:  # Print rows in bottom-to-top order
        print(row, tent_counts_per_row[len(puzzle_rows) - 1 - puzzle_rows.index(row)])  # Match tent counts
    print(" ".join(map(str, tent_counts_per_column)))

