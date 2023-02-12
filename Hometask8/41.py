n = '22 * 300 - 14 + 10 * 10'

m = n.split()


print(m)


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

def multanddiv(data):
    m2 = []
    for i in range(1, len(data) - 1, 2):
        if data[i] == '*' or data[i] == '/':
            result = calc(int(data[i - 1]), int(data[i + 1]), data[i])
            if i > 1: m2.pop(-1)
            m2.append(result)
        else:
            m2.append(m[i])
            m2.append(int(m[i + 1]))
    print(m2)
    result2 = int(m2[0])
    for i in range(1, len(m2) - 1, 2):
        result2 = calc(result2, int(m2[i + 1]), m2[i])
    print(result2)

multanddiv(m)