# -*- coding: utf-8 -*-

"""
# Time takes too long ...

def is_perfect(num) -> bool:
    if num == 1: return False
    elif num % 2 == 0: elems = [1, 2, num//2]
    else: elems = [1]

    for i in range(3, num//3+1):
        if num % i == 0: elems.append(i)
    if sum(elems) == num: return True
    else: return False
            
if __name__ == "__main__":
    while True:
        try:
            total, num = 0, int(input())
            for i in range(2, num+1):
                if is_perfect(i): total += 1
            print(total)
        except: print(-1)
"""

import sys
for s in sys.stdin:
    if len(s.strip())==0:
        continue
    k = int(s)
    m = []
    for i in range(2, k+1):
        n = []
        for j in range(2,int(pow(i, 1/2))+1):
            if i%j==0:
                n.append(i/j)
                n.append(j)
                if sum(n)>i and j<i:
                    break
        if sum(n)+1 ==i:
            m.append(i)
    print(len(m))