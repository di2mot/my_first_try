import os

current_dir = str

for root, dirs, files in os.walk('main'):
    for file in files:
        if current_dir == root:
            break
        if file.endswith(".py"):
            current_dir = root
            print(current_dir)
            with open('text_dir.txt', 'a') as file:
                file.write(current_dir + '\n')


