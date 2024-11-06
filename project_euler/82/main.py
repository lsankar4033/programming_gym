import math

with open('./matrix.txt') as f:
    lines = f.readlines()
    matrix_rows = [[int(c) for c in line.split(",")] for line in lines]
    matrix_cols = [[matrix_rows[r][c] for r in range(len(matrix_rows))] for c in range(len(matrix_rows[0]))]

num_rows = len(matrix_rows)
num_cols = len(matrix_cols)

# best solution for getting to each point
best_sols = [[math.inf] * num_cols] * num_rows
for col in range(num_cols):

    # iterate through col making each sol better until no longer possible

    pass


# returns next col
def find_next_col_sols(prev_col_sols, cur_col_vals):
    # iterate until we find a stable solution
    new_col_sols = [math.inf] * len(cur_col_vals)

    # change condition here to be stability change
    stable = False
    while not stable:
        new_sols = [math.inf] * len(cur_col_vals)

        for r in range(len(cur_col_vals)):
            candidates = [
                new_col_sols[r],
                prev_col_sols[r] + cur_col_vals[r]
            ]
            if r > 0:
                candidates.append(new_col_sols[r - 1] + cur_col_vals[r])
            if r < len(cur_col_vals) - 1:
                candidates.append(new_col_sols[r + 1] + cur_col_vals[r])

            new_sols[r] = min(candidates)

        stable = True if new_sols == new_col_sols else False 
        new_col_sols = new_sols

    return new_col_sols

sols = [list(matrix_cols[0])]

for c in range(1, num_cols):
    sols.append(find_next_col_sols(sols[-1], matrix_cols[c]))

print(min(sols[-1]))