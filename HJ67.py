# -*- coding: utf-8 -*-

# 题目的隐藏条件好像是，不考虑使用括号，数字位置可调
def helper(arr, item):
    if item < 1:
        return False
    if len(arr) == 1:
        return arr[0] == item
    for i in range(len(arr)):
        L = arr[:i] + arr[i+1:]
        v = arr[i]
        if helper(L, item-v) or helper(L, item+v) or helper(L, item*v) or helper(L, item/v):
            return True
    return False


if __name__ == "__main__":
    while True:
        try:
            arr = list(map(int, input().split(' ')))
            if helper(arr, 24):
                print("true")
            else:
                print("false")
        except:
            break