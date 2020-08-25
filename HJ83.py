# -*- coding: utf-8 -*-

def f1(a,b,c,d):
    if a>c-1 or b>d-1 or a<0 or b<0:
        return False
    else:
        return True
def f(a,b):
    if a>9 or b>9 or a<0 or b<0:
        return False
    else:
        return True
        

if __name__ == "__main__":
    while True:
        try:
            c,l = map(int,input().split())
            if not f(c,l):
                print(-1)
            else:
                print(0)
                x1,y1,x2,y2 = map(int,input().split())
                if f1(x1,y1,c,l) and f1(x2,y2,c,l):
                    print(0)
                else:
                    print(-1)
                c1 = input()
                c1 = int(c1)
                if c1>=c or c1<0:
                    print(-1)
                else:
                    print(0)
                l1 = input()
                l1 = int(l1)
                if l1>=l or l1<0:
                    print(-1)
                else:
                    print(0)
                c2,l2 = map(int,input().split())
                if f1(c2,l2,c,l):
                    print(0)
                else:
                    print(-1)
        except: break
    