def diagonalDifference(arr):
    
    leftDiag = 0
    rightDiag = 0
    length = len(arr)
  
    for i in range(len(arr)):
       leftDiag += arr[i][i]
       rightDiag += arr[i][length - 1 - i]
           
    return abs(leftDiag - rightDiag)
                
