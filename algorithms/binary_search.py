def binary_search(arr, target, visualize):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        visualize.check_mid(mid)

        if arr[mid] == target:
            visualize.found(mid)
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        visualize.show_range(low, high)

    return -1