def primes():
    # i - наша интерируемая переменная
    i = 2
    # запускаем цикл
    while True:
        ''' count - счётчки, он не должен превышать i + 1, т.к. простые числа делятся только
        на себя и единицу, т.е. сумма получается i + 1, если сумма больше то это не простое
        число
        '''
        count = 0
        # перебираем делители
        for n in range(1, i+1):
            # тут проверяме на простоту
            if (i // 1 == i and i // i == 1) and (i%n == 0 and i%n != 1):
                # сумируем в счётчик все значения n которые подходят
                count += n
        # тут наконецто проверяме сумму, если она составляет i+1 то ок
        if count == i + 1:
            yield i
        # увеличиваем i на единицу
        i += 1

# проверка работоспособности
yo = primes()
for i in range(20):
    print(next(yo))

"""
Старый вариант

def prov(i):
    while True:
        count = 0
        for n in range(1, i+1):
            if (i // 1 == i and i // i == 1) and (i%n == 0 and i%n != 1):
                count += n
        if count <= i + 1:
            return i
        return False

def primes():
    res = 2
    while True:
        if prov(res) is not False:
            yield prov(res)
        else: pass
        res += 1

"""
