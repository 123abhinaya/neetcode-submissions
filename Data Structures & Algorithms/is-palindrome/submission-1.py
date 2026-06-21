class Solution:
    def val (self,c):
            return (ord('A') <= ord(c) <= ord('Z') or
                   ord('a') <= ord(c) <= ord('z') or
                   ord('0') <= ord(c) <= ord('9') )

    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        while i < j:
            while i < j and not self.val(s[i]):
                i += 1
            while i < j and not self.val(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

             