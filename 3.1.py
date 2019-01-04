# 方法1
# 用O(n)的辅助数组
# def get_duplicate_num(l):
#     l1 = [0 for _ in range(len(l))]
#     for i in l:
#         l1[i] += 1
#         if l1[i] > 1:
#             return i
#     return False


# 方法2： 二分查找
def get_duplicate_num(l):
    start = 1
    end = len(l)-1
    while start <= end:
        middle = (end-start)/2 + start
        if middle %1 !=0:
            middle = int(middle) + 1
        else:
            middle = int(middle)
        count = computeCount(l,start,middle)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return False

def computeCount(l,start,end):
    count = 0
    for i in l:
        if start <= i <= end:
            count += 1
    return count

if __name__ == '__main__':
    print(get_duplicate_num([2,3,5,4,2,6,7]))
