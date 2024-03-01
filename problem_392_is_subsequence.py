class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
            j += 1
        return False


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        j = 0
        for letter in t:
            if letter == s[j]:
                j += 1
            if j == len(s):
                return True
        return False


sol = Solution2()
s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))
