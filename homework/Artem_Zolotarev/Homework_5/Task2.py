a = 'результат операции: 42'

b = 'результат операции: 514'

c = 'результат работы программы: 9'


def find_index(string, text):
    try:
        return text.index(string) + 2
    except ValueError:
        return -1


print(int(a[find_index(': ', a):]) + 10)
print(int(b[find_index(': ', b):]) + 10)
print(int(c[find_index(': ', c):]) + 10)
