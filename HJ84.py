# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            s, num = input(), 0
            for c in s:
                if c.isalpha() and c.isupper(): num += 1
            print(num)
        except: break