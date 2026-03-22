class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        
        if len(nums) <= 1:
            return True

        for i, v in enumerate(nums):
            
            if i > far:
                return False
            
            far = max(far, i + v)
            
            if far >= len(nums) - 1:
                return True
        
        return True