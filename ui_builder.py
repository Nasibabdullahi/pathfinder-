import tkinter as tk

from settings import (
    COLOR_BG,
    COLOR_END_FILL,
    COLOR_PATH,
    COLOR_START_FILL,
    COLOR_VISITED,
    COLOR_WALL,
)


def build_ui(app):
    toolbar = tk.Frame(app.root, bg=COLOR_BG, pady=8)
    toolbar.pack(fill="x")

    tk.Label(
        toolbar,
        text="PATHFINDING VISUALIZER",
        font=("Courier", 13, "bold"),
        fg="#00b4d8",
        bg=COLOR_BG,
    ).pack(side="left", padx=14)

    app.mode_buttons = {}
    for mode_name, label in [("start", "Start"), ("end", "End"), ("wall", "Wall")]:
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
            padx=10,
            pady=4,
            command=lambda mode_name=mode_name: app.set_mode(mode_name),
        )
        button.pack(side="left", padx=4)
        app.mode_buttons[mode_name] = button

    app.btn_run = tk.Button(
        toolbar,
        text="RUN BFS",
        font=("Courier", 10, "bold"),
        fg="white",
        bg="#533483",
        relief="flat",
        padx=12,
        pady=4,
        command=app.bfs,
    )
    app.btn_run.pack(side="left", padx=8)

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
    app.btn_clear.pack(side="left", padx=4)

    app.canvas = tk.Canvas(
        app.root,
        width=app.canvas_w,
        height=app.canvas_h,
        bg=COLOR_BG,
        highlightthickness=0,
    )
    app.canvas.pack()
    app.canvas.bind("<Button-1>", app.on_click)
    app.canvas.bind("<B1-Motion>", app.on_drag)

    app.status_var = tk.StringVar(value="Welcome! Pick a mode above, then click the grid.")
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

    legend = tk.Frame(app.root, bg=COLOR_BG, pady=4)
    legend.pack()
    for color, label in [
        (COLOR_START_FILL, "Start"),
        (COLOR_END_FILL, "End"),
        (COLOR_WALL, "Wall"),
        (COLOR_VISITED, "Visited"),
        (COLOR_PATH, "Shortest Path"),
    ]:
        tk.Label(legend, text="■", fg=color, bg=COLOR_BG, font=("Courier", 12)).pack(
            side="left", padx=2
        )
        tk.Label(
            legend,
            text=label,
            fg="#aaaacc",
            bg=COLOR_BG,
            font=("Courier", 9),
        ).pack(side="left", padx=(0, 10))