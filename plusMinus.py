
def plusMinus(arr):
    
    plus_count = 0
    neg_count = 0
    zero_count = 0
    
    for elt in arr:
        if elt < 0:
            neg_count += 1
        elif elt > 0:
            plus_count += 1
        else:
            zero_count += 1
        
    print("{:.6f}".format(plus_count/len(arr)))
    print("{:.6f}".format(neg_count/len(arr)))
    print("{:.6f}".format(zero_count/len(arr)))
