# -*- coding: utf-8 -*-

def get_number(total, group=3):
    if total < group - 1: return 0
    
    number, cur = 0, total
    while cur >= group:
        number += cur // group
        cur = cur % group + cur // group
    if cur == group - 1: number += 1
    
    return number
    

if __name__ == "__main__":
    while True: print(get_number(int(input())))