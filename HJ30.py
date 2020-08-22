# -*- coding: utf-8 -*-

if __name__ == "__main__":
    try:
        while True:
            alphabet = '0123456789ABCDEF'
            string = list(input().replace(' ',''))
            temp1 = sorted(string[::2])
            temp2 = sorted(string[1::2])
            temp = []
            while temp1 or temp2:
                if temp1:
                    temp.append(temp1.pop(0))
                if temp2:
                    temp.append(temp2.pop(0))
            result = ''
            for i in temp:
                if i.isdigit():
                    result += alphabet[int('{:0>4}'.format(bin(int(i))[2:])[::-1],2)]
                elif 'a' <= i <= 'f' or 'A' <= i <= 'F':
                    i = ord(i.upper())-55
                    result += alphabet[int('{:0>4}'.format(bin(i)[2:])[::-1],2)]
                else:
                    result += i
            print(result)
     
    except Exception:
        pass