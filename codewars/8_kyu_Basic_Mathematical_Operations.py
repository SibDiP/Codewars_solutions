"""8 kyu Basic Mathematical Operations
"""

# 1 eval(), f-string. eval() with open argument - unsecure practice
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

# 2 dict insted of if
def basic_op(operator, value1, value2):
    operation_dict = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }
    return operation_dict[operator]
