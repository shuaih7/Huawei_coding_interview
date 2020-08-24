# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None
 
class SingleLinkList(object):
    def __init__(self,node=None):
        self._head = node
 
    def length(self):
        cur = self._head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count
 
    def travel(self):
        cur = self._head
        while cur:
            print(cur.elem, end = " ")
            cur = cur.next
        print("")
 
    def add(self,item):
        node = Node(item)
        node.next = self._head
        self._head = node
 
    def insert(self,item,index):
        node = Node(item)
        if not self._head:
            self._head = node
        else:
            cur = self._head
            count = 0
            while cur:
                if cur.elem == index:
                    node.next = cur.next
                    cur.next = node
                    break
                else:
                    cur = cur.next
 
    def remove(self,item):
        node = Node(item)
        cur = self._head
        pre = None
        while cur:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    while True:
        try:
            ll = SingleLinkList()
            a = list(map(int,input().split()))
            n = a[0]
            ll.add(a[1])
            for i in range(n-1):
                c = a[2+i*2]
                d = a[3+i*2]
                ll.insert(c,d)
            ll.remove(a[-1])
            ll.travel()
        except:
            break