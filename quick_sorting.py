import time
from settings import COLOR_SORT_COMPARE, COLOR_SORT_DONE, COLOR_SORT_SWAP, SORT_DELAY

def run_quick_sort(app):
    if app.running:
        return

    app.running = True
    app.btn_sort.config(state="disabled")
    app.btn_merge_sort.config(state="disabled")
    app.btn_generate.config(state="disabled")
    app.status_var.set("Quick Sort is running...")
    
    values = app.values
    _quick_sort_recursive(app, values, 0, len(values) - 1)

    app.draw_bars(sorted_start=0, sorted_color=COLOR_SORT_DONE)
    app.status_var.set("Quick Sort complete.")
    app.running = False
    app.btn_sort.config(state="normal")
    app.btn_merge_sort.config(state="normal")
    app.btn_generate.config(state="normal")

def _quick_sort_recursive(app, data, low, high):
    if low < high:
        pivot_index = _partition(app, data, low, high)
        _quick_sort_recursive(app, data, low, pivot_index - 1)
        _quick_sort_recursive(app, data, pivot_index + 1, high)

def _partition(app, data, low, high):
    pivot = data[high]
    i = low - 1
    
    # Highlight the pivot
    app.draw_bars(highlight={high: "purple"}) 
    
    for j in range(low, high):
        app.draw_bars(highlight={j: COLOR_SORT_COMPARE, high: "purple"})
        app.root.update()
        time.sleep(SORT_DELAY)

        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            app.draw_bars(highlight={i: COLOR_SORT_SWAP, j: COLOR_SORT_SWAP})
            app.root.update()
            time.sleep(SORT_DELAY)

    data[i + 1], data[high] = data[high], data[i + 1]
    app.draw_bars(highlight={i + 1: COLOR_SORT_DONE})
    app.root.update()
    time.sleep(SORT_DELAY)
    
    return i + 1