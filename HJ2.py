# -*- coding: utf-8 -*-

def c_count():
    string = input()
    
    length = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] == " ": break
        else: length += 1
    return length

print(c_count())