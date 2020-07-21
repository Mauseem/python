#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    un = list(set(ar))
    pair = 0
    for num in un:
        pair += (ar.count(num) // 2)
    print(pair)

