def decodeHuff(root, s):
    current = root
    decoded = ""
    
    for c in s:
        if int(c) == 1:
            current = current.right
        elif int(c) == 0:
            current = current.left
            
        if current.left == None and current.right == None:
            decoded += current.data
            current = root
        
              
    print(decoded)
