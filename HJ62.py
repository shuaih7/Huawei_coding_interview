# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num = abs(int(input()))
            if num == 0: counter = 0
            else: counter = 1
            
            while num//2 > 0:
                counter += num % 2
                num //= 2
                
            print(counter)
        except: break