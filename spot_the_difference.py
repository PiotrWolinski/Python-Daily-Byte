def spot(s: str, t: str) -> str:

    letters = []
    letters_set = set()
    
    for i in s:
        letters_set.add(i)

    for i in t:
        letters.append(i)

    for i in t:
        if i in letters_set:
            letters.remove(i)

    if len(letters):
        return letters[0]

    return ''



assert spot(s = "foobar", t = "barfoot") == 't'
assert spot(s = "ide", t = "idea") == 'a'
assert spot(s = "coding", t = "ingcod") == ''