# -*- coding: utf-8 -*-

def longestPalindrome(s):
    if s==s[::-1]:return len(s)
    maxLen=0
    for i in range(len(s)):
        if i-maxLen>=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
            maxLen+=2
            continue
        if i-maxLen>=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
            maxLen+=1
    return maxLen

if __name__ == "__main__":
    while True:
        try:
            a=input()
            if a:
                print(longestPalindrome(a))
     
        except:
            break