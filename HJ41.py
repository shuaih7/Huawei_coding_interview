# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a = int(input())
            weight = list(map(int,input().split()))
            count = list(map(int,input().split()))
            fm,temp,ans = [],[],[0]
            # 将所有砝码放入列表
            for i in range(a):
                for j in range(count[i]):
                    fm.append(weight[i])
            # 称重
            for i in fm:
                temp = set(ans)
                for j in temp:
                    ans.append(j+i)
            # 去重
            print(len(set(ans)))
        except: break
    