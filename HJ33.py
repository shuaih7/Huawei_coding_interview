# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            inp_add = list(map(int, input().split(".")))
            inp_num = int(input())
            
            ## Convert address to number
            number = 0
            for i in range(len(inp_add)): number += inp_add[i]*(256**(4-i-1))
            
            ## Convert number to address
            add1 = str(inp_num >> 24)
            add2 = str((inp_num & 0x00FF0000) >> 16)
            add3 = str((inp_num & 0x0000FF00) >> 8)
            add4 = str(inp_num & 0x000000FF)
            address = add1 + "." + add2 + "." + add3 + "." + add4
            
            print(number)
            print(address)
        except: break
        