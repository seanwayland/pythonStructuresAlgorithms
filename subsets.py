class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            print(num)
            # create new arrays and append by adding to each array in current output
            # also keep all arrays in current output 
            output += [curr + [num] for curr in output]
            print(output)
