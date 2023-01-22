#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    countUp = 0
    countDown = 0
    countValley = 0
    above = False
    below = False
    for i in range(steps):
        if path[i] == 'U':
            countUp += 1
        elif path[i] == 'D':
            countDown += 1
        if countUp == countDown:
            above = False
            below = False
        elif countUp > countDown:
            above = True
            below = False
        else:
            if above == False and below == False:
                countValley += 1
            below = True
            above = False
    return countValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
