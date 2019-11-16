namespace_n = dict()


def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return 'Yes'
    if start not in namespace_n:
        return None
    for node in namespace_n[start]:
        if node not in path:
            newpath = find_path(node, end, path)
            if newpath:
                return newpath
    return None


def new_dict(key, value=''):
    if key not in namespace_n:
        namespace_n[key] = value
    time_set = set()
    time_set = time_set.union(namespace_n[key])
    time_set.add(value)
    namespace_n[key] = time_set
    return namespace_n


# вводится число n класов
for i in range(int(input())):
    input_command = str(input())
    try:
        # разбиваю строчку по двоеточию
        input_command = input_command.split(':')
        input_command = [x.strip(' ') for x in input_command]

        # проверяю длинну после двоеточия
        # если больше 1 символа, бью на пробелы
        if len(input_command[1]) > 1:
            space = input_command[1].split()
            space = [x.strip(' ') for x in space]
            # добавляю каждый символ после пробела в словарь
            for i in space:
                new_dict(i, input_command[0])
                new_dict(input_command[0])
        else:
            # если строка из одного символа то всё просто
            new_dict(input_command[1], input_command[0])
            new_dict(input_command[0])

    except Exception:
        # а тут если просто ключ есть без значения
        new_dict(input_command[0])


# вводится число запросов
for i in range(int(input())):
    reqvest = str(input()).split()
    if str(find_path(reqvest[0], reqvest[1])) is 'Yes':
        print('Yes')
    else:
        print('No')
