class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *a):
        self.list.extend(a)
        while len(self.list) >= 5:
            print(sum(self.list[0:5]))
            del self.list[0:5]

    def get_current_part(self):
        return self.list
