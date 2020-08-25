# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            s1 = input()
            s2 = input()
     
            short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
     
            repeat = ''
     
            for i in range(len(short)):
                for j in range(len(short)):
                    if short[i:j + 1] in long and j + 1 - i > len(repeat):
                        repeat = short[i:j + 1]
            print(repeat)
        except:
            break