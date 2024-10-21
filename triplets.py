def triplets(a, b, c):

    #Sort each and convert into set to remove duplicates
    a, b, c = (sorted(set(a)), sorted(set(b)), sorted(set(c)))
    
    # counter for distinct triplets
    distinct = 0
    
    # b is the integer array with the most constraints
    for elt in b:
        # where to insert elt (b) in sorted a
        index1 = bisect.bisect(a, elt)
        # where to insert elt (b) in sorted c
        index2 = bisect.bisect(c, elt)
        distinct += index1 * index2
    
    return distinct
