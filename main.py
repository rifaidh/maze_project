import tkinter as tk
from engine import GameState
import algorithm
import maze

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Game")
        self.root.configure(bg="#000000")
        
        self.state = GameState()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppController(root)
    root.mainloop()
