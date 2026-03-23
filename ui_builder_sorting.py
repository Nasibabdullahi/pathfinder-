import tkinter as tk
from settings import COLOR_BG

def build_sorting_ui(app):
    toolbar = tk.Frame(app.root, bg=COLOR_BG, pady=8)
    toolbar.pack(fill="x")

    tk.Label(toolbar, text="DSA VISUALIZER", font=("Courier", 13, "bold"), 
             fg="#00b4d8", bg=COLOR_BG).pack(side="left", padx=14)

    # Generate Button
    app.btn_generate = tk.Button(toolbar, text="GENERATE", font=("Courier", 10, "bold"),
                                 fg="white", bg="#0f3460", relief="flat", padx=12,
                                 command=app.generate_values)
    app.btn_generate.pack(side="left", padx=6)

    # Bubble Button
    app.btn_sort = tk.Button(toolbar, text="BUBBLE", font=("Courier", 10, "bold"),
                             fg="white", bg="#533483", relief="flat", padx=12,
                             command=app.bubble_sort)
    app.btn_sort.pack(side="left", padx=6)

    # Merge Button
    app.btn_merge_sort = tk.Button(toolbar, text="MERGE", font=("Courier", 10, "bold"),
                                   fg="white", bg="#e94560", relief="flat", padx=12,
                                   command=app.merge_sort)
    app.btn_merge_sort.pack(side="left", padx=6)

    # Quick Button
    app.btn_quick_sort = tk.Button(toolbar, text="QUICK", font=("Courier", 10, "bold"),
                                   fg="white", bg="#4e9f3d", relief="flat", padx=12,
                                   command=app.quick_sort)
    app.btn_quick_sort.pack(side="left", padx=6)

    app.canvas = tk.Canvas(app.root, width=app.canvas_w, height=app.canvas_h, 
                           bg=COLOR_BG, highlightthickness=0)
    app.canvas.pack()

    app.status_var = tk.StringVar(value="Select a sort.")
    tk.Label(app.root, textvariable=app.status_var, font=("Courier", 9),
             fg="#aaaacc", bg=COLOR_BG, anchor="w", padx=14, pady=6).pack(fill="x")