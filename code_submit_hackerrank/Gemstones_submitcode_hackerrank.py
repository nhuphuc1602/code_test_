import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
        i, j = 0,0
        for i in range(i, len(arr)+1):
            for j in range(i+1, len(arr)):
                if (arr[i] + arr[j] == m):
                    s1 = str(i+1)
                    s2 = str(j+1)
                    s = s1 + " " + s2
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(''.join(map(str, result)))#Nhớ xóa khoảng trắng dòng này để pass testcases trên HackerRank
        fptr.write('\n')

    fptr.close()