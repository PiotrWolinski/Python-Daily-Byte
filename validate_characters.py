def validate(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    queue = []

    valid_set = set(['{}', '[]', '()'])

    for i in s:
        if i == '{' or i == '[' or i == '(':
            queue.append(i)
        elif len(queue) != 0:
            popped = queue.pop()
            tmp = f"{popped}{i}"
            print(tmp)
            if tmp not in valid_set:
                return False
        elif len(queue) == 0:
            return False
        
    if len(queue):
        return False

    return True


