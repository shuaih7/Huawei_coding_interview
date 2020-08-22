# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input()
    words = sentence.split()
    for word in words[::-1]: 
        print(word, end="")
        print(" ", end="")