# # -*- coding:utf-8 -*-
# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         count = 0
#         if rows <= 0 or cols <= 0:
#             return 0
#         if threshold == 0:
#             return rows * cols
#         visited = [[False for i in range(cols)] for j in range(rows)]
#         count = self.movingCountCore(rows, cols, threshold, 0, 0,visited)
#         return count
#
#     def movingCountCore(self, rows, cols, threshold, row, col, visited):
#         count = 0
#         if 0 <= row < rows and 0<= col < cols and not visited[row][col] and self.checkSum(row, col, threshold):
#             visited[row][col] = True
#             count = 1 + self.movingCountCore(rows, cols, threshold, row + 1, col, visited) + \
#                     self.movingCountCore(rows, cols, threshold, row - 1, col, visited) + \
#                     self.movingCountCore(rows, cols, threshold, row, col + 1, visited) + \
#                     self.movingCountCore(rows, cols, threshold, row, col - 1, visited)
#         return count
#
#     def checkSum(self, row, col, threshold):
#         sumv = 0
#         for i in str(row):
#             sumv += int(i)
#         for j in str(col):
#             sumv += int(j)
#         if sumv <= threshold:
#             return True
#         else:
#             return False
#
# s = Solution()
# print(s.movingCount(10,1,100))

# -*- coding:utf-8 -*-
# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         count = 0
#         if rows <= 0 or cols <= 0:
#             return 0
#         if threshold == 0:
#             return rows * cols
#         count = 0
#         if rows!=1 and cols!=1:
#             for i in range(rows):
#                 for j in range(cols):
#                     if self.checkSum(i,j,threshold):
#                         count += 1
#         if rows==1 or cols == 1:
#             for i in range(rows):
#                 for j in range(cols):
#                     if self.checkSum(i,j,threshold):
#                         count += 1
#                     else:
#                         break
#         return count
#     def checkSum(self,row,col,threshold):
#         val = 0
#         for i in str(row):
#             val+=int(i)
#         for j in str(col):
#             val += int(j)
#         if val <= threshold:
#             return True
#         else:
#             return False
