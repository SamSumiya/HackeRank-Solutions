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

def calc(l):
    positives = 0 
    negatives = 0 
    neutrals = 0 
    
    for i in l: 
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += 1 
        else:
            neutrals += 1
    return positives, negatives, neutrals

def plusMinus(arr):
    pos, neg, neu = calc(arr) 
    length = len(arr) 
    
    print ('{:.6f}'.format(pos/length))
    print ('{:.6f}'.format(neg /length))
    print ('{:.6f}'.format(neu /length))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
