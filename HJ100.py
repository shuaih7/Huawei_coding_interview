# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a = int(input())
            print(3 * a * (a + 1) // 2 - a)
        except:break