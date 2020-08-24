# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            from collections import Counter

            a = input()
            # c是只出现一次的字符的列表
            c = list(map(lambda c: c[0], list(filter(lambda c: c[1] == 1, Counter(a).most_common()))))
            # 如果c为空，说明没有出现一次的字符。输出-1
            if not c:print(-1)
            for i in a:
                if i in c:
                    print(i)
                    break

        except:
            break