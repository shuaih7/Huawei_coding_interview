# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            s = input()
            num = int(input())
            
            result, maximal = s[:num], 0
            for i in range(len(s)-num-1):
                counter = 0
                for n in range(num): 
                    if s[i+n] in "GC": counter += 1
                if counter > maximal: 
                    result = s[i:i+num]
                    maximal = counter
            print(result)
        except: break