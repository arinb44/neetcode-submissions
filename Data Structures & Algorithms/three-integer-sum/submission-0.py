class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                       # skip repeated first number
            left = i + 1
            right = len(nums) - 1
            goal = -nums[i]
            while left < right:
                total = nums[left] + nums[right]
                if total == goal:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1              # skip repeated second number
                elif total > goal:
                    right -= 1
                else:
                    left += 1
        return results