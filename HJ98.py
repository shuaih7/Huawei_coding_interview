# -*- coding: utf-8 -*-

class sell:
    def __init__(self):
        self.A = None
        self.N_A = None
        self.money = None
        self.balance = 0
         
    def dostring(self,s):
        s = s.split(";")
        self.init(s[0])
        for i in range(1,len(s)):
            if len(s[i])>0:
                if s[i][0]=="p":self.OpPay(s[i])
                if s[i][0]=='b':self.OpBuy(s[i])
                if s[i][0]=='c':self.OpChange()
                if s[i][0]=='q':self.OpQuary(s[i])
        return
     
    def init(self,a):
        a = a.replace("-"," ")
        a = a.split()
        for i in range(len(a)):
            if a[i]=='r':
                self.A = {'A1':[2,int(a[i+1])],'A2':[3,int(a[i+2])],'A3':[4,int(a[i+3])],'A4':[5,int(a[i+4])],'A5':[8,int(a[i+5])],'A6':[6,int(a[i+6])]}
                self.N_A = [int(a[i+j]) for j in range(1,7)]
        self.money = {1:int(a[7]),2:int(a[8]),5:int(a[9]),10:int(a[10])}
        print("S001:Initialization is successful")
     
    def OpPay(self,temp):
        temp2 = temp.split(" ")
        p = int(temp2[1])
        if p not in [1,2,5,10]:
            print("E002:Denomination error")
            return
        M = 1 * self.money[1] + 2 * self.money[2]
        if (M < p)&(p not in [1,2]):
            print("E003:Change is not enough, pay fail")
            return
        if p>10:
            print("E004:Pay the balance is beyond the scope biggest")
            return
        if sum(self.N_A)==0:
            print("E005:All the goods sold out")
            return
        else:
            self.money[p] = self.money[p]+1
            self.balance = self.balance + p
            print("S002:Pay success,balance="+str(self.balance))
     
    def OpBuy(self,temp):
        temp2 = temp.split(" ")
        b = temp2[1]
        if b not in self.A:
            print("E006:Goods does not exist")
            return
        if self.A[b][1] == 0:
            print("E007:The goods sold out")
            return 
        if self.balance < self.A[b][0]:
            print("E008:Lack of balance")
            return        
        self.balance = self.balance-self.A[b][0]
        print("S003:Buy success,balance="+str(self.balance))
     
    def OpChange(self):
        c = self.balance
        if c == 0:
            print("E009:Work failure",end='')
        else:
            T = [0,0,0,0]
            while c > 0:
                if (c >= 10) & (self.money[10]>0):
                    T[3] = T[3]+1
                    c = c - 10
                    self.money[10] = self.money[10] - 1
                elif (c >= 5) & (self.money[5]>0):
                    T[2] = T[2]+1
                    c = c - 5
                    self.money[5] = self.money[5] - 1
                elif (c >= 2) & (self.money[2]>0):
                    T[1] = T[1]+1
                    c = c - 2
                    self.money[2] = self.money[2] - 1
                elif c > self.money[1]:
                    T[0] = T[0]+self.money[1]
                    self.money[1] = 0
                    c = 0
                else:
                    T[0] = T[0]+c
                    self.money[1] = self.money[1]-c
                    c = c - 1
            print("1 yuan coin number="+str(T[0]))
            print("2 yuan coin number="+str(T[1]))
            print("5 yuan coin number="+str(T[2]))
            print("10 yuan coin number="+str(T[3]))
            self.balance = 0
         
    def OpQuary(self,temp):
        if temp == 'q 0':
            for v in self.A:
                print(v+str(self.A[v][0])+str(self.A[v][1]))
        if temp == 'q 1':
            print("1 yuan coin number="+str(self.money[1]))
            print("2 yuan coin number="+str(self.money[2]))
            print("5 yuan coin number="+str(self.money[5]))
            print("10 yuan coin number="+str(self.money[10]))
        else:
            print("E010:Parameter error",end='')
 
if __name__ == '__main__':
    while True:
        try:
            S = sell()
            a = input()
            S.dostring(a)
        except:break