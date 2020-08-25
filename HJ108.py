# -*- coding: utf-8 -*-

def print_func():
    in_put = input().split()
    a = int(in_put[0])
    b = int(in_put[1])
    if not a *b:
        return 0
    if a > b:
        c = a
    else:
        c = b
    temp = c
    while c < a * b:
        if (c % a == 0) and (c % b == 0):
            return c
        c += temp
    return a * b


if __name__ == "__main__":
    while True:
        try: print(print_func())
        except: break