# -*- coding: utf-8 -*-
import datetime
import time

import pytest


@pytest.fixture(scope='class', autouse=True)
def start_stop_time():
    print(f'\nТесты запущены {datetime.datetime.now()}\n')
    yield
    print(f'\nТесты завершены {datetime.datetime.now()}')


@pytest.fixture()
def execution_time():
    start_time = time.perf_counter()
    yield
    print(f'\nВремя выполнения теста: {round(time.perf_counter() - start_time, 5)}')



