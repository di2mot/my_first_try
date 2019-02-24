namespace_n = {'global': ''}
code_list = ['create', 'add', 'get']


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

    return namespace_n


def add(command):
    command_1 = [command[0], command[2] + '1', command[1]]
    return create(command_1)


def get(var, per):

    if per in namespace_n and var in namespace_n[per]:
        return per

    try:
        for i in namespace_n:
            if per in namespace_n[i]:
                return get(var, i)

    except:
        return 'None'


for i in range(int(input())):
    command = input().split()
    if command[0] == code_list[0]:
        namespace_n = create(command)
    if command[0] == code_list[1]:
        namespace_n = add(command)
    if command[0] == code_list[2]:
        print(get(command[2] + '1', command[1]))
