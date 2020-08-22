# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a = input()
            # res是最终返回的字符串的列表形式，char是提取的英文字母。
            res, char = [False] * len(a), []
            # 经过这个循环，把相应的非英文字母及其位置存储到了res中。并且把英文字母提取出来了。
            for i, v in enumerate(a):
                if v.isalpha():  # 相应地, str.isalnum() 检查字符串是否仅有字母数字构成； str.isdigit() 检查字符串是否仅有字母数字构成
                    char.append(v)
                else:
                    res[i] = v
            # 使用lambda表达式排序，暴力有效。
            char.sort(key=lambda c: c.lower())
            # 将char中对应的字符填到res中。
            for i, v in enumerate(res):
                if not v:
                    res[i] = char[0]
                    char.pop(0)
            print("".join(res))
        except:
            break