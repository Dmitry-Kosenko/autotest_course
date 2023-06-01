# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
with open('test_file/task1_data.txt', encoding='utf-8') as source_file:
    result = ''
    lines = source_file.readlines()
    for line in lines:
        result += ''.join(s for s in line if not s.isdigit())
with open('test_file/task1_answer.txt', mode='w', encoding='utf-8') as out_file:
    out_file.writelines(result)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
