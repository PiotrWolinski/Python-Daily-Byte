def check_route(string: str) -> bool:
    vertical = 0
    horizontal = 0

    for i in string:
        if i == 'U':
            vertical += 1
        elif i == 'D':
            vertical -= 1
        elif i == 'R':
            horizontal += 1
        else:
            horizontal -= 1

    if vertical == horizontal == 0:
        return True
    
    return False

print(check_route('URURD'))