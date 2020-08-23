# -*- coding: utf-8 -*-

def finder(s) -> int:
    if len(s) <= 1: return len(s)
    len_array = [1]

    for pos in range(len(s)):
        if pos == 0: 
            length = 0
            for i in range(len(s)):
                if s[i] == s[0]: length += 1
                else: break
            len_array.append(length)
            
        elif pos == len(s)-1:
            length = 0
            for c in s[::-1]: 
                if c == s[-1]: length += 1
                else: break
            len_array.append(length)
        
        else:
            if s[pos-1] == s[pos+1]:
                length = 3
                for i in range(2,len(s),1):
                    if pos-i < 0 or pos+i == len(s): break
                    elif s[pos-i] == s[pos+i]: length += 2
                    else: break
                len_array.append(length)
                    
            if s[pos] == s[pos+1]:
                length = 2
                for i in range(1,len(s),1):
                    if pos-i < 0 or pos+i+1 == len(s): break
                    elif s[pos-i] == s[pos+i+1]: length += 2
                    else: break
                len_array.append(length)
        
    return max(len_array)
            

if __name__ == "__main__":
    while True:
        try:
            s = input()
            print(finder(s))
        except: break