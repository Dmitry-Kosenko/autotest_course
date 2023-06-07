# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture(autouse=True)
def check_id(request):
    marker = request.node.get_closest_marker("id_check")
    if marker is None:
        return
    print(', '.join(map(str, marker.args)))


@pytest.mark.id_check(1, 2, 3)
def test():
    # Здесь пишем код
    pass
