class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        nums = sorted(set(nums))
        for num in nums:
            if num < missing:
                continue
            elif num == missing:
                missing += 1
            elif num != missing:
                return missing 
        else:
            return missing 