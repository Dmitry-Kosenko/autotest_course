# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("args, expected", [
    ((10, 2), 5.0),
    ((100, 2, 5), 10.0),
    pytest.param((10, 0, 5), 'division by zero', marks=pytest.mark.smoke),
    ((), 'no params'),
    pytest.param((10.0, 2, 0.5), 10.0, marks=pytest.mark.skip(reason='Пропуск теста'))
])
def test_all_division(args, expected):
    match expected:
        case 'division by zero':
            with pytest.raises(ZeroDivisionError):
                all_division(*args)
        case 'no params':
            with pytest.raises(IndexError):
                all_division(*args)
        case _:
            assert all_division(*args) == expected
