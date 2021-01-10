def two_sum(arr: list[int], k: int) -> bool:
    sums = {}

    for i in arr:
        if k - i in sums:
            return True
        else:
            sums[i] = k - i
        
    return False

assert two_sum([1, 3, 8, 2], 10) == True
assert two_sum([3, 9, 13, 7], 8) == False
assert two_sum([4, 2, 6, 5, 2], 4) == True
            