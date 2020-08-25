# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            from collections import defaultdict
     
            dd, s, res = defaultdict(list), input(), ""
            for i in set(s):
                dd[s.count(i)].append(i)
     
            for i in sorted(dd.keys(), reverse=True):
                res += "".join(sorted(dd[i], key=ord))
            print(res)
     
        except:
            break