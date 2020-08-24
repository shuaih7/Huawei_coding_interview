from collections import Counter

if __name__ == "__main__":
    while True:
        try:
            # 测试用例中的用例，参数是两行。而提交的代码跑的用例是一行。这点需要注意！
            string, len_defined = input().strip().split()
            len_total = 0
            rst = ''
            for i in list(string):
                # 网站的Python环境，默认编码是UTF-8，这样一个汉字占用三个字节。
                # 而题目的意思应该默认编码是gbk，一个汉字占用两个字节。
                # 因此，为了保险起见，在代码中应特别指明encode的方式。
                len_total += len(i.encode('gbk'))
                if len_total <= int(len_defined):
                    rst += i
            print(rst)
     
        except:
            break