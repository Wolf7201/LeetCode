"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error
less than 10-5 will be accepted.

Задан целочисленный массив num, состоящий из элементов, и целое число k.

Найдите непрерывный подмассив, длина которого равна k и который имеет
максимальное среднее значение, и верните это значение. Будет принят
любой ответ с ошибкой расчета менее 10^-5.
"""

from typing import List

TOPICS = ('Array', 'Sliding Window')


class Solution:
    """
    Задача решена методом статического скользящего окна.

    Алгоритмическая сложность O(n), так как мы один раз проходимся циклом
    по входным данным от 0 до k, а цикл вторым циклом от k до конца массива.

    Пространственная сложность O(1) — константной, так как не требуется
    дополнительная память, которая бы увеличивалась в зависимости от
    размера входного списка nums. Все необходимые переменные занимают
    константное пространство.

    Runtime 992ms Beats 83.75%, Memory 27.91MB Beats 53.14%%
    """

    def findMaxAverage(self, nums: List[int], k: int) -> int:
        subarray_sum = sum(nums[:k])

        max_sum = subarray_sum
        for i in range(k, len(nums)):
            subarray_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, subarray_sum)

        max_average = max_sum / k
        return round(max_average, 5)


def test_case1():
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected = 12.75000
    assert (solution.findMaxAverage(nums, k) == expected,
            f"Test case 1 failed: expected {expected}, "
            f"got {solution.findMaxAverage(nums, k)}")


def test_case2():
    solution = Solution()
    nums = [5]
    k = 1
    expected = 5.00000
    assert (solution.findMaxAverage(nums, k) == expected,
            f"Test case 2 failed: expected {expected}, "
            f"got {solution.findMaxAverage(nums, k)}")


if __name__ == '__main__':
    test_case1()
    test_case2()
    print("All test cases passed.")
