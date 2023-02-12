""" n = '6 / 3'
m = n.split()
print(type(n)) """

""" def newparse(data):
    newlist = data.split()
    return newlist """

""" newparse(n)
print(type(newparse(n))) """

""" def realisefunction(data):
    if data[1] == '+':
        print(f"{data[0]}{data[1]}{data[2]} = {int(data[0]) + int(data[2])}")
    if data[1] == '-':
        print(f"{data[0]}{data[1]}{data[2]} = {int(data[0]) - int(data[2])}")
    if data[1] == '/':
        print(f"{data[0]}{data[1]}{data[2]} = {int(data[0]) / int(data[2])}")
    if data[1] == '*':
        print(f"{data[0]}{data[1]}{data[2]} = {int(data[0]) * int(data[2])}") """
    

""" realisefunction(newparse(n))  """

""" def calculate(userinput): # <<< на вход примимает выражение типа 'a [+-/*] b'
    pattern = "([\-]{0,}\d{1,})\s{0,}([\/|\+|\*|\-]{1})\s{0,}([\-]{0,}\d{1,})"
    parsedata = re.findall(pattern, userinput)[0] # возвращает list ('операнд1','операция','операнд 2')
    a = int(parsedata[0])
    b = int(parsedata[2])
    oper = parsedata[1]
    match oper:
        case "+":
            func = lambda a, b: a + b
        case "-":
            func = lambda a, b: a + b
        case "/":
            if b != 0:
                func = lambda a, b: a / b
            else:
                print("DivisionByZero")
                func = None
        case "*":
            func = lambda a, b: a + b
    return func(a, b) if func!=None else '' """

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


# a = int(m[0])
# c = m[1]
# b = int(m[2])

""" result = int(m[0])
multanddiv = [i for i in range(0, len(m)) if m[i]=="*" or m[i]=="/"]
staples = [i for i in range(0, len(m)) if m[i][0]=="(" or m[i][-1]==")"]

print(multanddiv) """
""" print(staples) """

""" def donew_List(staples, old_list):
    newlist = []
    for item in old_list:
        if item in staples:
            if  """


""" def mult_and_div(data, expression):
    new_list = []
    for item in expression:
        if item in data:

    for item in data: """
        

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
