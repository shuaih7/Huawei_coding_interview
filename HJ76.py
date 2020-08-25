# -*- coding: utf-8 -*-

if __name__ == "__main__":
    if __name__ == "__main__":
        while True:
            try:
                num = int(input())
                if num == 1: print(1)
                else:
                    if num % 2 > 0: array = [num**2]
                    else: array = [num**2-1, num**2+1]
                    for i in range(num//2-1+num%2):
                        array.insert(0, array[0]-2)
                        array.append(array[-1]+2)
                    for i in range(len(array)):
                        print(array[i], end="")
                        if i < len(array)-1: print("+", end="")
                        else: print()
            except: break