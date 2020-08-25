# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import re
    while True:
        try:
            a,b = input().strip(),input().strip()
            a = a.replace("?","\w{1}").replace(".","\.").replace("*","\w*") # important string operation
            c = re.findall(a,b)
            if b in c and len(c) == 1: print("true")
            else: print("false")
        except: break