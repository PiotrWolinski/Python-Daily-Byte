def first_unique_character(s: str) -> int:
    if not s:
        return -1

    letters = {}

    for i in s:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1

    for i in range(len(s)):
        if letters[s[i]] > 1:
            continue
    
        return i

    return -1

assert first_unique_character("abcabd") == 2
assert first_unique_character("thedailybyte") == 1
assert first_unique_character("developer") == 0
