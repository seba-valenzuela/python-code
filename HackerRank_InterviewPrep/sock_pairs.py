#!/bin/python3

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
    count = Counter(ar) #this counts the number of times unique values appear
    onlyCountValues = count.values()
    
    
print(ar)
print(n)

