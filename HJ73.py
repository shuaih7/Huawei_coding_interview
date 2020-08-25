# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import datetime
    while True:
        try:
            print(datetime.datetime(*map(int, input().split())).strftime("%j").lstrip("0"))
     
        except:
            break