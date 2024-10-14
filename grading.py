
def gradingStudents(grades):
    
    count = len(grades)
    rounded = [0] * count
    
    for i, g in enumerate(grades):
        
        if g < 38:
            rounded[i] = g
        elif g % 5 >= 3:
            toAdd = g + (5-g%5)
            rounded[i] = toAdd
        else:
            rounded[i] = g
        
    
    return rounded
