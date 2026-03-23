import tkinter as tk
from tkinter import simpledialog
import math

from tree_node import TreeNode
from tree_traversal_logic import (
    generate_random_tree,
    run_traversal,
)
from ui_builder_tree import build_ui
from settings import (
    COLOR_BG,
    ANIMATION_DELAY,
)

# Tree configs
TREE_CANVAS_W = 900
TREE_CANVAS_H = 600
TREE_NODE_SIZE = 20  # radius
TREE_FONT = ("Courier", 14, "bold")
TREE_LINE_WIDTH = 3

class TreeVisualizer:
    def __init__(self):
        self.root_node = None
        self.selected_node = None
        self.mode = "random"
        self.running = False
        self.node_positions = {}
        self.canvas_w = TREE_CANVAS_W
        self.canvas_h = TREE_CANVAS_H

        self.root = tk.Tk()
        self.root.title("Tree Traversal Visualizer")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        self.traversal_buttons = {}

        build_ui(self)
        self.set_mode("random")


    def calc_positions(self, root):
        """Calculate x,y for each node using level spacing."""


        if not root:
            return {}
        level_size = [1]
        queue = [(root, 0, 0.5)]  # node, level, hfrac
        positions = {}
        while queue:
            node, level, hfrac = queue.pop(0)
            x = 900 * hfrac
            y = 80 + level * 100
            positions[node] = (x, y)
            hfrac_left = hfrac - (0.25 / (2 ** level))
            hfrac_right = hfrac + (0.25 / (2 ** level))
            if node.left:
                queue.append((node.left, level+1, hfrac_left))
            if node.right:
                queue.append((node.right, level+1, hfrac_right))
        return positions

    def draw_tree(self):
        self.canvas.delete("all")
        if not self.root_node:
            return
        self.node_positions = self.calc_positions(self.root_node)
        for node, (x, y) in self.node_positions.items():
            # Draw lines to children
            if node.left:
                lx, ly = self.node_positions[node.left]
                self.canvas.create_line(x, y+20, lx, ly-20, width=TREE_LINE_WIDTH, fill="#533483")
            if node.right:
                rx, ry = self.node_positions[node.right]
                self.canvas.create_line(x, y+20, rx, ry-20, width=TREE_LINE_WIDTH, fill="#533483")
            # Draw node circle
            self.canvas.create_oval(x-TREE_NODE_SIZE, y-TREE_NODE_SIZE, 
                                  x+TREE_NODE_SIZE, y+TREE_NODE_SIZE,
                                  fill="#4cc9f0", outline="white", width=2)
            # Draw value
            self.canvas.create_text(x, y, text=str(node.val), font=TREE_FONT, fill="white")

    def highlight_node(self, node, color):
        if node not in self.node_positions:
            return
        x, y = self.node_positions[node]
        self.canvas.create_oval(x-TREE_NODE_SIZE, y-TREE_NODE_SIZE, 
                              x+TREE_NODE_SIZE, y+TREE_NODE_SIZE,
                              fill=color, outline="white", width=3, tags="highlight")
        # Redraw text on top
        self.canvas.create_text(x, y, text=str(node.val), font=TREE_FONT, fill="white", tags="text")

    def set_mode(self, new_mode):
        self.mode = new_mode
        labels = {
            "random": "Random Tree", "select": "Select Node",
            "left": "Add Left", "right": "Add Right", "value": "Set Value"
        }
        for mode_name, button in self.mode_buttons.items():
            button.config(
                bg="#e94560" if mode_name == new_mode else "#16213e",
                relief="sunken" if mode_name == new_mode else "raised",
            )
        self.status_var.set(f"Mode: {labels[new_mode]} - click on nodes/canvas.")

    def on_click(self, event):
        if self.running:
            return
        x, y = event.x, event.y
        clicked_node = self.get_node_at(x, y)
        if self.mode == "random":
            self.root_node = generate_random_tree()
            self.draw_tree()
            self.status_var.set("Random tree generated! Select traversal type and RUN.")
        elif self.mode == "select":
            self.selected_node = clicked_node
            color = "#ffff00" if clicked_node else "#ff0000"
            self.status_var.set(f"Selected: {clicked_node.val if clicked_node else 'None'}")
        elif clicked_node and self.selected_node == clicked_node:
            if self.mode == "left":
                if not clicked_node.left:
                    clicked_node.left = TreeNode(0)
                    self.draw_tree()
                    self.status_var.set("Left child added.")
            elif self.mode == "right":
                if not clicked_node.right:
                    clicked_node.right = TreeNode(0)
                    self.draw_tree()
                    self.status_var.set("Right child added.")
            elif self.mode == "value":
                new_val = simpledialog.askinteger("Set Value", "Enter value (1-99):", minvalue=1, maxvalue=99)
                if new_val is not None:
                    clicked_node.val = new_val
                    self.draw_tree()
                    self.status_var.set(f"Value set to {new_val}")
        else:
            self.status_var.set("First select a node (mode: select), then add/edit.")

    def get_node_at(self, x, y):
        for node, (nx, ny) in self.node_positions.items():
            dist = math.sqrt((x - nx)**2 + (y - ny)**2)
            if dist <= TREE_NODE_SIZE:
                return node
        return None

    def run_traversal(self, trav_type):
        run_traversal(self, trav_type)

    def clear_all(self):
        self.root_node = None
        self.selected_node = None
        self.canvas.delete("all")
        self.status_var.set("Cleared. Click 'Random Tree' or build manually.")
        self.set_mode("random")

    def run(self):
        self.root.mainloop()

