# -*- coding: utf-8 -*-

d={
    "abc":2,
    "def":3,
    "ghi":4,
    "jkl":5,
    "mno":6,
    "pqrs":7,
    "tuv":8,
    "wxyz":9,
}

if __name__ == "__main__":
    while True:
        try:
            a,res=input(),""
            for i in a:
                if i.isupper():   # check whether the character is upper case
                    if i!="Z":
                        res+=chr(ord(i.lower())+1)
                    else:
                        res+="a"
                elif i.islower(): # check whether the character is lower case
                    for j in d.keys():
                        if i in j:
                            res+=str(d[j])
                            break
                else:
                    res+=i
            print(res)
     
        except:
            break