# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            h = int(input())
            total = h
            
            b1 = h/2
            b2 = b1/2
            b3 = b2/2
            b4 = b3/2
            b5 = b4/2
            
            total += (b1*2 + b2*2 + b3*2 + b4*2)
            
            print(format(total, ".6f"))
            print(format(b5, ".6f"))
        except: break
        