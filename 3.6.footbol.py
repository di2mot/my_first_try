n = int(input())
#n = 3
footbol_team = dict()

# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# Команда: |Всего_игр| Побед| Ничьих| Поражений| Всего_очков|
# Индекс:      0        1      2          3          4
for i in range(n):
    text = input().split(';')
    # Обновляю значения в словаре
    if text[0] in footbol_team:
        footbol_team[text[0]][0] += 1
        if text[1] > text[3]:
            footbol_team[text[0]][1] += 1
            footbol_team[text[0]][4] += 3
        if text[1] == text[3]:
            footbol_team[text[0]][2] += 1
            footbol_team[text[0]][4] += 1
        if text[1] < text[3]:
            footbol_team[text[0]][3] += 1



    if text[2] in footbol_team:
        footbol_team[text[2]][0] = footbol_team[text[2]][0] + 1
        if text[3] > text[1]:
            footbol_team[text[2]][1] += 1
            footbol_team[text[2]][4] += 3
        if text[3] == text[1]:
            footbol_team[text[2]][2] += 1
            footbol_team[text[2]][4] += 1
        if text[3] < text[1]:
            footbol_team[text[2]][3] += 1


    # Проверяю наличие ключей в словаре, если нет, то создаю
    if text[0] not in footbol_team:
        footbol_team[text[0]] = [1, 0, 0, 0, 0]
        if text[1] > text[3]:
            footbol_team[text[0]][1] += 1
            footbol_team[text[0]][4] += 3
        if text[1] == text[3]:
            footbol_team[text[0]][2] += 1
            footbol_team[text[0]][4] += 1
        if text[1] < text[3]:
            footbol_team[text[0]][3] += 1


    if text[2] not in footbol_team:
        footbol_team[text[2]] = [1, 0, 0, 0, 0]
        if text[3] > text[1]:
            footbol_team[text[2]][1] += 1
            footbol_team[text[2]][4] += 3
        if text[3] == text[1]:
            footbol_team[text[2]][2] += 1
            footbol_team[text[0]][4] += 1
        if text[3] < text[1]:
            footbol_team[text[2]][3] += 1

    #print(footbol_team)
for i in footbol_team:
    print(i, ' :', *footbol_team[i])

