import math
import os
import random
import re
import sys

def gridChallenge(grid):
    sorted_grid = ["".join(sorted(row)) for row in grid]
    
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])
    
    for j in range(cols):
        for i in range(1, rows):
            if sorted_grid[i][j] < sorted_grid[i-1][j]:
                return "NO"
                
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
