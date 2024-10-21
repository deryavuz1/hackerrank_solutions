#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):

    median_elt = 0
    num_notices = 0
    median_length = d
    median_array = sorted(expenditure[0:d])
    
    for index in range(d, len(expenditure)):
        if median_length % 2 == 1:
            # odd length, take middle
            median_elt = median_array[median_length // 2]
        elif median_length % 2 == 0:
            median_elt = (median_array[(median_length // 2)] + median_array[(median_length // 2) - 1]) / 2
        if expenditure[index] >= median_elt * 2:
            num_notices+=1
        

        to_remove = expenditure[index-d]
        bisect_index = bisect.bisect_left(median_array, to_remove)
        del median_array[bisect_index]
        to_add = expenditure[index]
        bisect.insort_left(median_array, to_add)
        
    return num_notices
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
