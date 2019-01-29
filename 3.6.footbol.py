n = int(input())
footbol_team = dict()

# Создаём функции которые будут заниматься логикой скрипта

def fun_1(text):
    if text[1] > text[3]:
        footbol_team[text[0]][1] += 1
        footbol_team[text[0]][4] += 3
    if text[1] == text[3]:
        footbol_team[text[0]][2] += 1
        footbol_team[text[0]][4] += 1
    if text[1] < text[3]:
        footbol_team[text[0]][3] += 1
    return footbol_team

def fun_2(text):
    if text[3] > text[1]:
        footbol_team[text[2]][1] += 1
        footbol_team[text[2]][4] += 3
    if text[3] == text[1]:
        footbol_team[text[2]][2] += 1
        footbol_team[text[2]][4] += 1
    if text[3] < text[1]:
        footbol_team[text[2]][3] += 1
    return footbol_team
# Получается список с ключём:
# {"название_команды":[Всего_игр, Побед, Ничьих, Поражений, Всего_очков]}
# Для понимания, доступ к индексам параметра ключа:
# Команда: |Всего_игр| Побед| Ничьих| Поражений| Всего_очков|
# Индекс:      0        1      2          3          4
for i in range(n):
    text = input().split(';')
    # Обновляю значения в словаре
    if text[0] in footbol_team:
        footbol_team[text[0]][0] += 1
        fun_1(text)

    if text[2] in footbol_team:
        footbol_team[text[2]][0] += 1
        fun_2(text)

# Проверяю наличие ключей в словаре, если нет, то создаю
    if text[0] not in footbol_team:
        footbol_team[text[0]] = [1, 0, 0, 0, 0]
        fun_1(text)

    if text[2] not in footbol_team:
        footbol_team[text[2]] = [1, 0, 0, 0, 0]
        fun_2(text)
# Вывод на печать
for i in footbol_team:
    q = ''
    for j in footbol_team[i]:
        q += str(j) + ' '
    print(i + ':' + q)

