class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # left half sorted
                if nums[mid] > target:   # target small
                    if nums[left] > target: # target very small, is in right half
                        left = mid + 1
                    else:                   # target not that small
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            else:                       # right half sorted
                if nums[mid] > target: 
                    right = mid - 1
                elif nums[mid] < target:     # target big
                    if nums[right] < target: # target very big, is in left half
                        right = mid - 1
                    else:                   # target not that big
                        left = mid + 1
        return -1