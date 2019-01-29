footbol_team = dict()
# Создаём функции которые будут заниматься логикой скрипта
for i in range(int(input())):
    text = input().split(';')
    # Проверяем, если команда в списке, если нет то создаём новый ключ
    if text[0] not in footbol_team:
        footbol_team[text[0]] = [0, 0, 0, 0, 0]
    footbol_team[text[0]][0] += 1
    if text[1] > text[3]:
        footbol_team[text[0]][1] += 1
        footbol_team[text[0]][4] += 3
    if text[1] == text[3]:
        footbol_team[text[0]][2] += 1
        footbol_team[text[0]][4] += 1
    if text[1] < text[3]:
        footbol_team[text[0]][3] += 1
    # Проверяем, если команда в списке, если нет то создаём новый ключ
    if text[2] not in footbol_team:
        footbol_team[text[2]] = [0, 0, 0, 0, 0]
    footbol_team[text[2]][0] += 1
    if text[3] > text[1]:
        footbol_team[text[2]][1] += 1
        footbol_team[text[2]][4] += 3
    if text[3] == text[1]:
        footbol_team[text[2]][2] += 1
        footbol_team[text[2]][4] += 1
    if text[3] < text[1]:
        footbol_team[text[2]][3] += 1

# Вывод на печать
for i in footbol_team:
    q = ''
    for j in footbol_team[i]:
        q += str(j) + ' '
    print(i + ':' + q)

