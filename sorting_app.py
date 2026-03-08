import random
import tkinter as tk

from bubble_sort_logic import run_bubble_sort
from settings import (
    COLOR_BG,
    COLOR_GRID_LINE,
    COLOR_SORT_BAR,
    SORT_BAR_COUNT,
    SORT_CANVAS_H,
    SORT_CANVAS_W,
    SORT_MAX_VALUE,
    SORT_MIN_VALUE,
)
from ui_builder_sorting import build_sorting_ui


class SortingVisualizer:
    def __init__(self):
        self.values = []
        self.running = False

        self.root = tk.Tk()
        self.root.title("DSA Visualizer - Bubble Sort")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        self.canvas_w = SORT_CANVAS_W
        self.canvas_h = SORT_CANVAS_H

        build_sorting_ui(self)
        self.generate_values()

    def generate_values(self):
        if self.running:
            return
        self.values = [random.randint(SORT_MIN_VALUE, SORT_MAX_VALUE) for _ in range(SORT_BAR_COUNT)]
        self.draw_bars()
        self.status_var.set("New array generated. Click RUN BUBBLE SORT.")

    def draw_bars(self, highlight=None, sorted_start=None, sorted_color=None):
        highlight = highlight or {}
        self.canvas.delete("all")

        if not self.values:
            return

        bar_width = self.canvas_w / len(self.values)
        max_value = max(self.values)
        scale = (self.canvas_h - 20) / max_value if max_value else 1

        for index, value in enumerate(self.values):
            x1 = index * bar_width
            x2 = x1 + bar_width - 1
            y2 = self.canvas_h
            y1 = y2 - (value * scale)

            color = COLOR_SORT_BAR
            if sorted_start is not None and index >= sorted_start:
                color = sorted_color or color
            if index in highlight:
                color = highlight[index]

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=COLOR_GRID_LINE)

    def bubble_sort(self):
        run_bubble_sort(self)

    def run(self):
        self.root.mainloop()