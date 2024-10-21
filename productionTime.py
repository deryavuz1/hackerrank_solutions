#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    low, high = 1, max(machines) * goal
    while low < high:
        mid = (low + high) // 2
        total_items = sum(mid // machine for machine in machines)
        if total_items >= goal:
            high = mid  # Can we do it in fewer days?
        else:
            low = mid + 1  # We need more days
    return low
    
   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
