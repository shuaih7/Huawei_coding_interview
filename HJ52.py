# -*- coding: utf-8 -*-

# Python 如何计算编辑距离
# https://www.jianshu.com/p/9a53f32cf62b

def editDistance(str1, str2):
    len1, len2 = len(str1) + 1, len(str2) + 1
    dp = [[0 for i in range(len2)] for j in range(len1)]
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j
    for i in range(1, len1):
        for j in range(1, len2):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]


if __name__ == "__main__":
    while True:
        try:
            print(editDistance(input(), input()))
        except:
            break