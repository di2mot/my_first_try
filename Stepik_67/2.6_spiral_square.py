# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке.:

# Немного подсмотрел алгоритм
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]

# Объявляем счётчики
i, j, coint = 0, 0, 1

# Запускаем цикл
while coint <= (n * n):
    a[i][j] = coint
    if i <= j + 1 and i + j < n - 1:
        j += 1
    elif i < j and j + i >= n - 1:
        i += 1
    elif i >= j and i + j > n - 1:
        j -= 1
    else:
        i -= 1
    coint += 1
# Выводим 
for i in a:
    print(*i, sep='\t')
    
# Для прохождения на сайте использовать:
#for i in range(0, n):
#    print(*a[i], sep=' ')


#Есть и более красивые решения:
n = int(input())
x,y,dx,dy, m = 0,0,0,1, [[0]*n for i in range(n)]
for i in range(n*n):
  m[x][y]=str(i+1)
  if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0 or m[x+dx][y+dy]:
      dx,dy = dy,-dx
  x,y = x+dx, y+dy
print("\n".join([" ".join(i) for i in m]))

#Есть и такой:
n = int(input())
m = [[0] * n for i in range(n)]
i, j, di, dj = 0, 0, 0, 1

for k in range(n * n):
    m[i][j] = k + 1
    if (not -1 < i + di < n) or (not -1 < j + dj < n) or m[i + di][j + dj] != 0:
        di, dj = dj, -di
    i, j = i + di, j + dj

[print(*i) for i in m]

# Пояснение к коду:
not -1 < i + di < n - по вертикали
not -1 < j + dj < n - по горизонтали
m[i + di][j + dj] != 0 - поскольку сначала всё поле заполнено '0',
то здесь проверяется не попали ли мы на уже пройденное значение: если равно 0,
то нужно новое значение, если не равно, то нужно повернуть!
not -1 < i + di < n
если новый индекс i + di в поле -1 <...< n нет (not) - это, так сказать, дословный перевод.
По человечески это звучит как, новый индекс НЕ в поле
