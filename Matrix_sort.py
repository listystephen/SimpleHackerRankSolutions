#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	#Reading no. of Row and colmn
    nm = raw_input().split()

    n = int(nm[0])
    m = int(nm[1])

    arr = []
	#Assigning values to list of list (Matrix)
    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))
    #print arr
    k = int(raw_input())
    
    arr = sorted(arr, key=lambda x : x[k])
    print('\n'.join(' '.join(map(str,sl)) for sl in arr))
