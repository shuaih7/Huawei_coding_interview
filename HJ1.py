# -*- coding: utf-8 -*-

# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# str.count(sub, start= 0,end=len(string))
# -----------------------------------------------------------------------
# 内容来源： https://www.runoob.com/python/att-string-count.html

def c_count(): 
    str1 = input().lower() 
    str2 = input().lower() 
    count = str1.count(str2) 
    return count 

print(c_count())