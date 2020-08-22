# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a, b = input(), input()
            resA, resB = "", ""
            for i in a:
                if i.isupper():
                    if i != "Z":
                        resA += chr(ord(i) + 1).lower()
                    else:
                        resA += "a"
                elif i.islower():
                    if i != "z":
                        resA += chr(ord(i) + 1).upper()
                    else:
                        resA += "A"
                elif i.isdigit():
                    if i != "9":
                        resA += chr(ord(i) + 1)
                    else:
                        resA += "0"
            for i in b:
                if i.isupper():
                    if i != "A":
                        resB += chr(ord(i) - 1).lower()
                    else:
                        resB += "z"
                elif i.islower():
                    if i != "a":
                        resB += chr(ord(i) - 1).upper()
                    else:
                        resB += "Z"
                elif i.isdigit():
                    if i != "0":
                        resB += chr(ord(i) - 1)
                    else:
                        resB += "9"
            print(resA)
            print(resB)
        except:
            break