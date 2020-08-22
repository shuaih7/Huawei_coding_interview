# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == "__main__":
    while True:
        try:
            a = input()
            dd = defaultdict(int)
            for i in a:
                dd[i] += 1
            for i in dd:
                if dd[i] == min(dd.values()):
                    a = a.replace(i, "") # Replace a character or a substring from the input string
            print(a)
        except:
            break