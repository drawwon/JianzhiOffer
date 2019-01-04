def get_duplicate(lists):
    for i in range(len(lists)):
        while lists[i] != i:
            if lists[i] == lists[lists[i]]:
                return True
            a = lists[i]
            lists[i],lists[a] = lists[a], lists[i]
            # break
    return False
    # result = {}
    # for i in lists:
    #     if i not in result.keys():
    #         result[i] = 1
    #     else:
    #         result[i] += 1
    # for key,val in result.items():
    #     if val > 1:
    #         print(key)

if __name__ == '__main__':
    print(get_duplicate([2,3,1,0,2,5,3]))