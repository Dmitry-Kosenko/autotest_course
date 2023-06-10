# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def division(a, b):
    """
    Деление первого аргумента на второй
    :return: Результат деления
    """
    return a / b


class Test:

    def test_positive(self, execution_time):
        assert division(4, 2) == 2.0

    def test_float(self, execution_time):
        assert division(0.4, 2) == 0.2

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            division(4, 0)
