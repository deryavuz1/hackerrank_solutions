def maxSubsetSum(arr):
    
    # solutions array to store the max at each index calculation
    cache = [0] * len(arr)
    
    # Initialize cache[0] as the first element of the array (or 0) if it is negative
    cache[0] = max(arr[0], 0)
    
    # Stop and return cache[0] if the length of the array is 1, it's already max
    if len(arr) == 1:
        return cache[0]
    
    # Initialize cache[1] as the max of the first element, second element (or 0)
    # We initialize both 0 and 1 since our for loop starts from index 2 - we need 2 back items max
    cache[1] = max(cache[0], arr[1])
    
    # Set cache[1] to the maximum of the previous solution or 2 indices back due to the above explanation
    # covers the case were indices are odd + even jumps
    for i in range(2, len(arr)):
        cache[i] = max(cache[i - 2] + arr[i], cache[i - 1])
        
    # Returning the solution
    return cache[-1]
        
