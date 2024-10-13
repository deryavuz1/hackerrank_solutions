def reverseArray(a):
    
    alen = len(a)
    new_arr = [0] * alen
    
    for index, elt in enumerate(a):
        rev_index = alen - index -1
        new_arr[rev_index] = elt
        
    return new_arr
        
