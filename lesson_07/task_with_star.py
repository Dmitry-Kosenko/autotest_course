# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:
    """Римское число"""
    __ROMAN_DIGITS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def __init__(self, roman_num: str):
        for symbol in roman_num:
            assert symbol in RomanNums.__ROMAN_DIGITS, f'{symbol} не римская цифра!'
        self.__roman_num = roman_num
        self.__roman_num_length = len(self.__roman_num)

    def from_roman(self) -> int:
        """Преобразует римское в арабское число и возвращает результат"""

        arabian = 0

        for idx, symbol in enumerate(self.__roman_num):
            if self.__roman_num_length > idx + 1 and \
                    RomanNums.__ROMAN_DIGITS[self.__roman_num[idx + 1]] > RomanNums.__ROMAN_DIGITS[symbol]:
                arabian -= RomanNums.__ROMAN_DIGITS[symbol]
            else:
                arabian += RomanNums.__ROMAN_DIGITS[symbol]
        return arabian

    def is_palindrome(self) -> bool:
        """Проверяет является ли арабское представление числа палиндромом"""

        arabian = self.from_roman()
        return str(arabian) == str(arabian)[::-1]


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]

test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
