# -*- coding: utf-8 -*-

import re # This module is used for the python string matching

if __name__ == "__main__":
    try:
        while 1:
             
            s = input()
             
            a = re.findall(r'(.{3,}).*\1', s)
            b1 = re.findall(r'\d', s)
            b2 = re.findall(r'[A-Z]', s)
            b3 = re.findall(r'[a-z]', s)
            b4 = re.findall(r'[^0-9A-Za-z]', s)
     
            if ([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(s) > 8): print("OK") 
            else: print("NG")
          
    except:
        pass