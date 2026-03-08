import tkinter as tk

from bfs_logic import run_bfs
from ui_builder import build_ui

from settings import (
    CELL_SIZE,
    COLOR_BG,
    COLOR_EMPTY,
    COLOR_END_FILL,
    COLOR_GRID_LINE,
    COLOR_PATH,
    COLOR_START,
    COLOR_START_FILL,
    COLOR_WALL,
    COLS,
    PADDING,
    ROWS,
)


class PathfindingVisualizer:
    def __init__(self):
        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.start_cell = None
        self.end_cell = None
        self.mode = "wall"
        self.running = False

        self.root = tk.Tk()
        self.root.title("Pathfinding Visualizer - BFS")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        self.canvas_w = COLS * CELL_SIZE + PADDING * 2
        self.canvas_h = ROWS * CELL_SIZE + PADDING * 2

        build_ui(self)
        self.set_mode("wall")
        self.refresh_grid()

    def cell_coords(self, row, col):
        x1 = PADDING + col * CELL_SIZE
        y1 = PADDING + row * CELL_SIZE
        return x1, y1, x1 + CELL_SIZE, y1 + CELL_SIZE

    def draw_cell(self, row, col, color, dot_color=None):
        x1, y1, x2, y2 = self.cell_coords(row, col)
        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill=color,
            outline=COLOR_GRID_LINE,
            width=1,
        )
        if dot_color:
            margin = 5
            self.canvas.create_oval(
                x1 + margin,
                y1 + margin,
                x2 - margin,
                y2 - margin,
                fill=dot_color,
                outline="",
            )

    def refresh_grid(self):
        self.canvas.delete("all")
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) == self.start_cell:
                    self.draw_cell(row, col, COLOR_START, COLOR_START_FILL)
                elif (row, col) == self.end_cell:
                    self.draw_cell(row, col, COLOR_EMPTY, COLOR_END_FILL)
                elif self.grid[row][col] == 1:
                    self.draw_cell(row, col, COLOR_WALL)
                else:
                    self.draw_cell(row, col, COLOR_EMPTY)

    def bfs(self):
        run_bfs(self)

    def get_cell(self, event):
        col = (event.x - PADDING) // CELL_SIZE
        row = (event.y - PADDING) // CELL_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            return row, col
        return None

    def on_click(self, event):
        if self.running:
            return
        cell = self.get_cell(event)
        if not cell:
            return
        row, col = cell

        if self.mode == "start":
            self.start_cell = (row, col)
            self.grid[row][col] = 0
            self.refresh_grid()
            self.status_var.set(f"Start set at ({row}, {col})")
        elif self.mode == "end":
            self.end_cell = (row, col)
            self.grid[row][col] = 0
            self.refresh_grid()
            self.status_var.set(f"End set at ({row}, {col})")
        elif self.mode == "wall":
            if (row, col) != self.start_cell and (row, col) != self.end_cell:
                self.grid[row][col] = 1 - self.grid[row][col]
                self.refresh_grid()

    def on_drag(self, event):
        if self.running or self.mode != "wall":
            return
        cell = self.get_cell(event)
        if not cell:
            return
        row, col = cell
        if (row, col) != self.start_cell and (row, col) != self.end_cell:
            self.grid[row][col] = 1
            self.draw_cell(row, col, COLOR_WALL)

    def set_mode(self, new_mode):
        self.mode = new_mode
        labels = {"wall": "Draw Walls", "start": "Place Start", "end": "Place End"}
        for mode_name, button in self.mode_buttons.items():
            button.config(
                bg="#e94560" if mode_name == new_mode else "#16213e",
                relief="sunken" if mode_name == new_mode else "raised",
            )
        self.status_var.set(f"Mode: {labels[new_mode]} - click or drag on the grid")

    def clear_all(self):
        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.start_cell = None
        self.end_cell = None
        self.refresh_grid()
        self.status_var.set("Grid cleared. Place a Start and End, then draw walls.")

    def run(self):
        self.root.mainloop()