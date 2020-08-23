# -*- coding: utf-8 -*-

def checklegality(s):
    flag = True
    if len(s) != 4:
        flag = False
        return flag
    for i in s:
        if not (i.isdecimal() and 0<=int(i)<=255):
            flag = False
    return flag
 
def tenToTwo(s):
    s2 = []
    for i in s:
        a2 = str(bin(int(i)))[2:]
        if len(a2) < 8:
            a2 = '0'*(8-len(a2))+a2
        s2.append(a2)
    return s2
 
def andTwo(s1,s2):
    alist = []
    for i in range(len(s1)):
        a = ''
        for j in range(8):
            a += str(int(s1[i][j]) and int(s2[i][j]))
        alist.append(a)
    return '.'.join(alist)


if __name__ == "__main__":
    while True:
        try:
            result = -1
            m_10, ip1_10, ip2_10 = [i.split('.') for i in [input(),input(),input()]]
            for s in [m_10, ip1_10, ip2_10]:
                if not checklegality(s):
                    result =1
            if result != 1:
                m_2, ip1_2, ip2_2 = [tenToTwo(i) for i in [m_10, ip1_10, ip2_10]]
                and1 = andTwo(m_2, ip1_2)
                and2 = andTwo(m_2, ip2_2)
                if and1 == and2:
                    result = 0
                else:
                    result = 2
            print(result)
        except:
            break