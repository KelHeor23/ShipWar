from pprint import pprint
from random import randint, choice

from Ship import Ship

class GamePole:

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._ships = list()

    def init(self):
        # Создаем корабли
        self._ships = [
            Ship(4, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(3, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(2, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
            Ship(1, tp=randint(1, 2)),
        ]

        for ship in self._ships:
            placed = False
            ship._field = self # Для каждого колрабля задаем, что он работает с этим полем

            # Пытаемся расставить корабли.
            while not placed or ship._x == None or ship._y == None:
                ship._x = randint(0, self._size - 1)
                ship._y = randint(0, self._size - 1)

                # Если корабль, с заданными координатами не помещается, прерываем итеррацию цикла
                if ship.is_out_pole(self._size):
                    ship._x = None
                    ship._y = None
                    continue

                # Проходим по списку всех кораблей
                for otherShip in self._ships:
                    # Игнорируем сеюя, в этом списке
                    if id(ship) == id(otherShip):
                        continue
                    # Если дошли до кораблей, которые еще не расставлены, то прерываемся
                    if otherShip._x == None and otherShip._y == None:
                        break
                    # Првоеряем не пересекаемся ли с другим кораблем
                    if ship.is_collide(otherShip):
                        ship._x = None
                        ship._y = None
                        break
                placed = True

    def get_ships(self) -> list:
        return self._ships
    
    def move_ships(self) -> None:
        for ship in self._ships:
            i = choice([1, -1])
            if ship.move(i):
                continue
            elif ship.move(-i):
                continue

    def show(self):
        field = self.__fill_field()
        pprint(field)

    def get_pole(self):
        field = self.__fill_field()
        fieldTuple = [tuple(item) for item in field]
        return tuple(fieldTuple)

    def __fill_field(self):
        field = [[0 for _ in range(self._size)] for _ in range(self._size)]
        for ship in self._ships:
            selfDict, _ = ship.coordsOfTheShip()
            for x, y in selfDict:
                field[x][y] = selfDict[x, y]
        return field