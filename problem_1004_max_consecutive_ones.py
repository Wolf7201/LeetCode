"""
Given an array of integers nums and an integer k, return
the number of contiguous subarrays where the product of
all the elements in the subarray is strictly less than k.

Учитывая массив целых чисел nums и целое число k, верните
количество смежных подмассивов, где произведение всех
элементов в подмассиве строго меньше k.
"""

from typing import List

TOPICS = ('Array', 'Binary Search', 'Sliding Window', 'Prefix Sum')


class Solution:
    """
    Задача решена методом скользящего окна, поскольку отдельные элементы
    подмассива, произведение которых меньше обозначенного числа, по
    отдельности также дробятся на подмассивы при итерации цикла мы
    прибавляем количество элементов подмассива к ответу.

    Алгоритмическая сложность O(n), так как мы один раз проходимся циклом
    по входным данным, а цикл while работает за O(1), потому что только
    двигает указатель пока окно не будет удовлетворять заданному числу.

    Пространственная сложность O(1) — константной, так как не требуется
    дополнительная память, которая бы увеличивалась в зависимости от
    размера входного списка nums. Все необходимые переменные занимают
    константное пространство.

    Runtime 497ms Beats 64.87, Memory 16.87MB Beats 96.86%
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


def test_case1():
    solution = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    expected = 6
    assert (solution.longestOnes(nums, k) == expected,
            f"Test case 1 failed: expected {expected}, "
            f"got {solution.longestOnes(nums, k)}")


def test_case2():
    solution = Solution()
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    expected = 10
    assert (solution.longestOnes(nums, k) == expected,
            f"Test case 2 failed: expected {expected}, "
            f"got {solution.longestOnes(nums, k)}")


if __name__ == '__main__':
    test_case1()
    test_case2()
    print("All test cases passed.")
