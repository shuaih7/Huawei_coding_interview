# -*- coding: utf-8 -*-

if __name__ == "__main__":
    num = int(input())
    index = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
    result = ""
    while num // 10 > 0:
        a = round(num % 10)
        
        if index[a] < 0: 
            index[a] = 1
            result += str(a)
        num //= 10
    if index[num] < 0: result += str(num)
    
    print(result)
    