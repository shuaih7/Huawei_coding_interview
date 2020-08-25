# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            a=int(input())
            for i in range(0,21):
                for j in range(0,34):
                    if 5*i+3*j+(100-i-j)*(1/3)==100:
                        print('{} {} {}'.format(i,j,100-i-j))
        except:
            break