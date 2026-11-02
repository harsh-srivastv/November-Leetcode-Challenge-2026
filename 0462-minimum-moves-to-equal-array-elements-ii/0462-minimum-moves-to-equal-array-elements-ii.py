class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        median = nums[len(nums)//2]
        
        for i in nums:
            ans += abs(median - i)
            
        return ans
        