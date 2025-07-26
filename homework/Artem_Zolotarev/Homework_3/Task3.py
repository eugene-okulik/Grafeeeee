import random

# рассчитываем среднее арифмитическое
a = random.randint(1, 100)
b = random.randint(1, 100)
array = [a, b]
print(array)
average_arithmetic = ((sum(array))/(len(array)))
print(average_arithmetic)


# рассчитываем среднее геометрическое
multiple = 1
for x in array:
    multiple *= x

average_geometry = multiple**(1/len(array))
print(average_geometry)
