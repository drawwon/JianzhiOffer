# # # # # # # # # # # n=5
# # # # # # # # # # # count=0
# # # # # # # # # # # while n:
# # # # # # # # # # #     n = n & (n - 1)
# # # # # # # # # # #     count += 1
# # # # # # # # # # # print(count)
# # # # # # # # # # class ListNode:
# # # # # # # # # #     def __init__(self, x):
# # # # # # # # # #         self.val = x
# # # # # # # # # #         self.next = None
# # # # # # # # # # class Solution:
# # # # # # # # # #     # 返回合并后列表
# # # # # # # # # #     def Merge(self, pHead1, pHead2):
# # # # # # # # # #         # write code here
# # # # # # # # # # #递归方法
# # # # # # # # # #         # if not pHead1:
# # # # # # # # # #         #     return pHead2
# # # # # # # # # #         # if not pHead2:
# # # # # # # # # #         #     return pHead1
# # # # # # # # # #         # if pHead1.val <= pHead2.val:
# # # # # # # # # #         #     pHead1.next = self.Merge(pHead1.next,pHead2)
# # # # # # # # # #         #     return pHead1
# # # # # # # # # #         # else:
# # # # # # # # # #         #     pHead2.next = self.Merge(pHead1,pHead2.next)
# # # # # # # # # #         #     return pHead2
# # # # # # # # # # # 非递归方法
# # # # # # # # # #         head = ListNode(0)
# # # # # # # # # #         node = head
# # # # # # # # # #         while pHead1 and pHead2:
# # # # # # # # # #             if pHead1.val <= pHead2.val:
# # # # # # # # # #                 head.next = pHead1
# # # # # # # # # #                 head = head.next
# # # # # # # # # #                 pHead1 = pHead1.next
# # # # # # # # # #             else:
# # # # # # # # # #                 head.next = pHead2
# # # # # # # # # #                 head = head.next
# # # # # # # # # #                 pHead2 = pHead2.next
# # # # # # # # # #         if pHead1:
# # # # # # # # # #             head.next = pHead1
# # # # # # # # # #         if pHead2:
# # # # # # # # # #             head.next = pHead2
# # # # # # # # # #         return node.next
# # # # # # # # # # s = Solution()
# # # # # # # # # # list1 = ListNode(1)
# # # # # # # # # # list1.next = ListNode(3)
# # # # # # # # # # list1.next.next = ListNode(5)
# # # # # # # # # #
# # # # # # # # # # list2 = ListNode(2)
# # # # # # # # # # list2.next = ListNode(4)
# # # # # # # # # # list2.next.next = ListNode(6)
# # # # # # # # # #
# # # # # # # # # # a= s.Merge(list1,list2)
# # # # # # # # # # while a:
# # # # # # # # # #     print(a.val)
# # # # # # # # # #     a = a.next
# # # # # # # # # # -*- coding:utf-8 -*-
# # # # # # # # # class Solution:
# # # # # # # # #     def reOrderArray(self, array):
# # # # # # # # #         # write code here
# # # # # # # # #         # if not array:
# # # # # # # # #         #     return None
# # # # # # # # #         result_odd = []
# # # # # # # # #         result_even = []
# # # # # # # # #         for i in array:
# # # # # # # # #             if i%2!=0:
# # # # # # # # #                 result_odd.append(i)
# # # # # # # # #             else:
# # # # # # # # #                 result_even.append(i)
# # # # # # # # #         result_odd.extend(result_even)
# # # # # # # # #         return result_odd
# # # # # # # # # s = Solution()
# # # # # # # # # s.reOrderArray([])
# # # # # # # # # -*- coding:utf-8 -*-
# # # # # # # # class Solution:
# # # # # # # #     # matrix类型为二维列表，需要返回列表
# # # # # # # #     def printMatrix(self, matrix):
# # # # # # # #         # write code here
# # # # # # # #         if not matrix:
# # # # # # # #             return None
# # # # # # # #         if isinstance(matrix[0],int):
# # # # # # # #             return matrix[0]
# # # # # # # #         if len(matrix[0])==1:
# # # # # # # #             return matrix[0]
# # # # # # # #         rows = len(matrix)
# # # # # # # #         cols = len(matrix[0])
# # # # # # # #         visited = [[0 for i in range(cols)] for j in range(rows)]
# # # # # # # #         col = 0
# # # # # # # #         row = 0
# # # # # # # #         while sum(sum(i) for i in visited) < rows * cols:
# # # # # # # #             if not visited[row][col]:
# # # # # # # #                 print(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while col + 1 < cols and not visited[row][col + 1]:
# # # # # # # #                 col += 1
# # # # # # # #                 print(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while row + 1 < rows and not visited[row + 1][col]:
# # # # # # # #                 row += 1
# # # # # # # #                 print(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while col > 0 and not visited[row][col - 1]:
# # # # # # # #                 col -= 1
# # # # # # # #                 print(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while row > 0 and not visited[row - 1][col]:
# # # # # # # #                 row -= 1
# # # # # # # #                 print(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # # s = Solution()
# # # # # # # # s.printMatrix([[1,2],[3,4]])#[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# # # # # # # # class Solution:
# # # # # # # #     # matrix类型为二维列表，需要返回列表
# # # # # # # #     def printMatrix(self, matrix):
# # # # # # # #         # write code here
# # # # # # # #         if not matrix:
# # # # # # # #             return None
# # # # # # # #         if isinstance(matrix[0],int):
# # # # # # # #             return matrix[0]
# # # # # # # #
# # # # # # # #         rows = len(matrix)
# # # # # # # #         cols = len(matrix[0])
# # # # # # # #         result = []
# # # # # # # #         visited = [[0 for i in range(cols)] for j in range(rows)]
# # # # # # # #         col = 0
# # # # # # # #         row = 0
# # # # # # # #         while sum(sum(i) for i in visited) < rows * cols:
# # # # # # # #             if not visited[row][col]:
# # # # # # # #                 result.append(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while col + 1 < cols and not visited[row][col + 1]:
# # # # # # # #                 col += 1
# # # # # # # #                 result.append(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while row + 1 < rows and not visited[row + 1][col]:
# # # # # # # #                 row += 1
# # # # # # # #                 result.append(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while col > 0 and not visited[row][col - 1]:
# # # # # # # #                 col -= 1
# # # # # # # #                 result.append(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #             while row > 0 and not visited[row - 1][col]:
# # # # # # # #                 row -= 1
# # # # # # # #                 result.append(matrix[row][col])
# # # # # # # #                 visited[row][col] = 1
# # # # # # # #         return result
# # # # # # #
# # # # # # # class Solution:
# # # # # # #     # matrix类型为二维列表，需要返回列表
# # # # # # #     def printMatrix(self, matrix):
# # # # # # #         if not matrix or len(matrix)<=0:
# # # # # # #             return None
# # # # # # #         start=0
# # # # # # #         rows = len(matrix)
# # # # # # #         cols = len(matrix[0])
# # # # # # #         while start*2 < rows and start*2 < cols:
# # # # # # #             self.printCircle(start,rows,cols,matrix)
# # # # # # #             start+=1
# # # # # # #     def printCircle(self, start,rows,cols,matrix):
# # # # # # #         endRow = rows-1-start
# # # # # # #         endCol = cols-1-start
# # # # # # #         for i in range(start,endCol+1):
# # # # # # #             print(matrix[start][i])
# # # # # # #         if endRow>start:
# # # # # # #             for i in range(start+1,endRow+1):
# # # # # # #                 print(matrix[i][endCol])
# # # # # # #         if endRow>start and endCol>start:
# # # # # # #             for i in range(endCol-1,start-1,-1):
# # # # # # #                 print(matrix[endRow][i])
# # # # # # #         if endCol>start and endRow>start+1:
# # # # # # #             for i in range(endRow-1,start,-1):
# # # # # # #                 print(matrix[i][start])
# # # # # # #
# # # # # # # s = Solution()
# # # # # # # s.printMatrix([[1,2],[3,4]])#[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# # # # # # # -*- coding:utf-8 -*-
# # # # # # # class ListNode:
# # # # # # #     def __init__(self, x):
# # # # # # #         self.val = x
# # # # # # #         self.next = None
# # # # # #     class Solution:
# # # # # #         def EntryNodeOfLoop(self, pHead):
# # # # # #             # write code here
# # # # # #             result = []
# # # # # #             while pHead.next:
# # # # # #                 result.append(pHead)
# # # # # #                 pHead = pHead.next
# # # # # #
# # # # # #                 if pHead in result:
# # # # # #                     return pHead
# # # # # #             return None
# # # # #
# # # # # class Solution:
# # # # #     def HasSubtree(self, pRoot1, pRoot2):
# # # # #         # write code here
# # # # #         result = False
# # # # #         if pRoot1 and pRoot2:
# # # # #             if pRoot1.val == pRoot2.val:
# # # # #                 result = self.Tree1HasTree2(pRoot1, pRoot2)
# # # # #             if not result:
# # # # #                 result = self.HasSubtree(pRoot1.left, pRoot2)
# # # # #             if not result:
# # # # #                 result = self.HasSubtree(pRoot1.right, pRoot2)
# # # # #         return result
# # # # #
# # # # #     def Tree1HasTree2(self, pRoot1, pRoot2):
# # # # #         if not pRoot2:
# # # # #             return True
# # # # #         if not pRoot1:
# # # # #             return False
# # # # #         if pRoot1.val != pRoot2.val:
# # # # #             return False
# # # # #         return self.Tree1HasTree2(pRoot1.left, pRoot2.left) and self.Tree1HasTree2(pRoot1.right, pRoot2.right)
# # # # #
# # # # # s = Solution()
# # # # # class TreeNode:
# # # # #     def __init__(self, x):
# # # # #         self.val = x
# # # # #         self.left = None
# # # # #         self.right = None
# # # # # tree = TreeNode(1)
# # # # # tree.left = TreeNode(2)
# # # # # tree.right = TreeNode(3)
# # # # # tree.left.left = TreeNode(4)
# # # # # tree.left.right = TreeNode(5)
# # # # # tree.right.left = TreeNode(6)
# # # # # tree.right.right = TreeNode(7)
# # # # #
# # # # # tree.left.left.left = TreeNode(8)
# # # # # tree.left.left.right = TreeNode(9)
# # # # # tree.left.right.left = TreeNode(10)
# # # # # tree.left.right.right = TreeNode(11)
# # # # # tree.right.left.left = TreeNode(12)
# # # # # tree.right.left.right = TreeNode(13)
# # # # # tree.right.right.left = TreeNode(14)
# # # # # tree.right.right.right = TreeNode(15)
# # # # #
# # # # # tree2 = TreeNode(8)
# # # # # tree2.left = TreeNode(9)
# # # # # tree2.right = TreeNode(2)
# # # # # def pre(tree):
# # # # #     if not tree:
# # # # #         return
# # # # #
# # # # #     pre(tree.left)
# # # # #     pre(tree.right)
# # # # #     return tree.val
# # # # #
# # # # # def layer(tree):
# # # # #     array = [tree]
# # # # #     while array:
# # # # #         node = array[0]
# # # # #         array.remove(array[0])
# # # # #         print(node.val)
# # # # #         if node.left:
# # # # #             array.append(node.left)
# # # # #         if node.right:
# # # # #             array.append(node.right)
# # # # #
# # # # # # layer(tree)
# # # # # # print(s.HasSubtree(tree,tree2))
# # # # # class Solution:
# # # # #     # 返回从上到下每个节点值列表，例：[1,2,3]
# # # # #     def PrintFromTopToBottom(self, root):
# # # # #         # write code here
# # # # #         if not root:
# # # # #             return []
# # # # #         queue = [[],[]]
# # # # #         layer = 0
# # # # #         queue[layer].append(root)
# # # # #         while queue[0] or queue[1]:
# # # # #             node = queue[layer].pop()
# # # # #             if layer:
# # # # #                 if node.right:
# # # # #                     queue[1-layer].append(node.right)
# # # # #                 if node.left:
# # # # #                     queue[1-layer].append(node.left)
# # # # #             else:
# # # # #                 if node.left:
# # # # #                     queue[1-layer].append(node.left)
# # # # #                 if node.right:
# # # # #                     queue[1-layer].append(node.right)
# # # # #             print(node.val,end=' ')
# # # # #             if not queue[layer]:
# # # # #                 print('\n')
# # # # #                 layer = 1-layer
# # # # # s = Solution()
# # # # # s.PrintFromTopToBottom(tree)
# # # #
# # # # n = int(input())
# # # # nums = []
# # # # for i in range(n-1):
# # # #     nums.append(input().split())
# # # # tree = {'0':[1,1]}
# # # # fathers = []
# # # # for num in nums:
# # # #     father = num[0]
# # # #     if father not in tree.keys():
# # # #         tree[father][1] = 1
# # # #     else:
# # # #         tree[father][1] += 1
# # # #         if tree[father][1] == 2:
# # # #             tree[father][0] += 1
# # # # print(max([i for i in tree.values()]))
# # # words = input().split()
# # # print(' '.join(words[::-1]))
# #
# # n = int(input())
# # words = []
# # for i in range(n):
# #     words.append(input())
# #
# # for word in words:
# #     count = {}
# #     result = []
# #     for w in word:
# #         if w in count.keys():
# #             count[w] += 1
# #         else:
# #             count[w] = 1
# #     if 'G' in count.keys():
# #         while count['G'] > 0:
# #             count['G'] -= 1
# #             count['E'] -= 1
# #             count['I'] -= 1
# #             count['H'] -= 1
# #             count['T'] -= 1
# #             result.append('0')
# #     if 'Z' in count.keys():
# #         while count['Z'] > 0:
# #             count['Z'] -= 1
# #             count['E'] -= 1
# #             count['R'] -= 1
# #             count['O'] -= 1
# #             result.append('2')
# #     if 'W' in count.keys():
# #         while count['W'] > 0:
# #             count['T'] -= 1
# #             count['W'] -= 1
# #             count['O'] -= 1
# #             result.append('4')
# #     if 'U' in count.keys():
# #         while count['U'] > 0:
# #             count['F'] -= 1
# #             count['O'] -= 1
# #             count['U'] -= 1
# #             count['R'] -= 1
# #             result.append('6')
# #     if 'X' in count.keys():
# #         while count['X'] > 0:
# #             count['S'] -= 1
# #             count['I'] -= 1
# #             count['X'] -= 1
# #             result.append('8')
# #     if 'O' in count.keys():
# #         while count['O'] > 0:
# #             count['O'] -= 1
# #             count['N'] -= 1
# #             count['E'] -= 1
# #             result.append('3')
# #     if 'T' in count.keys():
# #         while count['T'] > 0:
# #             count['T'] -= 1
# #             count['H'] -= 1
# #             count['R'] -= 1
# #             count['E'] -= 1
# #             count['E'] -= 1
# #             result.append('5')
# #     if 'F' in count.keys():
# #         while count['F'] > 0:
# #             count['F'] -= 1
# #             count['I'] -= 1
# #             count['V'] -= 1
# #             count['E'] -= 1
# #             result.append('7')
# #     if 'S' in count.keys():
# #         while count['S'] > 0:
# #             count['S'] -= 1
# #             count['E'] -= 1
# #             count['V'] -= 1
# #             count['E'] -= 1
# #             count['N'] -= 1
# #             result.append('9')
# #     if 'N' in count.keys():
# #         while count['N'] > 0:
# #             count['N'] -= 1
# #             count['I'] -= 1
# #             count['N'] -= 1
# #             count['E'] -= 1
# #             result.append('1')
# #
# #     result = sorted(result)
# #     print(''.join(result))
#
#
# def isShui(num):
#     cube = 0
#     for i in str(num):
#         cube+=int(i)**3
#     if cube == num:
#         return True
#     else:
#         return False
#
#
# while True:
#     try:
#         nums = list(map(int,input().split()))
#         result = []
#         start,end = nums[0], nums[1]
#         for i in range(start,end+1):
#             if isShui(i):
#                 result.append(i)
#         if not result:
#             print('no')
#         else:
#             for i in range(len(result)):
#                 print(result[i],end=' ')
#             print(result[-1])
#     except:
#         break


# number = 22265#int(input())
# cnt = 2#int(input())

number = input()
cnt = int(input())
left = len(number) - cnt
number_list = list(number)


def getMax(number_list, cnt):
    flag = 0
    while flag < cnt:
        i = 0
        while i < len(number_list) - 1:
            if number_list[i] < number_list[i + 1]:
                flag += 1
                number_list.pop(i)
                if flag == cnt:
                    return
            i += 1


getMax(number_list, cnt)
print(''.join(number_list[:left]))
