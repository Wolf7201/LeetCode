class Solution:
    """
    Учитывая массив натуральных чисел nums и целое число k,
    найдите длину самого длинного подмассива, сумма которого
    меньше или равна k.

    Алгоритмическая сложность O(n)
    Пространственная сложность O(1)

    """

    def find_length(self, nums, k):
        # curr is the current sum of the window
        left = curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans


def test_case1():
    solution = Solution()
    nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    k = 8
    expected = 4
    assert (solution.find_length(nums, k) == expected,
            f"Test case 1 failed: expected {expected}, "
            f"got {solution.find_length(nums, k)}")


class Solution2:
    """
    Вам выдается двоичная строка s (строка, содержащая только "0" и "1").
    Вы можете выбрать до единицы "0" и переключить ее на "1". Какова длина
    самой длинной достижимой подстроки, которая содержит только "1"?

    Например, заданный s = "1101100111"ответ 5. Если вы выполните переворот
    по индексу 2, строка станет 1111100111

    Алгоритмическая сложность O(n)
    Пространственная сложность O(1)
    """

    def find_length(self, s):
        # curr is the current number of zeros in the window
        left = curr = ans = 0
        for right in range(len(s)):
            if s[right] == "0":
                curr += 1
            while curr > 1:
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


def test_case2():
    solution = Solution2()
    s = "1101100111"
    expected = 5
    assert (solution.find_length(s) == expected,
            f"Test case 2 failed: expected {expected}, "
            f"got {solution.find_length(s)}")


class Solution3:
    """
    Учитывая целочисленный массив nums и целое число k, найдите сумму
    подмассива с наибольшей суммой, длина которой равна k.

    Используется метод статического скользящего окна

    Алгоритмическая сложность O(n)
    Пространственная сложность O(1)
    """

    def find_best_subarray(self, nums, k):
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans


def test_case3():
    solution = Solution3()
    nums = [3, -1, 4, 12, -8, 5, 6]
    k = 4
    expected = 15
    assert (solution.find_best_subarray(nums, k) == expected,
            f"Test case 3 failed: expected {expected}, "
            f"got {solution.find_best_subarray(nums, k)}")


if __name__ == '__main__':
    test_case1()
    test_case2()
    test_case3()
    print("All test cases passed.")
