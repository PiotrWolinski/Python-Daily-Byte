def remove_adjecent(s: str) -> str:
    index = 0
    letters = list(s)

    while index < len(letters) - 1:
        if letters[index + 1] is not None:
            if f'{letters[index]}{letters[index + 1]}' == 2 * letters[index]:
                letters.pop(index)
                letters.pop(index)
                index = 0
                continue
        
        index += 1
        
        if len(letters) == 0:
            break

    return ''.join(letters)


assert remove_adjecent(s = "abccba") == ""
assert remove_adjecent(s = "foobar") == "fbar"
assert remove_adjecent(s = "abccbefggfe") == "a"