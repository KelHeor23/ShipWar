from Ship import Ship
from GamePole import GamePole

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)
assert (
    ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0
), "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
assert s1.is_collide(
    s2
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert (
    s1.is_collide(s3) == False
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(
    s2
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(
    10
), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
s2 = Ship(3, 2, 1, 5)
assert (
    s2.is_out_pole(10) == False
), "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
        for ship in p.get_ships():
            if s != ship:
                assert (
                    s.is_collide(ship) == False
                ), "корабли на игровом поле соприкасаются"
    p.move_ships()
p.show()
gp = p.get_pole()
assert (
    type(gp) == tuple and type(gp[0]) == tuple
), "метод get_pole должен возвращать двумерный кортеж"
assert (
    len(gp) == 10 and len(gp[0]) == 10
), "неверные размеры игрового поля, которое вернул метод get_pole"
pole_size_8 = GamePole(8)
pole_size_8.init()
print("\n Passed")