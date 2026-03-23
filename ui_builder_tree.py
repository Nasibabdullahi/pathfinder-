import tkinter as tk

from settings import (
    COLOR_BG,
)

def build_ui(app):
    toolbar = tk.Frame(app.root, bg=COLOR_BG, pady=8)
    toolbar.pack(fill="x")

    tk.Label(
        toolbar,
        text="TREE TRAVERSAL VISUALIZER",
        font=("Courier", 13, "bold"),
        fg="#00b4d8",
        bg=COLOR_BG,
    ).pack(side="left", padx=14)

    # Mode buttons
    app.mode_buttons = {}
    for mode_name, label in [
        ("random", "Random Tree"), 
        ("select", "Select Node"),
        ("left", "Add Left"), 
        ("right", "Add Right"),
        ("value", "Set Value")
    ]:
        button = tk.Button(
            toolbar,
            text=label,
            font=("Courier", 10, "bold"),
            fg="white",
            bg="#16213e",
            activebackground="#e94560",
            activeforeground="white",
            relief="raised",
            bd=0,
            padx=8,
            pady=4,
            command=lambda m=mode_name: app.set_mode(m),
        )
        button.pack(side="left", padx=2)
        app.mode_buttons[mode_name] = button

    # Traversal buttons
    tk.Label(toolbar, text=" | Run: ", font=("Courier", 10), fg="#aaaacc", bg=COLOR_BG).pack(side="left", padx=10)
    for trav, label in [("preorder", "Pre"), ("inorder", "In"), ("postorder", "Post"), ("levelorder", "Level")]:
        button = tk.Button(
            toolbar,
            text=label,
            font=("Courier", 10, "bold"),
            fg="white",
            bg="#533483",
            relief="flat",
            padx=8,
            pady=4,
            command=lambda t=trav: app.run_traversal(t),
        )
        button.pack(side="left", padx=2)
        # No need for dict, direct command to app.run_traversal

    app.btn_clear = tk.Button(
        toolbar,
        text="CLEAR",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#333355",
        relief="flat",
        padx=12,
        pady=4,
        command=app.clear_all,
    )
    app.btn_clear.pack(side="right", padx=14)

    app.canvas = tk.Canvas(
        app.root,
        width=900,
        height=600,
        bg=COLOR_BG,
        highlightthickness=0,
    )
    app.canvas.pack(pady=10)
    app.canvas.bind("<Button-1>", app.on_click)

    app.status_var = tk.StringVar(value="Click 'Random Tree' to start, or build manually. Then select traversal and RUN.")
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

    # Legend
    legend = tk.Frame(app.root, bg=COLOR_BG, pady=4)
    legend.pack()
    legend_labels = [
        ("#4cc9f0", "Node"),
        ("#f72585", "Visit Highlight"),
        ("#00b4d8", "Preorder"),
        ("#90be6d", "Inorder"),
        ("#f8961e", "Postorder"),
        ("#f5a623", "Level-order"),
    ]
    for color, label in legend_labels:
        tk.Label(legend, text="●", fg=color, bg=COLOR_BG, font=("Courier", 14)).pack(side="left", padx=4)
        tk.Label(legend, text=label, fg="#aaaacc", bg=COLOR_BG, font=("Courier", 9)).pack(side="left", padx=(0, 20))

