from collections import deque

def bfs_shortest_path(grid, start_pos, end_pos):
    queue = deque([(start_pos, [start_pos])])
    visited = set([start_pos])
    jalur_ditemukan = []
    urutan_eksplorasi = []

    while queue:
        sekarang, path = queue.popleft()
        
        if sekarang != start_pos and sekarang != end_pos:
            urutan_eksplorasi.append(sekarang)
        
        if sekarang == end_pos:
            jalur_ditemukan = path
            break
            
        r, c = sekarang
        arah = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in arah:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return jalur_ditemukan, urutan_eksplorasi