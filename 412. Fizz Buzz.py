"""
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []
        for i in range(1, n + 1):
            din_3 = i % 3 == 0
            div_5 = i % 5 == 0
            if din_3 and div_5:
                answer.append('FizzBuzz')
            elif din_3:
                answer.append('Fizz')
            elif div_5:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer

    def fizzBuzz2(self, n: int) -> List[str]:
        return [
            'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i)
            for i in range(1, n + 1)
        ]


sol = Solution()

print(sol.fizzBuzz(15))
