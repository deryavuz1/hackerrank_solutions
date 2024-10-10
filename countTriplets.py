#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    count = 0
    # track both potential pairs and triplets
    # Counter creates a dict inherently
    pairs = Counter()
    triplets = Counter()
    
    for elt in arr:
        if elt in triplets:
            # if elt in triplets, we have found triplets, add count
            count += triplets[elt]
        if elt in pairs:
            # elt has potential triplets waiting to be found
            # add to the 3rd value's count the number of existing pairs
            triplets[elt*r] += pairs[elt]
        # no pairs or triplets exist in first iter. 
        pairs[elt*r] += 1
    
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
