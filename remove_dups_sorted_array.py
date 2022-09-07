class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,length = 1,len(nums)
        for j in range(1,length):
            if nums[i-1]!=nums[j]:
                nums[i] = nums[j]
                i+=1
        return i
