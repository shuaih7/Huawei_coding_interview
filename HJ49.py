# -*- coding: utf-8 -*-

if __name__ == "__main__":
    while True:
        try:
            import threading
            arr = []
            def add_char(char):
                global arr
                arr.append(char)
            for _ in range(int(input().strip())):
                for i in ['A', 'B', 'C', 'D']:
                    t = threading.Thread(target=add_char, args=(i, ))
                    t.start()
                    t.join()
            print(''.join(arr))
        except:
            break