# 05-loops.py
# Task
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        if i<n:
            print(i**2)