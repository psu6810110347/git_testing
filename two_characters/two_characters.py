import math
import os
import random
import re
import sys

def alternate(s):
    unique_chars = list(set(s))
    max_len = 0
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            
            filtered = [c for c in s if c == char1 or c == char2]
            
            is_alternating = True
            for k in range(len(filtered) - 1):
                if filtered[k] == filtered[k+1]:
                    is_alternating = False
                    break
            
            if is_alternating and len(filtered) > max_len:
                max_len = len(filtered)
                
    return max_len
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
