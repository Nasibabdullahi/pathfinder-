import tkinter as tk
import random
from queue_logic import Queue
from queue_ui import build_queue_ui
from settings import COLOR_BG, COLOR_SORT_BAR, COLOR_PATH

class QueueApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DSA Visualizer - Queue")
        self.root.configure(bg=COLOR_BG)
        
        self.canvas_w = 800
        self.canvas_h = 500
        self.queue_logic = Queue()
        
        build_queue_ui(self)
        
    def draw_queue(self):
        self.canvas.delete("all")
        # Horizontal layout: Items enter from right, leave from left
        x_start = 100 
        y_center = self.canvas_h // 2
        box_w = 80
        box_h = 60
        
        items = list(self.queue_logic.items)
        for i, val in enumerate(items):
            x = x_start + (i * (box_w + 10))
            
            # Color the front of the line differently (The "Next" item)
            color = COLOR_PATH if i == 0 else COLOR_SORT_BAR
            
            self.canvas.create_rectangle(
                x, y_center - box_h//2, 
                x + box_w, y_center + box_h//2, 
                fill=color, outline="white", width=2
            )
            self.canvas.create_text(
                x + box_w//2, y_center, 
                text=str(val), fill="white", font=("Courier", 12, "bold")
            )

    def add_to_queue(self):
        val = random.randint(10, 99)
        self.queue_logic.enqueue(val)
        self.status_var.set(f"Enqueued {val}. (Added to the back)")
        self.draw_stack = self.draw_queue() # Draw the update

    def remove_from_queue(self):
        val = self.queue_logic.dequeue()
        if val == "Queue is Empty":
            self.status_var.set(val)
        else:
            self.status_var.set(f"Dequeued {val}. (Removed from the front)")
        self.draw_queue()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QueueApp()
    app.run()