def compare(s: str, t: str) -> bool:
    queue_s = []
    queue_t = []

    for i in s:
        if i == '#' and len(queue_s):
            queue_s.pop()
        else:
            queue_s.append(i)

    for i in t:
        if i == '#' and len(queue_t):
            queue_t.pop()
        else:
            queue_t.append(i)

    if queue_s != queue_t:
        return False
    
    return True
        
assert compare(s = "ABC#", t = "CD##AB") == True
assert compare(s = "como#pur#ter", t = "computer") == True
assert compare(s = "cof#dim#ng", t = "code") == False