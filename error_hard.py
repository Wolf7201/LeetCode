from typing import List


class Solution:
    def get_list(self, word, prefix):
        new_prefix = []

        for i in range(len(prefix)):
            m = len(word)
            n = len(prefix[i])
            new_prefix.extend(
                prefix[i] for j in range(m - n + 1) if word[j: j + n] == prefix[i]
            )
        return new_prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]

        str1 = strs[0]
        str2 = strs[1]
        len_pref = min(len(str1), len(str2))
        prefix = []
        for i in range(len_pref, 0, -1):
            prefix.extend(str1[j:j + i] for j in range(len(str1) - i + 1))

        for i in range(1, len(strs)):
            prefix = self.get_list(strs[i], prefix)

        return prefix[0] if prefix else ''



str1 = ['']

sol = Solution()

print(sol.longestCommonPrefix(str1))
