def func_1(x):
    a = {}
    if len(x) != 8:
        a = "False"
    else:
        if x[:1].isalpha() and x[2:6].isdigit() and x[7:8].isalpha():
            a["First letters"] = x[:2]
            a["Digits"] = x[2:6]
            a["Last letters"] = x[6:8]
        else:
            a = "not correct format"
    return a


def func_2(y):
    summa = 0
    result = list(y)
    for element in result:
        if element.isdigit():
            summa = summa + int(element)
    return summa
