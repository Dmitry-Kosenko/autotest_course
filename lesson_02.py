from pathlib import Path

# Задание 1
side = 5  # сторона квадрата
print(f'1. Периметр = {side * 4}\n',
       '  Площадь = %d' % side ** 2, '\n',
       '  Диагональ = {}'.format(side * 2 ** 0.5))

# Задание 2
a2, b2, c2 = 4, -16, 10  # коэффициенты
d = b2 ** 2 - 4 * a2 * c2  # дискриминант
if d < 0:
    print('2. Уравнение не имеет корней', d)
else:
    # корни уравнения
    x1 = round((-b2 + d ** 0.5) / (2 * a2), 2)
    x2 = round((-b2 - d ** 0.5) / (2 * a2), 2)
    print(f'2. Корни уравнения: {x1}, {x2}')

# Задание 3
first_str = 'First'
second_str = 'Second'
print(f'3. {second_str[:2]}{first_str[2:]} {first_str[:2]}{second_str[2:]}')

# Задание 4
# через срезы
file_path = r'e:\ATF\atf-rc-8.7.7.zip'
print('4.1. Название файла:', file_path[file_path.rfind('\\') + 1:file_path.rfind('.')])
print('     Название диска:', file_path[:file_path.find(':')])
print('     Корневая папка:', file_path.split('\\')[1])

# а так правильнее, но мы этого не проходили еще
path = Path(file_path)
print('4.2. Название файла:', path.stem)
print('     Название диска:', path.drive[:-1])
print('     Корневая папка:', path.parts[1])

# Задание 5
a5, b5 = 2, 3
print(f'5. {a5}+{b5}={a5+b5}', '{}*{}={}'.format(a5, b5, a5*b5))

# Задание 6
string1 = '0123456789'
print('6.', string1[::2])

# Задание 7
first_string = 'wtf'
second_string = 'brickquz jmpy veldt whangs fox'
indexes = (
    second_string.find(first_string[0]),
    second_string.find(first_string[1]),
    second_string.find(first_string[2])
)
print('7.', second_string[min(indexes):max(indexes)+1])