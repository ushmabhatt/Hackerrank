#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append('-1')
    pair_count = 0
    i=0
    while i<n:
        if ar[i]==ar[i+1]:
            pair_count=pair_count+1
            i=i+2
        else:
            i=i+1
    return(pair_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()