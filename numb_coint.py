# скрипт считающий сколько раз каждое число попадается в списке
a = input().split()
b = sorted(a)
j, c = 0, 0
for i in range(0, len(a)):
    if i!= c:
        continue
    j = b.count(b[i])
    c += j
    print(j, end=' ')
