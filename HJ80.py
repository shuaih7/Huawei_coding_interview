# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num1 = int(input())
            arr1 = list(map(int, input().split()))
            num2 = int(input())
            arr2 = list(map(int, input().split()))
            
            result = sorted(set(arr1+arr2))
            
            for i in range(len(result)): print(result[i], end="")
            print()
            
        except: break