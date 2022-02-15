#!/bin/python3

# Given a list of sock colors, return the number of pairs possible

import math
import os
import random
import re
import sys
# "collections" is a package, "Counter" is a function
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
ar = [10, 10, 20, 30, 20, 50, 30, 20, 40]
n = len(ar)

def sockMerchant(n, ar):
    count = Counter(ar) # Counts the number of times unique values appear
    onlyCountValues = count.values() # Limiting only to "number of times"
    print("only the values: ",onlyCountValues)
    pairs = 0
    for element in onlyCountValues:
        pairs = pairs + (element//2) # Floor division is saying: How many PAIRS can you extract from this number?
    return pairs

print(sockMerchant(n, ar))

