class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr,i = 0,0
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[curr] = nums[i]
                i += 1
                curr += 1
        return curr