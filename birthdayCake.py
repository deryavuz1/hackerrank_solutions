
def birthdayCakeCandles(candles):
    
    length = len(candles)
    sorted_arr = sorted(candles)
    tallest_count = 0
    tallest = sorted_arr[length-1]
    
    
    for i in reversed(sorted_arr):
        if i == tallest:
            tallest_count += 1
    
    return tallest_count
        
        
