# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            aln = list(range(n))
            m = input()
            margin = 4 if n >= 4 else n
            this = 0
            screen = aln[:margin] 
            for i in m:
                if i == 'U': 
                    this -= 1
                    if this not in screen:
                        if this == -1:
                            this = n-1
                            screen = aln[-margin:]
                        else:
                            screen = aln[this:this+margin]
                else: 
                    this += 1
                    if this not in screen:
                        if this == n:
                            this = 0
                            screen = aln[:margin]
                        else:
                            screen = aln[this-margin+1:this+1]
     
            print(' '.join([str(i+1) for i in screen]))
            print(aln[this]+1)
             
        except:
            break