def func_1(x):
    a = ()
    if len(x) == 8:
        if x[:1].isalpha() and x[2:6].isdigit():
            a = x[:6]
        else:
            print("Not correct format")
    else:
        a = "False"
    return a


def func_2(y):
    summa = 0
    result = list(y)
    for element in result:
        if element.isdigit():
            summa = summa + int(element)
    return summa
