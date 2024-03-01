from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


arr = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
sol = Solution()
print(sol.maximumWealth(arr))
