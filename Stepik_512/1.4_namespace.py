namespace_n = {'global': ''}
code_list = ['create', 'add', 'get']
exit_list = []


def create(command):
    if command[2] not in namespace_n:
        namespace_n[command[2]] = ''
    # Создаём временное множество
    global_list = set()
    # Что бы не обнулить значения ключа в словаре, добавляем их в множество
    global_list = global_list.union(namespace_n[command[2]])
    # Теперь к множеству добавляем новое значение
    global_list.add(command[1])
    # Обновляем значения ключа
    namespace_n[command[2]] = global_list
    print(namespace_n)
    return namespace_n


def add(command):
    command_1 = [command[0], command[2]+'1', command[1]]
    return create(command_1)


def get(command):
    try:
        if command[2]+'1' in namespace_n[command[1]]:
            exit_list.append(command[1])
            print(namespace_n)
            return exit_list

        elif command[2]+'1' not in namespace_n[command[1]]:
            for i in namespace_n:
                if command[1] in namespace_n[i] and command[2]+'1' in namespace_n[i]:
                    exit_list.append(i)
                    print(namespace_n)
                    return exit_list

            exit_list.append('None')
            print(namespace_n)
            return  exit_list

    except KeyError:
        exit_list.append('None')
        print(namespace_n)
        return exit_list


for i in range(int(input())):
    command = input().split()
    if command[0] == code_list[0]:
        namespace_n = create(command)
    if command[0] == code_list[1]:
        namespace_n = add(command)
    if command[0] == code_list[2]:
        exit_list = get(command)


for i in exit_list:
    print(i)

# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b