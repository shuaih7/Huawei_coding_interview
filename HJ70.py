# -*- coding: utf-8 -*-

def juzhengchengfa(s, j):
    for i in range(len(s)):
        if s[i]=='(' and s[i+3]==')':                                                 # 最先计算的两个矩阵位置，i/2
            k = j[int(i/2)][0]*j[int(i/2)][1]*j[int(i/2)+1][1]                        # 每次计算量
            s = s[0:i]+'Z'+s[i+4:]                                                    # 更新计算法则
            j = j[:int(i/2)] + [[j[int(i/2)][0], j[int(i/2)+1][1]]] + j[int(i/2)+1:]  # 得到新的矩阵的行列数
            return s, j, k
            

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            ij = [[int(i) for i in input().split()] for k in range(n)]
            cf = str(input())
            m = 0
            for i in range(n-1):    # 一共计算n-1次
                cf, ij, mn = juzhengchengfa(cf, ij)
                m += mn
            print(m)
        except:
            break