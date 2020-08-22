# -*- coding: utf-8 -*-

# Use defaultdict to do this 
# defaultdict will return a default value if there occurs the KeyError

from collections import defaultdict

if __name__ == "__main__":
    try:
        a,dd = int(input()),defaultdict(int) # defaultdict(int) will return 0 if there occurs the KeyError
        for i in range(a):
            key,val = map(int,input().split()) # Map a list's item to a function -> map(function, list)
            dd[key] += val
        for i in sorted(dd.keys()):
            print(str(i) + " " + str(dd[i]))

    except Exception as expt: print(expt)