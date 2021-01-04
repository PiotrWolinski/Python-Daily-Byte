def valid_palindrome(string: str) -> bool:
    return string == string[::-1]

print(valid_palindrome('level'))