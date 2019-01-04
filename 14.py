# 动态规划
# def cutLine(length):
#     if length == 1:
#         return 0
#     if length == 2:
#         return 1
#     if length ==3:
#         return 2
#     maxv = [0 for _ in range(length+1)]
#     maxv[0] = 0
#     maxv[1] = 1
#     maxv[2] = 2
#     maxv[3] = 3
#     leng = length
#     for i in range(4,length+1):
#         maxvalue=0
#         for j in range(1,i//2+1):
#             tempv = maxv[j] * maxv[i-j]
#             if tempv > maxvalue:
#                 maxvalue = tempv
#             maxv[i] = maxvalue
#     return maxv[-1]

# 贪婪算法
def cutLine(length):
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length ==3:
        return 2
    if length %3 ==0:
        return 3**(length//3)
    elif length%3 == 1:
        return 3**(length//3 -1)*4
    else:
        return 3**(length//3)*2
print(cutLine(8))
