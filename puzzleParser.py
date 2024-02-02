def parse_puzzle_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

        # Parse grid dimensions:
        grid_rows, grid_columns = map(int, lines[0].strip().split())

        # Parse tent counts:
        tent_counts_per_row = []
        tent_counts_per_column = list(map(int, lines[-1].strip().split()))

        # Parse trees and tent counts per row:
        trees = []
        for i in range(len(lines) - 2, 0, -1):  # Iterate from bottom to top
            row_data = lines[i].strip().split()
            puzzle_row = row_data[0]
            tent_count_row = int(row_data[1])
            tent_counts_per_row.append(tent_count_row)

            for j, cell in enumerate(puzzle_row):
                if cell == "T":
                    trees.append((len(lines) - 2 - i, j))  # Adjust for 0-based indexing and bottom-up counting

    return grid_rows, grid_columns, trees, tent_counts_per_row, tent_counts_per_column
