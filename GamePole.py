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

        # Счетчик попыток
        cntTry = 0
        # Пока у последнего корабля не заданы координаты пытаемся расставить кораблики
        # Если произошло 200 попыток и кораблики не встали, выбрасываем ошибку
        while self._ships[len(self._ships)- 1]._x is None or \
                    self._ships[len(self._ships)- 1]._y is None:
            cntTry += 1
            for i in range(len(self._ships)):            
                if not self.setShip(self._ships[i], self._ships[:i]):
                    i = 0
            if cntTry == 200:
                raise Exception("Расставить корабли не получилось")

    # Функция расстановки кораблей на поле
    def setShip(self, ship :Ship, otherShips) -> bool:
        cntTry = 0
        ship._field = self # Для каждого корабля задаем, что он работает с этим полем
        
        # Пытаемся расставить корабли.
        while ship._x is None or ship._y is None:
            ship._x = randint(0, self._size - 1)
            ship._y = randint(0, self._size - 1)

            # Если корабль, с заданными координатами не помещается, прерываем итерацию цикла
            if ship.is_out_pole(self._size):
                ship._x = None
                ship._y = None
                continue

            # Проходим по списку всех кораблей
            for otherShip in otherShips:
                # Првоеряем не пересекаемся ли с другим кораблем
                if ship.is_collide(otherShip): 
                    ship._x = None
                    ship._y = None
                    cntTry += 1                     
                    break
            if cntTry == 100:
                return False
        return True
        
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