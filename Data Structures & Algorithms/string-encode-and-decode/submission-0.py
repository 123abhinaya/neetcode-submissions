class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i   # add '#' separator after length
        return s                         # don't decode here, just return encoded string

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':           # find where length ends
                j += 1
            n = int(s[i:j])              # convert length to integer
            word = s[j+1 : j+1+n]        # extract the word of that length
            arr.append(word)
            i = j + 1 + n                # move to next encoded word
        return arr

