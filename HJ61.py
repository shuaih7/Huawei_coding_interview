# -*- coding: utf-8 -*-

def count(m,n):#m为多少个苹果，n为多少个盘子
    #1. 盘子多，苹果少，即n>m，count(m,n)=count(m,m)
    #2. 盘子少，苹果多，即n<=m,又分两种情况：
    #  （1）有至少一个空盘子：count(m,n)=count(m,n-1)
    #  （2）没有空盘子：count(m,n)=count(m-n,n)
    if m==0 or n==1:
        return 1
    if n>m:
        return count(m,m)
    else:
        return count(m,n-1)+count(m-n,n)
         
if __name__ == "__main__":
    while True:
        try:
            l=input().split()#['7','3']
            m=int(l[0])
            n=int(l[1])
            print(count(m,n))
        except:
            break
