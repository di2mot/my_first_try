# Ну, вот такое реение родил мой мозг
# Про re я конечно нагуглил, но сотальное моё!

import re
string = input()

# Тут прикол в том, что дальше трубется функуия типа:
# ('(? = test)', 'testtast'), и я не знал как встать переменную внутрь

in_string = '(?=' + input() + ')'

result = [m.start() for m in re.finditer(in_string, string )]
try:
    # Не бейте сильно, по заданию если нет вхождений
    # нужно выдвать -1, но я не хочу усложнять и решил просто
    # вызывать except
    errore = result[0]
    print(*result)

except IndexError:
    print('-1')


# Формат ввода:
# На первой строке содержится исходная строка, на второй строке ввода
# указана подстрока,позиции которой требуется найти.
# Строки состоят из символов латинского алфавита.
#
# Формат вывода:
# Строка, содержащая индексы (индексация начинается с нуля) вхождения
# подстроки в строку, разделённые пробелом или число -1 в случае,
# когда подстрока не найдена