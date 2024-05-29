def selection_sort(arr):
    n = len(arr)
    for i in range(n): 
        min_idx = i
        for j in range(i + 1, n):  
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr




def fibonacci_search(arr, x):
    n = len(arr)
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1
    offset = -1

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    i = n - 1  
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and i == n - 1 and arr[i] == x:
        return i

    return -1

print(fibonacci_search([1,3,4,5,7,10], 6))