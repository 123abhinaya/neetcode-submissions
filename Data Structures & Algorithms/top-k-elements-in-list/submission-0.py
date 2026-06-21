from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        arr = []
        for key,values in d.items():
            heappush(arr,(-values,key))
        res = []
        for i in range(k):
            res.append(heappop(arr)[1])
        return res