import random


def payment():
    salary = input("Введите число: ")
    if salary.isnumeric():
        bonus = random.randint(1, 1000) if random.choice([True, False]) else 0
        print(int(salary) + bonus)
    else:
        print("Введено не число!")


payment()
