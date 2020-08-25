# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            x=int(input())#第一个矩阵的行数#3
            y=int(input())#第一个矩阵的列数和第二个矩阵的行数#4
            z=int(input())#第二个矩阵的列数#5
            A=[]#矩阵A初始化
            B=[]#矩阵B初始化
            for i in range(x):#矩阵A赋值
                li=input().split()
                li=[int(v) for v in li]
                A.append(li)
            for j in range(y):#矩阵B赋值
                li=input().split()
                li=[int(v) for v in li]
                B.append(li)
            ans=[[0 for i in range(z)] for j in range(x)]#结果初始化3*5
            for i in range(x):
                for j in range(z):
                    for k in range(y):
                        ans[i][j]+=A[i][k]*B[k][j]
            for i in range(x):
                for j in range(z):
                    if j==(z-1):
                        print(ans[i][j])
                    else:
                        print(ans[i][j],end=' ')
        except:
            break