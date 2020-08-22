# -*- coding: utf-8 -*-

def is_prime(num: int) -> bool:
    if num < 2: return False
    elif num == 2: return True
    
    if num%2==0 or num%3==0 or num%5==0 or num%7==0: return False
    for i in range(11, num//7, 2):
        if num % i == 0: return False
    return True
    
    
def count_prime_pair(array):
    cur_array = array.copy(()
    
    

if __name__ == "__main__":
    while True: 
        total = int(input())
        array = list(map(int, input().split()))
        
        