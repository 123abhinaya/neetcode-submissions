class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        nums = list(set(nums))
        nums.sort()
        for num in nums:
            if num < missing:
                continue
            elif num == missing:
                missing += 1
            elif num != missing:
                return missing 
        else:
            return missing 