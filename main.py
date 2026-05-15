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

if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()
