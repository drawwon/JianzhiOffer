# def getOneNum(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     count = 0
#     num = bin(num)
#     return sum(1 for i in str(num) if i=='1')
#
# print(getOneNum(2))

# def countNum(num):
#     count = 0
#     flag = 1
#     while flag!=2**64:
#         if num & flag:
#             count+=1
#         flag = flag << 1
#     return count

# def countNum(num):
#     count = 0
#     while num:
#         count+=1
#         num=(num-1)&num
#     return count
#
# print(countNum(4))

