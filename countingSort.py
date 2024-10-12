def countingSort(arr):
    
    freqs = [0]*100
    toReturn = []
    for i in range(len(arr)):
        freqs[arr[i]] += 1
      
    
    for index, freq in enumerate(freqs):
        toReturn.extend([index] * freq)
        
    return toReturn
