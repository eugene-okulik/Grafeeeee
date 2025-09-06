secret_number = input('Введи секретное число: ')

while True:
    enter_number = input('Угадай цифру: ')
    if secret_number == enter_number:
        print('Поздравляю! Вы угадали')
        break
    else:
        print('попробуйте снова!')
