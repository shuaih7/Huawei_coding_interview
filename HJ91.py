# -*- coding: utf-8 -*-

def uniquePath(m, n):
    if m == 1 or n == 1:
        return 1
    result = [[0 for i in range(n)]] * m
    for i in range(m):
        result[i][0] = 1
    for i in range(n):
        result[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[m - 1][n - 1]


if __name__ == "__main__":
    while True:
        try:
            print(uniquePath(*map(lambda c:int(c)+1,input().split())))
        except:
            break