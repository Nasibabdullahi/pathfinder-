import time

from settings import COLOR_SORT_COMPARE, COLOR_SORT_DONE, COLOR_SORT_SWAP, SORT_DELAY


def run_heap_sort(app):
    if app.running:
        return

    app.running = True
    app.btn_sort.config(state="disabled")
    app.btn_generate.config(state="disabled")
    app.status_var.set("Heap Sort running...")
    app.root.update()

    values = app.values[:]
    n = len(values)

    
    for i in range(n // 2 - 1, -1, -1):
        _heapify(app, values, n, i)

    # Extract max
    for i in range(n - 1, 0, -1):
        values[0], values[i] = values[i], values[0]
        app.draw_bars(highlight={0: COLOR_SORT_SWAP, i: COLOR_SORT_SWAP})
        app.root.update()
        time.sleep(SORT_DELAY)
        _heapify(app, values, i, 0)
        app.draw_bars(sorted_start=i, sorted_color=COLOR_SORT_DONE)
        app.root.update()

    app.status_var.set("Heap Sort complete!")
    app.values[:] = values
    app.draw_bars(sorted_start=0, sorted_color=COLOR_SORT_DONE)
    app.running = False
    app.btn_sort.config(state="normal")
    app.btn_generate.config(state="normal")


def _heapify(app, values, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    app.draw_bars(highlight={i: COLOR_SORT_COMPARE, left: COLOR_SORT_COMPARE if left < n else None, right: COLOR_SORT_COMPARE if right < n else None})
    app.root.update()
    time.sleep(SORT_DELAY)

    if left < n and values[left] > values[largest]:
        largest = left

    if right < n and values[right] > values[largest]:
        largest = right

    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        app.draw_bars(highlight={i: COLOR_SORT_SWAP, largest: COLOR_SORT_SWAP})
        app.root.update()
        time.sleep(SORT_DELAY)
        _heapify(app, values, n, largest)
