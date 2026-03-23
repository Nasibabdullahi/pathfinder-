# At the top of sorting_app.py
from merge_sorting import run_merge_sort 

# Inside the SortingVisualizer class
class SortingVisualizer:
    # ... existing __init__ ...

    def merge_sort(self):
        """Trigger the merge sort visualization"""
        run_merge_sort(self)
from sorting_app import SortingVisualizer


def main():
    app = SortingVisualizer()
    app.run()


if __name__ == "__main__":
    main()