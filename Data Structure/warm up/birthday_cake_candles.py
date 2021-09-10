#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def getHighestNo(candles):
    max = 0
    for i in candles:
        if(i>max):
            max = i
    return max

def birthdayCakeCandles(candles):
    # Write your code here
    highest_no = getHighestNo(candles)
    counter = 0
    for i in candles:
        if(i==highest_no):
            counter = counter + 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
