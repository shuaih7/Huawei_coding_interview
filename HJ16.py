# -*- coding: utf-8 -*-

money, things = map(int, input().split())
money = money // 10    #money都是10的整数，整除后，减小循环次数
#三列分别表示主件，附件1，附件2
weight = [[0] * 3 for _ in range(0, things + 1)]    #价格
value = [[0] * 3 for _ in range(0, things + 1)]    #价值=价格*重要度
result = [[0] * (money + 1) for _ in range(things + 1)]
for i in range(1, things + 1):
    prices, degree, depend = map(int, input().split())    #分别为价格，重要性，主附件
    prices = prices // 10
  
    if depend == 0:    #主件
        weight[i][0] = prices
        value[i][0] = prices * degree
  
    elif weight[depend][1] == 0:    #附件
        weight[depend][1] = prices    #第一个附件
        value[depend][1] = prices * degree
  
    else:
        weight[depend][2] = prices    #第二个附件
        value[depend][2] = prices * degree
  
#遍历计算
for i in range(1, things + 1):
    for j in range(money, 9, -10):
        if j >= weight[i][0]:    #可以容下第i个主件时,比较不放第i个或者放第i个物品的价值
            result[i][j] = max(result[i - 1][i], result[i - 1][j - weight[i][0]] + value[i][0])
        else:
            result[i][j] = result[i - 1][j]
        if j >= (weight[i][0] + weight[i][1]):    #可以容下第i个主件和此主件的第1个附件时
            result[i][j] = max(result[i - 1][j], result[i - 1][j - weight[i][0] - weight[i][1]] + value[i][0] + value[i][1])
        else:
            result[i][j] = result[i - 1][j]
        if j >= (weight[i][0] + weight[i][2]):    #可以容下第i个主件和此主件的第2个附件时
            result[i][j] = max(result[i - 1][j],
                               result[i - 1][j - weight[i][0] - weight[i][2]] + value[i][0] + value[i][2])
        else:
            result[i][j] = result[i - 1][j]
        if j >= (weight[i][0] + weight[i][1] + weight[i][2]):    #可以容下第i个主件和此主件的第1个附件和第2个附件时
            result[i][j] = max(result[i - 1][j],
                               result[i - 1][j - weight[i][0] - weight[i][1] - weight[i][2]] + value[i][0] + value[i][1] + value[i][2])
        else:
            result[i][j] = result[i - 1][j]
print(result[things][money] * 10)