# -*- coding: utf-8 -*-

from collections import defaultdict
import traceback
 
def get_error_key(string):
    file_info = string.strip().split('\\')[-1].split()
    # print(file_info)
    file_name, err_no = file_info[0], file_info[1]
    file_name = file_name[-16:]
    key = file_name + ' ' + err_no
    return key
 
def main():
    records = dict()
    lists = []
    while True:
        try:
 
            strings = input().split(' \r\n')
            for string in strings:
                key = get_error_key(string)
                if key in records:
                    records[key] += 1
                else:
                    records[key] = 1
                    lists.append(key)
        except Exception as e:
            # traceback.print_exc()
            break
    # print(lists[-8:])
    # print(records)
    rets = []
    for key in lists[-8:]:
        ret = '{key} {num}'.format(key=key, num=records[key])
        #rets.append(ret)
        print(ret)
    #print(' '.join(rets))
 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
    
    
    