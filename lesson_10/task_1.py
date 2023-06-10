# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv
import random
import string


# Здесь пишем код

def generate_random_name():
    """
    Генератор случайной строки
    :return: строка из двух случайных наборов букв разделенных пробелом
    """

    def rand_word():
        """Возвращает строку из случайных латинских букв длинной от 1 до 15 символов"""
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15)))

    while True:
        first_word = rand_word()
        second_word = rand_word()
        yield f'{first_word} {second_word}'


gen = generate_random_name()

for _ in range(5):
    print(next(gen))
