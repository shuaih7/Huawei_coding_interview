# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == "__main__":
    while True:
        try:
            dd = defaultdict(list)
            a = input().split()
            # words是输入的单词，lookup是要查找的单词，num是要查找兄弟单词的索引，brothers是找到的兄弟单词列表
            words, lookup, num, brothers = a[1:1 + int(a[0])], a[-2], int(a[-1]), []
            for i in words:
                dd["".join(sorted(i))].append(i)
            for i in dd["".join(sorted(lookup))]:
                if i != lookup: brothers.append(i)
                
            print(len(brothers))
            if brothers and num <= len(brothers):
                print(sorted(brothers)[num - 1])
        except:
            break