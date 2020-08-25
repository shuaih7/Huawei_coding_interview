# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num, cur, counter = int(input()), 0, 0
            while num >= 1:
                if (num%2 > 0): 
                    cur += 1
                    if cur > counter: counter = cur
                else: cur = 0
                num //= 2
            print(counter)
        except: break