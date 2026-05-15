from collections import deque

def bfs_shortest_path(grid, start_pos, end_pos):
    queue = deque([(start_pos, [start_pos])])
    visited = set([start_pos])
    found_path = []
    exploration_sequence = []

    while queue:
        current, path = queue.popleft()
        
        if current != start_pos and current != end_pos:
            exploration_sequence.append(current)
        
        if current == end_pos:
            found_path = path
            break
            
        r, c = current
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return found_path, exploration_sequence
