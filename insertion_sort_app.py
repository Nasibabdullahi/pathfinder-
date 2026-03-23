import tkinter as tk
import random
import time
from insertion_sort_logic import insertion_sort
from selection_sort_ui import build_selection_ui
from settings import *

class InsertionSortApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Visualizer - Insertion Sort")
        self.root.configure(bg=COLOR_BG)

        self.canvas_w = SORT_CANVAS_W
        self.canvas_h = SORT_CANVAS_H
        self.data = []
        
        build_selection_ui(self)
        self.generate_array()

    def generate_array(self):
        self.data = [random.randint(SORT_MIN_VALUE, SORT_MAX_VALUE) for _ in range(SORT_BAR_COUNT)]
        self.draw_bars()

    def draw_bars(self, color_positions={}):
        self.canvas.delete("all")
        bar_width = self.canvas_w / len(self.data)
        for i, val in enumerate(self.data):
            x0, y0 = i * bar_width, self.canvas_h - (val * 4)
            x1, y1 = (i + 1) * bar_width, self.canvas_h
            color = color_positions.get(i, COLOR_SORT_BAR)
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=COLOR_GRID_LINE)

    def run_sort(self):
        for idx1, idx2, is_shift in insertion_sort(self.data):
            color = COLOR_SORT_SWAP if is_shift else COLOR_SORT_COMPARE
            self.draw_bars({idx1: color, idx2: color})
            self.root.update()
            time.sleep(SORT_DELAY)
        
        self.draw_bars({i: COLOR_SORT_DONE for i in range(len(self.data))})

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = InsertionSortApp()
    app.run()