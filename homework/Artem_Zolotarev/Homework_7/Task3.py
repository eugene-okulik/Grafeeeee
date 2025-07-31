first_str = 'результат операции: 42'
second_str = 'результат операции: 54'
third_str = 'результат работы программы: 209'
fourth_str = 'результат: 2'


def summary(text):
    return int(text.split()[-1]) + 10


print(summary(first_str))
print(summary(second_str))
print(summary(third_str))
print(summary(fourth_str))
