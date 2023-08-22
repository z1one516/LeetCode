class Solution:
    def searchInsert(self, nums, target) :
        for idx, val in enumerate(nums):
            answer  = 0
            if val >= target:
                answer = idx
                break
            else:
                answer = (idx+1)
        return answer
        