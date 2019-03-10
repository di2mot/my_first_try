class Buffer:
    def __init__(self):
        self.list = []
        self.list_five = []

    def add(self, *a):
        self.list.append(a)
        for i in self.list:
            if len(self.list_five) <= 5:
                self.list_five.append(i)


    def get_current_part(self):

        return print(self.list)# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]