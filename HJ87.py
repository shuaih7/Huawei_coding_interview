# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from functools import reduce
    while True:
        try:
            s = input()
            password = []
            password.extend(s)
            p1,p2,p3,p4 = [],[],[],[]
     
            for i in password:
                if i.isupper():
                    p1.append(i)
                elif i.islower():
                    p2.append(i)
                elif i.isdigit():
                    p3.append(i)
                else:
                    p4.append(i)
     
            score = []
            if len(s) <= 4:         
                score.append(5)
            elif 5 <= len(s) <= 7:
                score.append(10)
            else:
                score.append(25)
     
            if p1 or p2:       
                if len(p1) == 0 or len(p2) == 0:
                    score.append(10)
                else:
                    score.append(20)
     
            if len(p3) == 1:        
                score.append(10)
            elif len(p3) > 1:
                score.append(20)
     
            if len(p4) == 1:       
                score.append(10)
            elif len(p4) > 1:
                score.append(25)
     
            if (p1 or p2) and  p3:     
                score.append(2)
            elif (p1 or p2) and p3 and p4:
                score.append(3)
            elif p1 and p2 and p3 and p4:
                score.append(5)
     
            result = reduce(lambda x,y : x+y,score)
            if result >= 90:
                print('VERY_SECURE')
            elif result >= 80:
                print('SECURE')
            elif result >= 70:
                print('VERY_STRONG')
            elif result >= 60:
                print('STRONG')
            elif result >= 50:
                print('AVERAGE')
            elif result >= 25:
                print('WEAK')
            elif result >= 0:
                print('VERY_WEAK')
        except:break
