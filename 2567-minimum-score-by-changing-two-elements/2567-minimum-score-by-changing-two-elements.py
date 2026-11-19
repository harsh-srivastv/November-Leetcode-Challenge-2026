class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        # change the two from the left
        res1 = nums[-1] - nums[2]
        # change the two from the right
        res2 = nums[-3] - nums[0]
        # change one from each
        res3 = nums[-2] - nums[1]
        return min(res1, res2, res3)