import tkinter as tk
from settings import COLOR_BG

def build_stack_ui(app):
    toolbar = tk.Frame(app.root, bg=COLOR_BG, pady=8)
    toolbar.pack(fill="x")

    tk.Label(
        toolbar,
        text="STACK VISUALIZER",
        font=("Courier", 13, "bold"),
        fg="#00b4d8",
        bg=COLOR_BG,
    ).pack(side="left", padx=14)

    app.btn_push = tk.Button(
        toolbar,
        text="PUSH",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#16213e",
        activebackground="#00b4d8",
        relief="flat",
        padx=12,
        pady=4,
        command=app.push_item,
    )
    app.btn_push.pack(side="left", padx=6)

    app.btn_pop = tk.Button(
        toolbar,
        text="POP",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#533483",
        relief="flat",
        padx=12,
        pady=4,
        command=app.pop_item,
    )
    app.btn_pop.pack(side="left", padx=6)

    app.canvas = tk.Canvas(
        app.root,
        width=app.canvas_w,
        height=app.canvas_h,
        bg=COLOR_BG,
        highlightthickness=0,
    )
    app.canvas.pack()

    app.status_var = tk.StringVar(value="Push an item onto the stack.")
    tk.Label(
        app.root,
        textvariable=app.status_var,
        font=("Courier", 9),
        fg="#aaaacc",
        bg=COLOR_BG,
        anchor="w",
        padx=14,
        pady=6,
    ).pack(fill="x")