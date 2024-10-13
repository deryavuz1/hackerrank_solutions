def encryption(s):
    
    no_space = s.replace(" ", "")
    char_arr = list(no_space)
    char_count = len(char_arr)
    sq = math.sqrt(char_count)
    rows = math.floor(sq)
    cols = math.ceil(sq)
    
    list1 = []
   
    for i in range(rows):
        if i == rows-1:
            list1.append(no_space[i*cols:])
        else:
            list1.append(no_space[i * cols: (i +1)*cols])
    r = ""
    for i in range(len(list1)):
        for x in list1:
            r += x[i]
        r += " "
        
    return r
        
    
        
