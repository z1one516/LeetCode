class Solution:
    def twoSum(self, nums, target):
        answer = []
        for idx,i in enumerate(nums):
            for idx_2, j in enumerate(nums[idx+1:]):
                if i+j == target:
                    answer = [idx, idx+1+idx_2]
        return answer
    
    def  twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i