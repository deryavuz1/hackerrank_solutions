
def miniMaxSum(arr):
    
    minSum = 0
    maxSum = 0
    
    for index, elt in enumerate(sorted(arr)):
        
        if index < 4:
            minSum += elt
        
        if index >= 1 and index <= 4:
            maxSum += elt
            
    print(str(minSum) + " " + str(maxSum))

