def correct_capitalization(string: str) -> bool:
    letters_capitalized = 0
    for letter in string:
        if letter.isupper():
            letters_capitalized += 1
    
    if letters_capitalized == len(string) or letters_capitalized == 0:
        return True
    
    if string[0].isupper():
        return True

    return False

assert correct_capitalization('USA') == True

assert correct_capitalization('Calvin') == True

assert correct_capitalization('compUter') == False

assert correct_capitalization('coding') == True