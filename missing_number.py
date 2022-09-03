class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # mydict = {}
        # for i in range(len(nums)+1):
        #     mydict[i] = 0
        # print(mydict)
        # for i in range(len(nums)):
        #     mydict[nums[i]]=1
        # print(mydict)
        # result = (list(mydict.keys())[list(mydict.values()).index(0)]) 
        # #print(result)
        # return result
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i]!=i:
        #         return i
        # return(len(nums))
        sum_range = 0
        sum_nums = 0
        for i in range(len(nums) + 1):
            sum_range = sum_range + i
        for i in range(len(nums)):
            sum_nums = sum_nums + nums[i]
        return sum_range - sum_nums
