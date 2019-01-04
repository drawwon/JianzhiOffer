def partion(nums,l,r):
    x = nums[r]
    s = l - 1
    for i in range(l,r):
        if nums[i] <= x:
            s+=1
            nums[i], nums[s] = nums[s], nums[i]
    s += 1
    nums[s], nums[r] = nums[r], nums[s]
    return s

def quicksort(nums,l,r):
    if l < r:
        q = partion(nums, l ,r)
        quicksort(nums, l, q-1)
        quicksort(nums, q+1,r)

arrays = [1,2,4,5,6,3]
quicksort(arrays,0,len(arrays)-1)
print(arrays)