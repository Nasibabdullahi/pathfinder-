import time

from settings import COLOR_SORT_COMPARE, COLOR_SORT_DONE, COLOR_SORT_SWAP, SORT_DELAY


def run_bubble_sort(app):
    if app.running:
        return

    app.running = True
    app.btn_sort.config(state="disabled")
    app.btn_generate.config(state="disabled")
    app.status_var.set("Bubble Sort is running...")
    app.root.update()

    values = app.values
    n = len(values)

    for outer in range(n):
        swapped = False

        for inner in range(0, n - outer - 1):
            app.draw_bars(highlight={inner: COLOR_SORT_COMPARE, inner + 1: COLOR_SORT_COMPARE})
            app.root.update()
            time.sleep(SORT_DELAY)

            if values[inner] > values[inner + 1]:
                values[inner], values[inner + 1] = values[inner + 1], values[inner]
                swapped = True
                app.draw_bars(highlight={inner: COLOR_SORT_SWAP, inner + 1: COLOR_SORT_SWAP})
                app.root.update()
                time.sleep(SORT_DELAY)

        app.draw_bars(sorted_start=n - outer - 1, sorted_color=COLOR_SORT_DONE)
        app.root.update()

        if not swapped:
            app.draw_bars(sorted_start=0, sorted_color=COLOR_SORT_DONE)
            app.status_var.set("Already sorted. Bubble Sort finished.")
            app.running = False
            app.btn_sort.config(state="normal")
            app.btn_generate.config(state="normal")
            return

    app.status_var.set("Bubble Sort complete.")
    app.running = False
    app.btn_sort.config(state="normal")
    app.btn_generate.config(state="normal")

