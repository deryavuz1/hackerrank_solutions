
def lonelyinteger(a):
    
    dict = {}
    
    for i in a:
        dict[i] = 0
    
    for i in a:
        count = dict.get(i)
        dict[i] = count+1
        
    print(dict)
    
    for key in dict.keys():
        if dict.get(key) == 1:
            return key
