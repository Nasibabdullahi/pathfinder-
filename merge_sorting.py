import time
from settings import COLOR_SORT_COMPARE, COLOR_SORT_DONE, COLOR_SORT_SWAP, SORT_DELAY

def run_merge_sort(app):
    if app.running:
        return

    app.running = True
    app.btn_sort.config(state="disabled")
    app.btn_generate.config(state="disabled")
    app.status_var.set("Merge Sort is running...")
    app.root.update()

    values = app.values
    
    # Start the recursive process
    _merge_sort_recursive(app, values, 0, len(values) - 1)

    # Final UI Update
    app.draw_bars(sorted_start=0, sorted_color=COLOR_SORT_DONE)
    app.status_var.set("Merge Sort complete.")
    app.running = False
    app.btn_sort.config(state="normal")
    app.btn_generate.config(state="normal")

def _merge_sort_recursive(app, data, left, right):
    if left < right:
        mid = (left + right) // 2
        _merge_sort_recursive(app, data, left, mid)
        _merge_sort_recursive(app, data, mid + 1, right)
        _merge(app, data, left, mid, right)

def _merge(app, data, left, mid, right):
    # Highlight the range being merged
    app.draw_bars(highlight={i: COLOR_SORT_COMPARE for i in range(left, right + 1)})
    app.root.update()
    time.sleep(SORT_DELAY)

    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            data[k] = left_part[i]
            i += 1
        else:
            data[k] = right_part[j]
            j += 1
        
        # Visual feedback for the swap/overwrite
        app.draw_bars(highlight={k: COLOR_SORT_SWAP})
        app.root.update()
        time.sleep(SORT_DELAY)
        k += 1

    while i < len(left_part):
        data[k] = left_part[i]
        app.draw_bars(highlight={k: COLOR_SORT_SWAP})
        app.root.update()
        time.sleep(SORT_DELAY)
        i += 1
        k += 1

    while j < len(right_part):
        data[k] = right_part[j]
        app.draw_bars(highlight={k: COLOR_SORT_SWAP})
        app.root.update()
        time.sleep(SORT_DELAY)
        j += 1
        k += 1