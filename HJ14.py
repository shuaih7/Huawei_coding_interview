# -*- coding: utf-8 -*-

# Difference between sort and sorted
# a = ["we", "are", "the", "champions"]
# a.sort(key=str.lower) or you can use a = sorted(a, key=str.lower)
# Note that b = a.sort(key=str.lower) will return None

if __name__ == "__main__":
    words = []
    num = int(input())
    
    for i in range(num): words.append(input())
    words = sorted(words)
    for word in words: print(word)