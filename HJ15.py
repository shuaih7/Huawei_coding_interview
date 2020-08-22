# -*- coding: utf-8 -*-

if __name__ == "__main__":
    num = int(input())
    
    zero_num = 1
    while num//2 != 0:
        if num%2 == 1: zero_num += 1
        num //= 2
        
    print(zero_num)