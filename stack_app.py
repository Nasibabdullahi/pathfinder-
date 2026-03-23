import tkinter as tk
import random
from stack_logic import stack
from stack_UI import build_stack_ui
from settings import COLOR_BG

class StackApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Visualizer - Stack")
        self.root.configure(bg=COLOR_BG)
        
        self.canvas_w = 800
        self.canvas_h = 500
        self.stack_logic = stack()
        
        build_stack_ui(self)
        
    def draw_stack(self):
        self.canvas.delete("all")
        x_center = self.canvas_w // 2
        y_bottom = self.canvas_h - 50
        box_h = 40
        box_w = 120
        
        items = self.stack_logic.items
        for i, val in enumerate(items):
            y = y_bottom - (i * (box_h + 5))
            self.canvas.create_rectangle(
                x_center - box_w//2, y - box_h, 
                x_center + box_w//2, y, 
                fill="#e94560", outline="white"
            )
            self.canvas.create_text(x_center, y - box_h//2, text=str(val), fill="white", font=("Courier", 10, "bold"))

    def push_item(self):
        val = random.randint(10, 99)
        self.stack_logic.push(val)
        self.status_var.set(f"Pushed {val} onto the stack.")
        self.draw_stack()

    def pop_item(self):
        val = self.stack_logic.pop()
        self.status_var.set(f"Popped {val} from the stack.")
        self.draw_stack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = StackApp()
    app.run()