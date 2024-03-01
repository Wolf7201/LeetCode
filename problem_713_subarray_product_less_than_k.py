"""
Given an array of integers nums and an integer k, return
the number of contiguous subarrays where the product of
all the elements in the subarray is strictly less than k.

Учитывая массив целых чисел nums и целое число k, верните
количество смежных подмассивов, где произведение всех
элементов в подмассиве строго меньше k.
"""

from typing import List

TOPICS = ('Array', 'Sliding Window')


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

    Runtime 553ms Beats 97.23, Memory 19.27MB Beats 89.40%
    """
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = ans = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans


def test_case1():
    solution = Solution()
    nums = [10, 5, 2, 6]
    k = 100
    expected = 8
    assert (solution.numSubarrayProductLessThanK(nums, k) == expected,
            f"Test case 1 failed: expected {expected}, "
            f"got {solution.numSubarrayProductLessThanK(nums, k)}")


def test_case2():
    solution = Solution()
    nums = [1, 2, 3]
    k = 0
    expected = 0
    assert (solution.numSubarrayProductLessThanK(nums, k) == expected,
            f"Test case 2 failed: expected {expected}, "
            f"got {solution.numSubarrayProductLessThanK(nums, k)}")


if __name__ == '__main__':
    test_case1()
    test_case2()
    print("All test cases passed.")
