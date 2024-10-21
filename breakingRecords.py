def breakingRecords(scores):
    
    toReturn = [0] * 2
    
    maxCount = 0
    minCount = 0
    
    # just to initialize it to the head
    max_points = scores[0]
    min_points = scores[0]
    
    for c in range(len(scores)):
        if scores[c] > max_points:
            max_points = scores[c]
            maxCount += 1
        elif scores[c] < min_points:
            min_points = scores[c]
            minCount += 1
        
    return [maxCount, minCount]
    
