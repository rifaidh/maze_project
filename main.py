import tkinter as tk
from engine import GameState
from ui import MazeUI
import algorithm
import maze

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Game")
        self.root.configure(bg="#000000")
        
        self.state = GameState()

        callbacks = {
            'generate': self.handle_generate,
            'solve': self.handle_solve
        }
        
        self.ui = MazeUI(root, self.state, callbacks)
        
        self.root.bind("<KeyPress>", self.handle_keypress)
        
        self.handle_generate()

    def handle_generate(self):
            new_grid = maze.generate_maze_grid(self.state.rows, self.state.cols, self.state.start_pos, self.state.end_pos)
            self.state.reset_state(new_grid)
            self.ui.update_status("MANUAL PLAY: USE ARROW KEYS", self.ui.player_color)
            self.ui.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()
