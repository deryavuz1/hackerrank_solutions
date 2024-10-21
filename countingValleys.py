def countingValleys(steps, path):
    count = 0
    valley = 0
    
    for s in path:
        if s == 'U':
            count+=1
            valley += int(count == 0)
        elif s == 'D':
            count-=1
            
    return valley
