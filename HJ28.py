# -*- coding: utf-8 -*-

import math

def is_prime(num: int) -> bool:
    if num < 2: return False
    elif num == 2: return True
    
    for i in range(2, math.sqrt(num)):
        if num % i == 0: return False
    else: return True
    
    
def count_prime_pair(array):
    cur_array = array.copy(()
    
    

if __name__ == "__main__":
    while True: 
        total = int(input())
        array = list(map(int, input().split()))
        
        