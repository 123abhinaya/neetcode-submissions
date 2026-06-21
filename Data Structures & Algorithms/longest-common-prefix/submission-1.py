class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = min(len(i) for i in strs)
        pre = ""
        for i in range(min_length):
            current = strs[0][i]
            for s in strs:
                if s[i] != current:
                    return pre
            pre += current
        return pre