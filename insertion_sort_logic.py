def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        yield i, j, False 
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1    
            yield j + 1, j, True 
            
        arr[j + 1] = key
        
        yield j + 1, i, True