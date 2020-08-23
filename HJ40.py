# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            s = input()
            alnum, dgnum, bknum, elnum = 0, 0, 0, 0
            
            for c in s:
                if c.isalpha(): alnum += 1
                elif c.isdecimal(): dgnum += 1
                elif c == " ": bknum += 1
                else: elnum += 1
                    
            print(alnum)
            print(bknum)
            print(dgnum)
            print(elnum)
        except: break