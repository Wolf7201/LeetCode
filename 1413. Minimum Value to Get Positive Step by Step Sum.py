"""
Given an array of integers nums, you start with an initial positive
value startValue. In each iteration, you calculate the step by step
sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step
by step sum is never less than 1.

Учитывая массив целых чисел nums, вы начинаете с начального
 положительного значения startValue.

На каждой итерации вы вычисляете пошаговую сумму startValue
 плюс элементы в nums (слева направо).

Возвращает минимальное положительное значение startValue таким
образом, чтобы пошаговая сумма никогда не была меньше 1.
"""

from typing import List

TOPICS = ('Array', 'Sliding Window')


class Solution:
    """
    Задача решена префиксным методом.

    Алгоритмическая сложность O(n), так как мы один раз проходимся циклом
    по входным данным от 0 до k, а цикл вторым циклом от k до конца массива.

    Пространственная сложность O(1) — константной, так как не требуется
    дополнительная память, которая бы увеличивалась в зависимости от
    размера входного списка nums. Все необходимые переменные занимают
    константное пространство.

    Runtime 992ms Beats 83.75%, Memory 27.91MB Beats 53.14%%
    """

    @staticmethod
    def min_start_value(nums: List[int]) -> int:
        prefix = [nums[0]]
        prefix.extend(nums[i] + prefix[-1] for i in range(1, len(nums)))
        min_prefix = min(prefix)

        return abs(min_prefix) + 1 if min_prefix <= 0 else 1

    @staticmethod
    def min_start_value2(nums: List[int]) -> int:
        min_num = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] < min_num:
                min_num = nums[i]

        return abs(min_num) + 1 if min_num <= 0 else 1


def test_case1():
    solution = Solution()
    nums = [-3, 2, -3, 4, 2]
    expected = 5
    assert solution.min_start_value(nums) == expected, \
        f"Test case 1 failed: expected {expected}, got {solution.min_start_value(nums)}"


def test_case2():
    solution = Solution()
    nums = [1, 2]
    expected = 1
    assert solution.min_start_value(nums) == expected, \
        f"Test case 2 failed: expected {expected}, got {solution.min_start_value(nums)}"


def test_case3():
    solution = Solution()
    nums = [1, -2, -3]
    expected = 5
    assert solution.min_start_value(nums) == expected, \
        f"Test case 3 failed: expected {expected}, got {solution.min_start_value(nums)}"


def test_case4():
    solution = Solution()
    nums = [2, 3, 5, -5, -1]
    expected = 1
    assert solution.min_start_value(nums) == expected, \
        f"Test case 4 failed: expected {expected}, got {solution.min_start_value(nums)}"


if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    print("All test cases passed.")
