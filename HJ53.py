# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a,b = int(input()),0
            if a%2 == 1:
                b = 2
            elif a%4 == 0:
                b = 3
            elif a < 3:
                b = -1
            else:
                b = 4
            print(b)
        except:
            break