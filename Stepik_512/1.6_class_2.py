class ExtendedStack(list):
    def sum(self):

        return self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        return self.append(self.pop() - self.pop())

    def mul(self):
        # операция умножения
        return self.append(self.pop() * self.pop())

    def div(self):
        # операция
        return self.append(self.pop() // self.pop())