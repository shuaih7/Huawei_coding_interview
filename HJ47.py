def insertK(original_list):
    res = []
    key = -1
    value = -1
    for i in range(len(original_list)):
        if i == 0:
            res.append(original_list[i])
            key,value = original_list[i][0],original_list[i][1]
        else:
            if original_list[i][0] == original_list[i-1][0]:
                continue
            elif original_list[i][0] < original_list[i-1][0]:
                res.append(original_list[i])
                key,value = original_list[i][0],original_list[i][1]
            else:
                if original_list[i][0] == key + 1:
                    res.append(original_list[i])
                    key,value = original_list[i][0],original_list[i][1]
                else:
                    temp = []
                    diff = original_list[i][0] - key
                    for j in range(diff-1):
                        pair_key = key + (j+1)
                        pair_value = value + int((original_list[i][1]-value)/(original_list[i][0]-key)) * (j+1)
                        temp.append([pair_key,pair_value])
                    res += temp
                    res.append(original_list[i])
                    key,value = original_list[i][0],original_list[i][1]
    for pair in res:
        print(pair[0],pair[1])


if __name__ == "__main__":
    while True:
        try:
            n,m = map(int,input().split())
            original_list = []
            for i in range(n):
                key,value = map(int,input().split())
                temp = [key,value]
                original_list.append(temp)
            insertK(original_list)
        except:
            break