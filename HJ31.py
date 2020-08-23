# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s = input().split()
    result = ''

    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i] + ' '
        else:
            for j in range(len(s[i])):
                if s[i][j].isalpha():
                    result += s[i][j]
                else:
                    result += ' '
        result += ' '

    s1 = result.split()
    print(' '.join(s1[::-1]))