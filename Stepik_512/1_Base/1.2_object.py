objects = [1, 2, 1, 2, 3, 1, 2, 1, 2, 2, 6 , 7]
storage = set()
for i in objects:
    storage.add(id(i))
print(len(storage))