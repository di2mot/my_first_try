Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка.

def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0: l[i] //=  2
        else: del l[i]
     
# Читаемее:
def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            del l[i]
# Ещё варианты, чужие:

# 1:
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]
    
# 2:
def modify_list(l):
    b = []
    for x in l:
        if x % 2 == 0:
            b.append(x // 2)
    l[:] = b
