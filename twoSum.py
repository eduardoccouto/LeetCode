class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int

        """
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        return [i, j]
        
        


