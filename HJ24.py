# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        num = int(input())
        array = list(map(int, input().split()))
        
        if len(array) <= 2: print(0)
        else:
            minimal = len(array)
            
            for i in range(len(array)):
                removal = 0
                
                if i > 0 and i < len(array)-1: 
                    for j in range(0,i,1): 
                        if array[j] >= array[j+1]: removal += 1
                    for k in range(i,len(array)-1,1): 
                        if array[k] <= array[k+1]: removal += 1
                        
                elif i == 0: 
                    for j in range(len(array)-1):
                        if array[j] >= array[j+1]: removal += 1
                elif i == len(array)-1:
                    for k in range(len(array)-1):
                        if array[k] <= array[k+1]: removal += 1
               
                if removal < minimal: minimal = removal
                        
        print(minimal)