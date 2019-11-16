import sys
import re

patern = r'z[a-zA-Z0-9]{3}z'
line = 'aza1aza'
# for line in sys.stdin:
#     line = line.rstrip()
#     find = re.findall(patern, line)
#     if find:
#         print(line)
find = re.findall(patern, line)
if find:
    print(line)

'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
'''