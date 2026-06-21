from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       s = set(nums)
       return len(nums) != len(s)