# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            s = input().split()
            for i, c in enumerate(s[::-1]):
                print(c[::-1], end="")
                if i < len(s)-1: print(" ", end="")
            print()
        except: break