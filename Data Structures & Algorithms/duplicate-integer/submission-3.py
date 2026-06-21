from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       s = Counter(nums)
       for i,j in s.items():
        if j > 1:
            return True
       return False