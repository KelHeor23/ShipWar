class Ship:
    def __init__(self, length: int, tp: int = 1, x:int = None, y:int = None) -> None:
        self._length = length
        self._tp = tp
        self._x = x  
        self._y = y
        self._is_move = True
        self._cells = [1 for _ in range(length)]  # текущий список с кораблями
        self._field = None

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value
        
    def set_start_coords(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_start_coords(self) -> tuple:
        return self._x, self._y
    
    # Механизм движения корабля
    def move(self, go) -> None:
        if not self._is_move:
            return False

        # Специально для тех, кто решит подвигать корабли, для которых не задано поле
        if self._field is None:
            if self._tp == 1:
                self._x += go
                return
            if self._tp == 2:
                self._y += go
                return
            
        # Сохраняем текущее положение
        temp_x, temp_y = self._x, self._y

        # Обновляем координаты в зависимости от типа движения
        if self._tp == 1:  # Горизонтальное движение
            self._x += go
        elif self._tp == 2:  # Вертикальное движение
            self._y += go

        # Проверяем выход за пределы поля и столкновения
        if not self.is_out_pole(self._field._size) or self.is_collides():        
            self._x, self._y = temp_x, temp_y #Если есть проблема, возвращаем старые координаты
            return False

        return True

    # Проверка, находится ли корабль в пределах поля.
    def is_out_pole(self, size) -> bool:
        if self._tp == 1:
            if self._x not in range(size):
                return True
            if self._y not in range(size):
                return True
            if self._length >= size - self._x + 1:
                return True
            return False

        if self._tp == 2:
            if self._x not in range(size):
                return True
            if self._y not in range(size):
                return True
            if self._length >= size - self._y + 1:
                return True
            return False

    # Проверка, столкновений с другими кораблями.
    def is_collides(self) -> bool:
        for other_ship in self._field._ships:
            if self.is_collide(other_ship):
                return True
        return False
    
    # Проверка на столкновение с другим кораблем.
    def is_collide(self, ship) -> bool:
        # Проверяем, если координаты корабля не заданы
        if ship._x is None and ship._y is None:
            return True

        self_coords, self_range = self.coordsOfTheShip()
        other_range = ship.coordsOfTheShip()[1]

        # Проверяем пересечение координат
        return bool(set(self_coords).intersection(other_range))

    # Возвращает координаты корабля и его диапазон.
    def coordsOfTheShip(self):
        if self._tp == 1:  # Горизонтальный корабль
            self_coords = {
                (x, self._y): ceil
                for ceil in self._cells
                for x in range(self._x, self._x + self._length)
            }
            self_range = {
                (x, y)
                for x in range(self._x - 1, self._x + self._length + 1)
                for y in range(self._y - 1, self._y + 2)
            }
        elif self._tp == 2:  # Вертикальный корабль
            self_coords = {
                (self._x, y): ceil
                for ceil in self._cells
                for y in range(self._y, self._y + self._length)
            }
            self_range = {
                (x, y)
                for x in range(self._x - 1, self._x + 2)
                for y in range(self._y - 1, self._y + self._length + 1)
            }
    
        return self_coords, self_range
