def add_binary(a: str, b: str) -> str:
    reversed_a = list(a)[::-1]
    reversed_b = list(b)[::-1]

    size = len(a) if len(a) > len(b) else len(b)
    answer = []
    carry = '0'

    for _ in range(size):
        # print(f'a = {reversed_a}')
        # print(f'b = {reversed_b}')

        bit_a = '0'
        bit_b = '0'

        if len(reversed_a):
            bit_a = reversed_a[0]
            reversed_a = reversed_a[1::]

        if len(reversed_b):
            bit_b = reversed_b[0]
            reversed_b = reversed_b[1::]

        if carry == '1':
            if bit_a == '1' and bit_b == '1':
                answer.append('1')
            elif bit_a == '1' or bit_b == '1':
                answer.append('0')
            elif bit_a == '0' and bit_b == '0':
                answer.append('1')
                carry == '0'
        else:
            if bit_a == '1' and bit_b == '1':
                answer.append('0')
                carry = '1'
            elif bit_a == '1' or bit_b == '1':
                answer.append('1')
            elif bit_a == '0' and bit_b == '0':
                answer.append('0')

        # print(f'answer = {answer}')

    if carry == '1':
        answer.append('1')
        

    # print(answer[::-1])
    return ''.join(answer[::-1])

assert add_binary('100', '1') == '101'
assert add_binary('11', '1') == '100'
assert add_binary('1', '0') == '1'