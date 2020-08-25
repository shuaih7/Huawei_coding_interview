# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            
            counter = 0
            for i in range(num):
                d = len(str(i))
                sqr = i**2
                
                sqr_str = str(sqr)
                cur_str = str(i)
                
                if sqr_str[-1*d:] == cur_str[-1*d:]: counter += 1
            print(counter)
        except: break