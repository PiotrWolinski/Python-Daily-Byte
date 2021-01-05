def longest_common_prefix(arr: list[str]) -> str:
    shortest_word = arr[0]

    # finding shortest word in O(n)
    for word in arr:
        if len(word) < len(shortest_word):
            shortest_word = word

    arr.remove(shortest_word)

    prefix = ''
    for letter in shortest_word:
        tmp_prefix = prefix
        tmp_prefix += letter
        counter = 0
        for word in arr:
            if word[0:len(tmp_prefix):] == tmp_prefix:
                counter += 1
            else:
                break

        if counter == len(arr):
            prefix = tmp_prefix
        else:
            break

    return prefix


assert longest_common_prefix(["colorado", "color", "cold"]) == 'col'
assert longest_common_prefix(["a", "b", "c"]) == ''
assert longest_common_prefix(["spot", "spotty", "spotted"]) == 'spot'
assert longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
print(longest_common_prefix(["aca", "cba"]))
assert longest_common_prefix(["aca", "cba"]) == ''
