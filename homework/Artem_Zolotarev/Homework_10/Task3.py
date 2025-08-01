first = int(input('Введи первое число: '))
second = int(input('Введи второе число: '))


def decorator(func):
    def wrapper():
        if first == second:
            result = func(first, second, operation='+')
            return result
        elif (first < 0) or (second < 0):
            result = func(first, second, operation='*')
            return result
        elif first > second:
            result = func(first, second, operation='-')
            return result
        elif first < second:
            result = func(first, second, operation='/')
            return result
        return None
    return wrapper


@decorator
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '/':
        return num1 / num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    return None


print(calc())
