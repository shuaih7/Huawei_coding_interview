# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 贪心算法
    while True:
        try:
            num = input().split('/')
            a = int(num[0])  #a是分子，b是分母
            b = int(num[1])
            c = 0
            temp = ''  #定义空的字符串，等会存储计算结果
            while(a>=1):
                if b % (a-1) == 0:
                    temp = '1/'+ str(b//(a-1))+'+'+'1/'+str(b)
                    print(temp)
                    break
                else:
                    c = (b//a) + 1
                    temp = '1/'+str(c)+'+'
                    print(temp,end="")
                    a = a*c - b
                    b = b*c
                    if b % a == 0:
                        b = b // a
                        a = 1
                        temp = str(a) + '/' + str(b)
                        print(temp)
                        break
        except:
            break