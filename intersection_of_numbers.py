def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    arr = []
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    for i in nums1_set:
        if i in nums2_set:
            arr.append(i)

    return arr

assert intersection(nums1 = [2, 4, 4, 2], nums2 = [2, 4]) == [2, 4]
assert intersection(nums1 = [1, 2, 3, 3], nums2 = [3, 3]) == [3]
assert intersection(nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7]) == []