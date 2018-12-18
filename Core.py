import random

# **Print grid func**
def print_grid(grid):
    print("\n")
    for i in range(len(grid)):
        res = ''
        for j in range(len(grid[i])):
            res += str(grid[i][j]) + '\t\t'
        print(res)
        print("\n")

# **Move grid using CMDs**
def move(grid, cmd):

    # **If player enter UP**

    if cmd == 'UP':
        grid_shift_up(grid)

        for i in range(0, len(grid) - 1):
            for j in range(0, len(grid[i])):
                if grid[i][j] == grid[i + 1][j]:
                    grid[i][j] *= 2
                    grid[i + 1][j] = 0

        grid_shift_up(grid)

    # **If player enter DOWN**

    elif cmd == 'DOWN':
        grid_shift_down(grid)

        j = len(grid) - 1
        while j > -1:
            k = len(grid[j]) - 1
            while k > -1:
                if grid[j][k] == grid[j - 1][k]:
                    grid[j][k] *= 2
                    grid[j - 1][k] = 0
                k -= 1
            j -= 1

        grid_shift_down(grid)

    # **If player enter LEFT**

    elif cmd == 'LEFT':
        grid_shift_left(grid)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i]) - 1):
                if grid[i][j] == grid[i][j + 1]:
                    grid[i][j] *= 2
                    grid[i][j + 1] = 0

        grid_shift_left(grid)

    # **If player enter RIGHT**

    elif cmd == 'RIGHT':
        grid_shift_right(grid)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                k = len(grid[i]) - 1
                while k > 0:
                    if grid[i][k] == grid[i][k - 1]:
                        grid[i][k] *= 2
                        grid[i][k - 1] = 0
                    k -= 1

        grid_shift_right(grid)

        # **Generate 2 in free space**

        generate_value(grid)

# **Shift-func up**
def grid_shift_up(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i]) - 1):
            for k in range(0, len(grid[j])):
                if grid[j][k] == 0:
                    if grid[j + 1][k] != 0:
                        grid[j][k] = grid[j + 1][k]
                        grid[j + 1][k] = 0

# **Shift-func down**
def grid_shift_down(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i]) - 1):
            for k in range(0, len(grid[j])):
                if grid[j][k] != 0:
                    if grid[j + 1][k] == 0:
                        grid[j + 1][k] = grid[j][k]
                        grid[j][k] = 0

# **Shift-func left**
def grid_shift_left(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            for k in range(0, len(grid[j]) - 1):
                if grid[j][k] == 0:
                    if grid[j][k + 1] != 0:
                        grid[j][k] = grid[j][k + 1]
                        grid[j][k + 1] = 0

# **Shift-func right**
def grid_shift_right(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            for k in range(0, len(grid[j]) - 1):
                if grid[j][k] != 0:
                    if grid[j][k + 1] == 0:
                        grid[j][k + 1] = grid[j][k]
                        grid[j][k] = 0

# **Generate-func 2 in free space**
def generate_value(grid):

    list_rnd_rows = []
    list_rnd_cols = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                list_rnd_rows.append(i)
                list_rnd_cols.append(j)

    get_random_pos(grid, list_rnd_rows, list_rnd_cols)

# **Get free space in greed**
def get_random_pos(grid, rows, cols):
    random_number = random.choice(rows)

    for row_value in rows:
        if row_value == random_number:
            rnd_row_index = rows.index(row_value)
            rnd_row = row_value

    rnd_col = cols[rnd_row_index]
    grid[rnd_row][rnd_col] = 2

# **Game start func**
def game_start():
    i = 0;
    main_grid = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

    generate_value(main_grid)
    generate_value(main_grid)

    print_grid(main_grid)

    while i == 0:
        command = input("Input command: ")
        move(main_grid, command)
        print_grid(main_grid)

# **START GAME**
game_start()



