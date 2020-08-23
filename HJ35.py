# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            matrix, array = [], []
            
            for i in range(num): array.append(-1)
            for i in range(num): matrix.append(array.copy()) # Must copy the python list!
            x, y, i = 0, 0, 1
            
            while matrix[0][-1] < 0:
                if y < 0: 
                    y = x
                    x = 0
                matrix[y][x] = i
                x, y, i = x+1, y-1, i+1
     
            for y in range(num):
                for x in range(num):
                    if matrix[y][x] > 0: print(str(matrix[y][x])+" ", end="")
                print()
        except: break
        