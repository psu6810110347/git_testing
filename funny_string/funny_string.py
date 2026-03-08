import math
import os
import random
import re
import sys

def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        if diff_s != diff_r:
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(output_path, 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
