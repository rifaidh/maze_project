import tkinter as tk
from tkinter import messagebox
import math

class MazeUI:
    def __init__(self, root, state, callbacks):
        self.root = root
        self.state = state
        self.callbacks = callbacks

        # ── New color theme: "Bioluminescent Jungle" ────────────────────────
        # Dark green background like a night forest
        self.bg_color        = "#0A1628"  
        self.panel_color     = "#0F2040"   

        # Maze elements
        self.wall_color      = "#1A3A5C"  
        self.wall_accent     = "#2E6A9E"   
        self.floor_color     = "#060F1E"   

        # Interactive and path colors
        self.explore_color   = "#00C896"
        self.explore_mid     = "#007A5E"   
        self.path_color      = "#FFD166"  
        self.path_glow       = "#FF9E2C"   

        # Titik penting
        self.start_color     = "#06FFB4"   
        self.end_color       = "#FF4D8F"   

        # Pemain
        self.player_color    = "#A259FF"   
        self.player_trail    = "#6B2FCC"   

        # Teks & UI
        self.text_bright     = "#E8F4FD"  
        self.text_muted      = "#7BA3C4"  
        self.accent_gold     = "#FFD166"   
        self.accent_pink     = "#FF4D8F"   
        self.accent_teal     = "#06FFB4"   

        self.cell_size = 15
        self.rectangles = {}
        self._explore_step = 0             
        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg=self.bg_color)
        self.root.title("🌿 MAZE EXPLORER")

        # Header
        header = tk.Frame(self.root, bg=self.bg_color)
        header.pack(fill="x", padx=0, pady=0)

        title_lbl = tk.Label(
            header, text="✦  MAZE EXPLORER  ✦",
            font=("Courier New", 15, "bold"),
            bg=self.bg_color, fg=self.accent_gold
        )
        title_lbl.pack(pady=(14, 0))

        self.lbl_status = tk.Label(
            self.root,
            text="🕹  MANUAL PLAY  ·  USE ARROW KEYS",
            font=("Courier New", 10),
            bg=self.bg_color, fg=self.accent_teal
        )
        self.lbl_status.pack(pady=(4, 10))

        # Button
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=(0, 12))

        # Generate Button
        self.btn_gen = tk.Button(
            btn_frame, text="GENERATE MAZE",
            font=("Courier New", 11, "bold"),
            bg=self.wall_color, fg=self.accent_gold,
            activebackground=self.wall_accent, activeforeground=self.accent_gold,
            relief="flat", padx=14, pady=6, cursor="hand2",
            bd=0, highlightthickness=2, highlightbackground=self.accent_gold,
            command=self.callbacks['generate']
        )
        self.btn_gen.grid(row=0, column=0, padx=10)

        # Solve Button
        self.btn_solve = tk.Button(
            btn_frame, text="FIND PATH",
            font=("Courier New", 11, "bold"),
            bg=self.wall_color, fg=self.accent_pink,
            activebackground=self.wall_accent, activeforeground=self.accent_pink,
            relief="flat", padx=14, pady=6, cursor="hand2",
            bd=0, highlightthickness=2, highlightbackground=self.accent_pink,
            command=self.callbacks['solve']
        )
        self.btn_solve.grid(row=0, column=1, padx=10)

        # Border
        canvas_frame = tk.Frame(
            self.root, bg=self.accent_gold,
            padx=2, pady=2,
            highlightthickness=0
        )
        canvas_frame.pack(padx=20, pady=(0, 8))

        inner_frame = tk.Frame(canvas_frame, bg=self.bg_color, padx=4, pady=4)
        inner_frame.pack()

        self.canvas = tk.Canvas(
            inner_frame,
            width=self.state.cols * self.cell_size,
            height=self.state.rows * self.cell_size,
            bg=self.floor_color, highlightthickness=0
        )
        self.canvas.pack()

        # Grid
        for r in range(self.state.rows):
            for c in range(self.state.cols):
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.wall_color, outline=""
                )
                self.rectangles[(r, c)] = rect

        # Footer Legends
        legend_frame = tk.Frame(self.root, bg=self.bg_color)
        legend_frame.pack(pady=(0, 12))

        legend_items = [
            ("▣", self.start_color,   "Start"),
            ("▣", self.end_color,     "Finish"),
            ("▣", self.player_color,  "Player"),
            ("▣", self.explore_color, "Exploration"),
            ("▣", self.path_color,    "Shortest Path"),
        ]
        for i, (sym, col, label) in enumerate(legend_items):
            tk.Label(
                legend_frame, text=f"{sym} {label}",
                font=("Courier New", 9),
                bg=self.bg_color, fg=col
            ).grid(row=0, column=i, padx=8)

    # 
    def get_cell_color(self, r, c):
        if (r, c) == self.state.start_pos:
            return self.start_color
        elif (r, c) == self.state.end_pos:
            return self.end_color
        elif self.state.grid[r][c] == 1:
            return self.wall_color
        else:
            return self.floor_color

    def draw_grid(self):
        for r in range(self.state.rows):
            for c in range(self.state.cols):
                color = self.get_cell_color(r, c)
                self.canvas.itemconfig(self.rectangles[(r, c)], fill=color)

        pr, pc = self.state.player_pos
        self.canvas.itemconfig(self.rectangles[(pr, pc)], fill=self.player_color)

    def update_player_move(self, old_pos, new_pos):
        old_color = self.get_cell_color(old_pos[0], old_pos[1])
        self.canvas.itemconfig(self.rectangles[old_pos], fill=old_color)
        self.canvas.itemconfig(self.rectangles[new_pos], fill=self.player_color)

    def update_status(self, text, color):
        self.lbl_status.config(text=text, fg=color)

    def show_win_message(self):
        self.update_status("YOU WIN!  Congratulations, you did it!", self.accent_gold)
        messagebox.showinfo("You Win!", "Amazing! You reached the finish line!")

    def show_error_message(self):
        messagebox.showinfo("Error", "No valid path could be found!")

    # AI Exploration Animation
    def animate_exploration(self, exploration, path, index):
        if index < len(exploration):
            r, c = exploration[index]
            ratio = index / max(len(exploration) - 1, 1)
            color = self._lerp_color(self.explore_color, self.explore_mid, ratio)
            self.canvas.itemconfig(self.rectangles[(r, c)], fill=color)
            self.root.after(10, self.animate_exploration, exploration, path, index + 1)
        else:
            self.animate_path(path, 0)

    # Shortest Path Animation
    def animate_path(self, path, index):
        if index < len(path):
            r, c = path[index]
            if (r, c) != self.state.start_pos and (r, c) != self.state.end_pos:
                # Path flashes between yellow and orange based on position
                ratio = (index / max(len(path) - 1, 1))
                color = self._lerp_color(self.path_color, self.path_glow, ratio)
                self.canvas.itemconfig(self.rectangles[(r, c)], fill=color)
            self.root.after(20, self.animate_path, path, index + 1)
        else:
            self.update_status(
                "✦  Shortest path found!  ✦",
                self.path_color
            )

    @staticmethod
    def _lerp_color(hex1: str, hex2: str, t: float) -> str:
        """Linearly interpolate between two hex colors."""
        t = max(0.0, min(1.0, t))
        r1, g1, b1 = int(hex1[1:3], 16), int(hex1[3:5], 16), int(hex1[5:7], 16)
        r2, g2, b2 = int(hex2[1:3], 16), int(hex2[3:5], 16), int(hex2[5:7], 16)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return f"#{r:02X}{g:02X}{b:02X}"