def valid_anagram(s: str, t: str) -> bool:
    letters = set()

    for l in s:
        letters.add(l)
    
    for i in t:
        if i not in letters:
            return False
    
    return True

assert valid_anagram(s = "cat", t = "tac") == True
assert valid_anagram(s = "listen", t = "silent") == True
assert valid_anagram(s = "program", t = "function") == False