import random

def generate_maze_grid(rows, cols, start_pos, end_pos):
    grid = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = [start_pos]
    grid[start_pos[0]][start_pos[1]] = 0

    while stack:
        r, c = stack[-1]
        tetangga_valid = []
        arah = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        
        for dr, dc in arah:
            nr, nc = r + dr, c + dc
            if 0 < nr < rows-1 and 0 < nc < cols-1 and grid[nr][nc] == 1:
                tetangga_valid.append((nr, nc, dr, dc))

        if tetangga_valid:
            nr, nc, dr, dc = random.choice(tetangga_valid)
            grid[r + dr//2][c + dc//2] = 0
            grid[nr][nc] = 0
            stack.append((nr, nc))
        else:
            stack.pop()

    grid[end_pos[0]][end_pos[1]] = 0
    grid[end_pos[0]-1][end_pos[1]] = 0 
    return grid