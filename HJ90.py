# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            ip=input().split(".")
            isValid=True
            for i in ip:
                if 0<=int(i)<=255:
                    pass
                else:
                    isValid=False
                    break
            print("YES" if isValid else "NO")
        except:
            break