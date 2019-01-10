class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.verifyCore(sequence)

    def verifyCore(self, sequence):
        i = 0
        while sequence[i] < sequence[-1]:
            i += 1
        for j in range(i, len(sequence)):
            if sequence[j] < sequence[-1]:
                return False
        left = True
        if i > 0:
            left = self.verifyCore(sequence[:i])
        right = True
        if i < len(sequence) - 1:
            right = self.verifyCore(sequence[i:-1])
        return left and right


s = Solution()
a = s.VerifySquenceOfBST([7, 4, 6, 5])
print(a)
