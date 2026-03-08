import time
from collections import deque

from settings import ANIMATION_DELAY, COLOR_PATH, COLOR_VISITED, COLS, ROWS


def run_bfs(app):
    if not app.start_cell or not app.end_cell:
        app.status_var.set("Please set both a Start and End point first.")
        return

    app.running = True
    app.btn_run.config(state="disabled")
    app.btn_clear.config(state="disabled")
    app.status_var.set("BFS is searching...")
    app.root.update()

    queue = deque([app.start_cell])
    visited = {app.start_cell: None}
    found = False

    while queue:
        current = queue.popleft()
        row, col = current

        if current != app.start_cell and current != app.end_cell:
            app.draw_cell(row, col, COLOR_VISITED)
            app.root.update()
            time.sleep(ANIMATION_DELAY)

        if current == app.end_cell:
            found = True
            break

        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nrow, ncol = row + drow, col + dcol
            neighbor = (nrow, ncol)
            if 0 <= nrow < ROWS and 0 <= ncol < COLS:
                if neighbor not in visited and app.grid[nrow][ncol] == 0:
                    visited[neighbor] = current
                    queue.append(neighbor)

    if found:
        _animate_path(app, visited)
    else:
        app.status_var.set("No path found - end is completely blocked by walls.")

    app.running = False
    app.btn_run.config(state="normal")
    app.btn_clear.config(state="normal")


def _animate_path(app, visited):
    path = []
    node = app.end_cell

    while node is not None:
        path.append(node)
        node = visited[node]

    path.reverse()

    for step in path:
        if step != app.start_cell and step != app.end_cell:
            row, col = step
            app.draw_cell(row, col, COLOR_PATH)
            app.root.update()
            time.sleep(ANIMATION_DELAY * 2)

    app.status_var.set(f"Path found! {len(path) - 1} steps. Press CLEAR to reset.")