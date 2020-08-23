# -*- coding: utf-8 -*-


def getTotalCount(n):
    new1 =1
    new2 =0
    adult=0
    for i in range(1,n):
        adult+=new2
        new2=new1
        new1=adult
    return new1+new2+adult


if __name__ == "__main__": 
    while True:
        try:
            num=int(input())
            print(getTotalCount(num))
        except:
            break
