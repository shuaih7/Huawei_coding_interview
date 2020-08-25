# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
# !/usr/bin/python3
# 解题思路：先按提干要求构建ls1和ls2，计算ls1和ls2总和之差的绝对值t，用ls3抹平两者差距；
# 问题变成了：ls3的总和减去t之后的值d，d能否被ls3中元素平分。如果d是奇数，那么一定不能平分。
# 如果d是偶数，那么变了成能不能从ls3中挑选出若干元素，他们的和为d/2,与打靶问题有类似之处;
# 但是本题比打靶问题简单，打靶问题每次射击的结果从0到10有11种情况，本地只有两种情况
# 分解子问题：
# 使用递归开始查找，对ls3中的每个元素遍历，每个元素都分两种情况：参与构建d/2和参与构建d/2;
# 形成一个二叉树，记录查找结果;
# 边界条件：
# 1.如果target为0了，那么说明找到了一个构建d/2的方法
# 2.如果ls3都查找完了还没有找到，说明没有办法构建d/2
# 本题也可以使用动态规划实现： dp[i][j]表示ls3中前一个元素能否构建j
# 状态转义方程式：dp[i][j] = dp[i - 1][j] or dp[i - 1][j - ls3[i]]
 
def search(ll, target):
    if target == 0:
        return True
 
    if not ll:
        return False
 
    return search(ll[1:], target) or search(ll[1:], target - ll[0])

if __name__ == "__main__":
    while True:
        try:
            m = int(input())
            ls = list(map(int, input().split()))
     
            ls1 = []
            ls2 = []
            ls3 = []
     
            for i in ls:
                if i % 5 == 0:
                    ls1.append(i)
                elif i % 3 == 0:
                    ls2.append(i)
                else:
                    ls3.append(i)
     
            t = abs(sum(ls1) - sum(ls2))
            d = sum(ls3) - t
            if d % 2 != 0:
                print('false')
            else:
                if search(ls3, d / 2):
                    print('true')
                else:
                    print('false')
     
        except:
            break