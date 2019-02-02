# Создаём два множества, в первом будут ключи, во втором будут слова которых нет в первом
inputSet, outputSet = set(), set()

for i in range(int(input())):
    inputSet.add(input().lower())

for i in range(int(input())):
    for j in input().lower().split():

        # Проверяем, есть ли данное слово
        if j not in inputSet:
            outputSet.add(j)

print(*outputSet, sep='\n')