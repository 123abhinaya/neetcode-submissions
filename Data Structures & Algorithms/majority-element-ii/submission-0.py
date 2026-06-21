from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        n = len(nums)//3
        res = []
        for i,j in s.items():
            if j > n:
                res.append(i)
        return res
