# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
# заканчивающихся строкой, содержащей только строку "end" (без кавычек)
# Программа должна вывести матрицу того же размера, у которой каждый элемент
# в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.
# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.


a = [[int(i) for i in input().split()]] 
n = input()
while n != 'end':
    a.append([int(i) for i in n.split()])
    n = input()
namb = 0
c = int(len(a))
for i in range(0, c):
    b = int(len(a[i]))
    for j in range(0, b):
        namb = int(a[i - 1][j]) + int(a[i - c + 1][j]) + \ # - c и - b для того что бы перейти на 0
            int(a[i][j - 1]) + int(a[i][j - b + 1])        #  и не выйти за пределы 
        print(namb, end=' ')
    print()
 