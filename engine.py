class GameState:
    def __init__(self, rows=41, cols=41):
        self.rows = rows
        self.cols = cols
        self.start_pos = (1, 1)
        self.end_pos = (self.rows - 2, self.cols - 2)
        
        self.player_pos = list(self.start_pos)
        self.is_playing = True
        self.grid = []

    def reset_state(self, new_grid):
        self.grid = new_grid
        self.player_pos = list(self.start_pos)
        self.is_playing = True

    def move_player(self, event_keysym):
        if not self.is_playing: 
            return None, None

        r, c = self.player_pos
        move = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
        
        if event_keysym in move:
            dr, dc = move[event_keysym]
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                old_pos = (r, c)
                self.player_pos = [nr, nc]
                return old_pos, (nr, nc)
                
        return None, None

    def check_win(self):
        if tuple(self.player_pos) == self.end_pos:
            self.is_playing = False
            return True
        return False
