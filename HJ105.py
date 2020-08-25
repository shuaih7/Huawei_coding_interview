# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            arr = list(map(int, input().split()))
            pos = list(filter(lambda x: x > 0, arr))
            print(len(arr) - len(pos))
            print('%.1f' % (sum(pos) / len(pos)))
        except: break