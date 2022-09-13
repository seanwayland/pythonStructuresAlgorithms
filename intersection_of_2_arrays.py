class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # use counter for each array 
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        print(c1)
        print(c2)
        
        # if its in both return the lowest value 
        result = []
        for x in c1:
            key = x
            value = c1[key]
            if c2[key]:
                result.extend([key for i in range(min(value, c2[key]))])
        return result
