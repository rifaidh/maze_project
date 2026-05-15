from collections import deque

def bfs_shortest_path(grid, start_pos, end_pos):
    queue = deque([(start_pos, [start_pos])])
    visited = {start_pos}
    found_path = []
    exploration_order = []

    max_rows = len(grid)
    max_cols = len(grid[0]) if grid else 0

    while queue:
        current, path = queue.popleft()
        
        if current != start_pos and current != end_pos:
            exploration_order.append(current)
        
        if current == end_pos:
            found_path = path
            break
            
        r, c = current
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < max_rows and 0 <= nc < max_cols:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return found_path, exploration_order
