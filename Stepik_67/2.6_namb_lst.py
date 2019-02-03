# Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
# которая выводит все позиции, на которых встречается число x в переданном списке lst.
# Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

lst = input().split()
x = str(input())
if lst.count(x) == 0:
    print("Отсутствует")
else:
    for i in range(0, len(lst)):
        if x == lst[i]:
            print(i, end=' ')
            
# Добавлю пару альтернативных решений
# 1

l = [int(i) for i in input().split()]
x = int(input())
if not x in l: print('Отсутствует')
for i in range(len(l)):
    if l[i]==x: print(i, end = ' ')
    
# 2

exec('''st = [int(i) for i in input().split()]
n = int(input())
if not n in st: print('Отсутствует')
for i in range(len(st)):
    if(st[i]==n):
        print(i, end=" ")''')
