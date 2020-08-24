# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            total = 0
            
            for i in range(7, num+1):
                if "7" in str(i) and  i%7 > 0: total += 1
            total += num // 7
            print(total)
        except: break