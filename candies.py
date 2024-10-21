def candies(n, arr):
    
    #solutions array
    cache = [1 for x in range(n)]
    # set the initial value of candy given to 1, we do not know rest of the array yet
    
    # Left to right first pass in the array
    for i in range(1, n, 1):
        if arr[i] > arr[i -1]:
            cache[i] = cache[i - 1] + 1

    # Right to left pass, we now verify if we have minimized
    for i in range(n - 1, 0, -1):
        # current child's score is greater than the next child
        # give more candy
        if arr[i-1] > arr[i] and cache[i-1] <= cache[i]:
            cache[i-1] = cache[i] + 1

    return sum(cache)
