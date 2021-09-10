#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive, negative, zero = 0, 0, 0
    arr_len = len(arr)
    for i in arr:
        if(i==0):
            zero = zero + 1
        if(i>0):
            positive = positive + 1
        if(i<0):
            negative = negative + 1
    print("%.6f" % float(positive/arr_len))
    print("%.6f" % float(negative/arr_len))
    print("%.6f" % float(zero/arr_len))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
