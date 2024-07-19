def task_1(arr, n):
    k = 7
    res = -1
    left = five_count = 0

    if n < 7:
        return res

    for right in range(len(arr)):
        if arr[right] == 3:
            left = right + 1
            five_count = 0
        elif arr[right] == 5:
            five_count += 1

        if right - left + 1 == k:
            res = max(res, five_count)
            left += 1
    return res


n = int(input())
m = list(map(int, input().split()))

print(task_1(m, n))
