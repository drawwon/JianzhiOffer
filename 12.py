# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(path) > len(matrix) or len(matrix)==0:
            return False
        # write code here
        visited = [[False for i in range(cols)] for j in range(rows)]
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(row, col, matrix, rows, cols, path, visited, pathLength):
                    return True
        return False

    def hasPathCore(self, row, col, matrix, rows, cols, path, visited, pathLength):
        if pathLength == len(path):
            return True
        haspath = False
        if col < cols and row < rows and path[pathLength] == matrix[row*cols+col] and not visited[row][col]:
            pathLength += 1
            visited[row][col] = True
            haspath = self.hasPathCore(row + 1, col, matrix, rows, cols, path, visited, pathLength) or \
                      self.hasPathCore(row - 1, col, matrix, rows, cols, path, visited, pathLength) or \
                      self.hasPathCore(row, col + 1, matrix, rows, cols, path, visited, pathLength) or \
                      self.hasPathCore(row, col - 1, matrix, rows, cols, path, visited, pathLength)
            if not haspath:
                pathLength -= 1
                visited[row][col] = False
        return haspath
