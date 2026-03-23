import tkinter as tk
from settings import COLOR_BG

def build_selection_ui(app):
    toolbar = tk.Frame(app.root, bg=COLOR_BG, pady=8)
    toolbar.pack(fill="x")

    tk.Label(
        toolbar,
        text="SELECTION SORT VISUALIZER",
        font=("Courier", 13, "bold"),
        fg="#00b4d8",
        bg=COLOR_BG,
    ).pack(side="left", padx=14)

    app.btn_generate = tk.Button(
        toolbar,
        text="NEW ARRAY",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#16213e",
        relief="flat",
        padx=12,
        pady=4,
        command=app.generate_array,
    )
    app.btn_generate.pack(side="left", padx=6)

    app.btn_sort = tk.Button(
        toolbar,
        text="RUN SELECTION SORT",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#533483",
        relief="flat",
        padx=12,
        pady=4,
        command=app.run_sort,
    )
    app.btn_sort.pack(side="left", padx=6)

    app.canvas = tk.Canvas(
        app.root,
        width=app.canvas_w,
        height=app.canvas_h,
        bg=COLOR_BG,
        highlightthickness=0,
    )
    app.canvas.pack()