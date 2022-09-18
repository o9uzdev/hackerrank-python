#The included code stub will read an integer, n, from STDIN.

#Without using any string methods, try to print the following:

#Note that "..." represents the consecutive values in between.

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

if n in range(1,151):
    output = "1"
    for i in range(2,n+1):
        output = output + str(i)
    print(output)
