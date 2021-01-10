def find_jewels(jewels: str, stones: str) -> int:
    amount = 0

    jewels_set = set()

    for i in jewels:
        jewels_set.add(i)

    for i in stones:
        if i in jewels_set:
            amount += 1

    return amount

assert find_jewels(jewels = "abc", stones = "ac") == 2
assert find_jewels(jewels = "Af", stones = "AaaddfFf") == 3
assert find_jewels(jewels = "AYOPD", stones = "ayopd") == 0