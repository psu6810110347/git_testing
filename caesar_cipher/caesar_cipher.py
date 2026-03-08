import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = []
    k = k % 26 
    
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + k) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
            
    return "".join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
