class Flowers:
    def __init__(self, title, price, lifecircle, quantity, height_stem, color):
        self.title = title
        self.price = price
        self.lifecircle = lifecircle
        self.quantity = quantity
        self.height_stem = height_stem
        self.color = color

    def __repr__(self):
        return f'({self.title!r}, {self.price}, {self.lifecircle}, {self.height_stem}, {self.color!r}, {self.quantity})'


class Rose(Flowers):
    def __init__(self, title, price, lifecircle, quantity, height_stem, color):
        super().__init__(title, price, lifecircle, quantity, height_stem, color)


class Tulpan(Flowers):
    def __init__(self, title, price, lifecircle, quantity, height_stem, color):
        super().__init__(title, price, lifecircle, quantity, height_stem, color)


class Narcisse(Flowers):
    def __init__(self, title, price, lifecircle, quantity, height_stem, color):
        super().__init__(title, price, lifecircle, quantity, height_stem, color)


class Bouquet:
    def __init__(self):
        self.list_flowers = []

    def add(self, flower: Flowers, count: int):
        for f in self.list_flowers:
            if f.title == flower.title:
                f.quantity += count
                break
        else:
            flower.quantity = count
            self.list_flowers.append(flower)

    def average_lifecircle(self):
        count = len(self.list_flowers)
        total = sum(_.lifecircle for _ in self.list_flowers)
        return total / count

    def sort_by_price(self):
        return sorted((x.price, x.title) for x in self.list_flowers)

    def sort_by_lifecircle(self):
        return sorted((x.lifecircle, x.title) for x in self.list_flowers)

    def sort_by_color(self):
        return sorted((x.color, x.title) for x in self.list_flowers)

    def sort_by_height_stem(self):
        return sorted((x.height_stem, x.title) for x in self.list_flowers)

    def find_flower_by_lifecircle(self, min_value: int = None, max_value: int = None):
        result = []
        for _ in self.list_flowers:
            if min_value is not None and min_value > _.lifecircle:
                continue
            if max_value is not None and max_value < _.lifecircle:
                continue
            result.append((_.title, _.lifecircle))
        return result

    def __repr__(self):
        return f'{self.__class__.__name__}: {list(self.list_flowers)}'


flower1 = Rose('rose', 150, 24, 1, 50, 'red')
flower2 = Tulpan('tulpan', 100, 48, 1, 20, 'yellow')
flower3 = Narcisse('narcisse', 300, 18, 1, 15, 'white')

bouquet = Bouquet()
bouquet.add(flower1, 5)
bouquet.add(flower2, 3)
bouquet.add(flower3, 3)
print(bouquet)
print(bouquet.average_lifecircle())
print(bouquet.sort_by_price())
print(bouquet.sort_by_lifecircle())
print(bouquet.sort_by_color())
print(bouquet.sort_by_height_stem())
print(bouquet.find_flower_by_lifecircle(10, 100))
