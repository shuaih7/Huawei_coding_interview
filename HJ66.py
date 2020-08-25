# -*- coding: utf-8 -*-

d = {'reset':'reset what',
     'reset board':'board fault',
     'board add':'where to add',
     'board delet':'no board at all',
     'reboot backplane':'impossible',
     'backplane abort':'install first'}

if __name__ == "__main__":
    while True:
        try:
            a = input().split(' ')
            n = 0
            if len(a) == 1 and d['reset'][0:len(a[0])] == a[0]:
                res = d['reset']
                n = n + 1
            elif len(a) == 2:
                for i,j in d.items():
                    b = i.split( )
                    if len(b) == 2 and b[0][0:len(a[0])] == a[0] and b[1][0:len(a[1])] == a[1] :
     
                        res = j
                        n = n + 1
            if n == 1:
                print(res)
            else:
                print('unkown command')
        except Exception as e:
            break