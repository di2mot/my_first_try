import sys
import re

patern_1 = r'\b(\w)(\w)'
patern_2 = r'\2\1'

# line = 'There.lo be no more "Aaaaaaaaaaaaaaa" aaaa'
#
for line in sys.stdin:
    line = line.rstrip()
    find = re.sub(patern_1, patern_2, line)
    print(find)
# find = re.sub(patern_1, patern_2, line)
# print(line)
# print(find)

'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
'''
''' Cod Narkoman edition'''

# find = re.findall(patern, line)
# fin_list = list()
# for repl_word in find:
#     words = list(repl_word)
#     words[0], words[1] = words[1], words[0]
#     words = ''.join(words)
#     fin_list.append(words)
#
# print(*fin_list)