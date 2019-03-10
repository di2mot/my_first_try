class MoneyBox:
    def __init__(self, capacity = 0):
        self.count = 0
        self.capacity = capacity  # конструктор с аргументом – вместимость копилки

    def can_add(self, v):

        if self.count + v <= self.capacity:
            return  True
        else: return False
    # True, если можно добавить v монет, False иначе

    def add(self, v=0):
        if self.can_add(v) == True:
            self.count += v

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)