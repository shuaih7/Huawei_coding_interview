# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a,res = list(input()),list()
    if '"' in a:
        for i in range(a.count('"')):
            if i % 2 == 0:
                res.extend(''.join(a[:a.index('"')]).split())
            else:
                res.append(''.join(a[:a.index('"')]))
            a = a[a.index('"')+1:]
        res.append(''.join(a))
    else:
        res = ''.join(a).split()
    print(len(res))
    for i in res:
        print(i)