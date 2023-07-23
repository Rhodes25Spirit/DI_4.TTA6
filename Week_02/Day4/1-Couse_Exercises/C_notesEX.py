## EXERCISE##
# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def calculation(a, b) -> None:
    '''action number_a + number_b'''

    result = a + b
    return result  # OR return print(result)


res = calculation(40, 10)
print(res)
pass


def calculation2(a, b) -> float:  # to add the type of the return add '- >'
    '''action number_a + number_b'''

    result = a - b
    return result  # OR return print(result)


res = calculation2(4.5, 10.3)
print(res)
pass

def totals(calculation):
    