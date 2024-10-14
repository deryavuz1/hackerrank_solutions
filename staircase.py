def staircase(n):
    
    for i in range(1, n+1):
        toPrint = "#"*i
        print(toPrint.rjust(n))
