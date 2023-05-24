# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


# Здесь пишем код
def segment(point_a: tuple, point_b: tuple):
    """ Считаем сумму значений координат
    :param point_a: координаты точки А
    :param point_b: координаты точки Б
    :return: сумма значений координат
    """
    try:
        return point_a[0] + point_a[1] + point_b[0] + point_b[1]
        # я бы сделал так, но тогда не будет исключения про конкатенацию строк: sum(point_a) + sum(point_b)
    except Exception as e:
        return str(e)[::-1]


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']

for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
