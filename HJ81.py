# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a,b=set(input()),set(input())
            print ("true" if a&b==a else "false")
        except:
            break