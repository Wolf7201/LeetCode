nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

i = m - 1
j = n - 1
for cur in range(len(nums1) - 1, m - 2, -1):
    if nums1[i] > nums2[j]:
        val = nums1[i]
        nums1[i] = 0
        nums1[cur] = val
        i -= 1
    else:
        nums1[cur] = nums2[j]
        j -= 1

print(nums1)
