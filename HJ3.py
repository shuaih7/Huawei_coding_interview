# -*- coding: utf-8 -*-

import os, sys


def merge_sort(array):
    if len(array) <= 1: return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    return merge(merge_sort(left), merge_sort(right))
  

def merge(left, right):
    result = []
    """
    # General solution
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]: result.append(left.pop(0))
        else: result.append(right.pop(0))
        
    result += left
    result += right
    """
    
    # Solution excluding the same number
    while len(left) > 0 and len(right) > 0:
        if left[0] == right[0]:  
            result.append(left.pop(0))
            right.pop(0)
        elif left[0] < right[0]: result.append(left.pop(0))
        else: result.append(right.pop(0))
        
    if len(left) and left[0] > result[-1]:   result += left
    if len(right) and right[0] > result[-1]: result += right
    
    return result
    

if __name__ == "__main__":
    # Input line
    str_array, str_num = input().strip().split(";")
    
    # Data type converting
    str_items = str_array.split(",")
    num = int(str_num)
    
    array = []
    for item in str_items:
        array.append(int(item))
        
    print(merge_sort(array))
    # print(sorted(array)) -> timesort
    
    
    
    