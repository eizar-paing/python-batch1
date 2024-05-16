def quick_sort(arr):
    if len(arr) <= 1: # 7 
        return arr
    else:
        pivot = arr[0] # 3
        less_than_pivot = [x for x in arr[1:] if x <= pivot] # [1, 2, 1]
        greater_than_pivot = [x for x in arr[1:] if x > pivot] # [6, 8, 10]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot) # (1, 2, 1) + 3 + (6, 8, 10)

        # [1, 2, 1] [3] [6, 8, 10]
        # [1] [1] [2] [3] [6] [8, 10]
        # [1] [1] [2] [3] [6] [8] [10]
        # [1, 1, 2, 3, 6, 8, 10]


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)

# less than pivot 
# for x in arr(1: ) arr[1] to [6]
#   if x <= pivort