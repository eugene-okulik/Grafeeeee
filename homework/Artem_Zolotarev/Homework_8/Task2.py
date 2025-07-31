from sys import set_int_max_str_digits


def fibonacci(limit):
    a, b = 0, 1
    counter = 0
    while counter < limit:
        a, b = b, a + b
        yield a
        counter += 1


def find_fibonacci(num):
    counter = 1
    number = 0
    for x in fibonacci(10000000):
        if counter == num:
            number = x
            break
        counter += 1
    return number
print(find_fibonacci(5))
print(find_fibonacci(200))
print(find_fibonacci(1000))
set_int_max_str_digits(10000000)
print(find_fibonacci(100000))
