#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    num = arr[-1]
    for itr in reversed(range(n - 1)):
        if (num < arr[itr]):
            if (itr == 0):
                arr[itr + 1] = arr[itr]
                for i in range(n):
                    print(arr[i], end=' ' if i != n - 1 else '\n')
                arr[itr] = num
            else:
                arr[itr + 1] = arr[itr]
            
        else:
            arr[itr + 1] = num
            for i in range(n):
                print(arr[i], end=' ' if i != n - 1 else '\n')
            break
        for i in range(n):
                print(arr[i], end=' ' if i != n - 1 else '\n')
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
