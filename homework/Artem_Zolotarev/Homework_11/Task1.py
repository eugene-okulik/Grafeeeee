class Book:

    def __init__(self, material, is_text):
        self.material = material
        self.is_text = is_text
        self.reserved = False

    def is_reserved(self):
        return self.reserved

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            print('Зарезервирована')
        else:
            print('Уже зарезервирована')

    def unreserve(self):
        if self.reserved:
            self.reserved = False
            print('Резерв снят')
        else:
            print('Книга итак доступна к резервированию')


class Books(Book):
    def __init__(self, material, is_text, title, author, page_quantity, isbn, reserved):
        super().__init__(material, is_text)
        self.title = title
        self.author = author
        self.page_quantity = page_quantity
        self.isbn = isbn
        self.reserved = reserved

    def info(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_quantity},'
                    f' материал: {self.material}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.page_quantity},'
                    f' материал: {self.material}')


ex1 = Books('бумага', True, 'Три товарища',
            'Эрих Мария Ремарк', 800, False, False)
ex2 = Books('бумага', True, 'Превращение', 'Франц Кафка',
            230, False, False)
ex3 = Books('бумага', True, 'Старик и море', 'Эрнест Хэмингуэй',
            200, False, False)
ex4 = Books('бумага', True, 'Так сказал Заратустра', 'Фридрих Ницше',
            560, False, False)
ex5 = Books('бумага', True, 'Война и Мир', 'Лев Толстой',
            1560, False, True)

print(ex1.info())
print(ex2.info())
print(ex3.info())
print(ex4.info())
print(ex5.info())


class EducationBooks(Book):
    def __init__(self, material, is_text, title, author, subject, grade, homework, page_quantity, reserved):
        super().__init__(material, is_text)
        self.title = title
        self.author = author
        self.page_quantity = page_quantity
        self.reserved = reserved
        self.subject = subject
        self.grade = grade
        self.homework = homework

    def info(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject},'
                    f' класс: {self.grade}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, предмет: {self.subject},'
                    f' класс: {self.grade}')

eb1 = EducationBooks('бумага', True, 'Алгебра', 'Попов', 'Математика',
                     9, True, 236, False)
eb2 = EducationBooks('бумага', True, 'Физика', 'Федченко', 'Физика',
                     11, True, 390, True)
eb3 = EducationBooks('бумага', True, 'Музыка', 'Попов', 'Музыка',
                     3, False, 152, False)

print(eb1.info())
print(eb2.info())
print(eb3.info())