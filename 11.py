# def findMin(nums,l,r):
#     if len(nums) == 0:
#         return
#     if l >= r:
#         return nums[l]
#     middle =  int((r-l)/2 + l)
#
#     if nums[middle] > nums[l]:
#         minv = findMin(nums, middle+1, r)
#     elif nums[middle] < nums[r]:
#         minv = findMin(nums, l, middle)
#     return minv
#
# print(findMin([3,4,5,1,2],0,4))

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length == 0:
            return 0
        elif length == 1:
            return rotateArray[0]
        else:
            l = 0
            r = length-1
            mid = 0
            while rotateArray[l] >= rotateArray[r]:
                if r - l == 1:
                    return rotateArray[r]
                mid = (r - l)//2 + l

                if rotateArray[mid] >= rotateArray[l]:
                    l = mid
                elif rotateArray[mid] <= rotateArray[r]:
                    r = mid
            return rotateArray[mid]


s = Solution()
print(s.minNumberInRotateArray([1,0,1,1,1,1]))



