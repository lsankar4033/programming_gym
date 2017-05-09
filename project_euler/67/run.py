# Maximum path sum 2 (and 1)
# Problem here: https://projecteuler.net/problem=67
# For each element in the triangle, calculate the maximum path total starting at that node. Each of these
# subproblems is only dependant on the solutions to the two problems below it, so dynamic programming can help
# us avoid repeating work.
# Go through the cells row by row, starting with the bottom row.
TRIANGLE_FILE = "triangle.txt"
TRIANGLE_FILE_EASY = "triangle_easy.txt"

def read_triangle(triangle_file):
    rows = []
    with open(triangle_file) as f:
        for line in f.readlines():
            rows.append([int(i) for i in line.strip().split(" ")])

    return rows

if __name__ == "__main__":
    triangle_rows = read_triangle(TRIANGLE_FILE)
    subproblem_sols = {}

    for row_i in range(len(triangle_rows) - 1, -1, -1):
        if row_i == len(triangle_rows) - 1:
            # Base case
            for (col_i, num) in enumerate(triangle_rows[row_i]):
                subproblem_sols[(row_i, col_i)] = num

        else:
            # Use appropriate next rows solutions for each
            for (col_i, num) in enumerate(triangle_rows[row_i]):
                best_child = max(subproblem_sols[(row_i + 1, col_i)], subproblem_sols[(row_i + 1, col_i + 1)])
                subproblem_sols[(row_i, col_i)] = num + best_child

    print("Solution: {}".format(subproblem_sols[(0, 0)]))
