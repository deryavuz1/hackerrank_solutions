def has_cycle(head):
    
    visited = []
    
    while n := head.next:
        if n in visited:
            return 1
        else:
            visited.append(n)
            head = n
    
    return 0
