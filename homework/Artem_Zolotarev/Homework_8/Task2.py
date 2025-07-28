from sys import set_int_max_str_digits


def fibonnachi(x):
    a, b = 0, 1
    for var in range(x):
        a, b = b, a + b
    return a

print(fibonnachi(5))
print(fibonnachi(200))
print(fibonnachi(1000))
set_int_max_str_digits(100000)
print(fibonnachi(100000))
