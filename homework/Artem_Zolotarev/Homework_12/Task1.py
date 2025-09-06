class Flowers:
    def __init__(self, title, price, lifecircle, height_stem, color):
        self.title = title
        self.price = price
        self.lifecircle = lifecircle
        self.height_stem = height_stem
        self.color = color

    def __repr__(self):
        return f'({self.title!r}, {self.price}, {self.lifecircle}, {self.height_stem}, {self.color!r})'


class RedFlowers(Flowers):
    def __init__(self, title, price, lifecircle, height_stem):
        super().__init__(title, price, lifecircle, height_stem, 'red')


class YellowFlowers(Flowers):
    def __init__(self, title, price, lifecircle, height_stem):
        super().__init__(title, price, lifecircle, height_stem, 'yellow')


class WhiteFlowers(Flowers):
    def __init__(self, title, price, lifecircle, height_stem):
        super().__init__(title, price, lifecircle, height_stem, 'while')


class Bouquet:
    def __init__(self, *args):
        self.list_flowers = [*args]

    def total_cost(self):
        return sum(x.price for x in self.list_flowers)

    def average_lifecircle(self):
        count = len(self.list_flowers)
        total = sum(_.lifecircle for _ in self.list_flowers)
        return total / count

    def sort_by(self, key):
        return sorted(self.list_flowers, key=lambda x: getattr(x, key))

    def find_flower_by_lifecircle(self, min_value: int = None, max_value: int = None):
        filtered_flowers = []
        for flower in self.list_flowers:
            if ((min_value is None or flower.lifecircle >= min_value) and (
                    max_value is None or flower.lifecircle <= max_value)):
                filtered_flowers.append(flower)
        return filtered_flowers

    def __repr__(self):
        return f'{self.__class__.__name__}: {list(self.list_flowers)}'


flower1 = RedFlowers('rose', 150, 24, 50)
flower2 = YellowFlowers('tulpan', 100, 48, 20)
flower3 = WhiteFlowers('narcisse', 300, 18, 15)

bouquet = Bouquet(flower3, flower2, flower1)
print(bouquet)
print(bouquet.total_cost())
print(bouquet.average_lifecircle())
print(bouquet.sort_by('lifecircle'))
print(bouquet.find_flower_by_lifecircle(10, 30))
