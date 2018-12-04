#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    colors = []
    pairs_counter = 0
    for i in range(n):
        if ar[i] in colors:
            idx = colors.index(ar[i])
            del colors[idx]
            pairs_counter += 1
        else:
            colors.append(ar[i])

    return pairs_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

