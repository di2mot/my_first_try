import sys
import re

patern = r"\b((\w+|\d+)\2)\b"

for line in sys.stdin:
    line = line.rstrip()
    find = re.findall(patern, line)
    if find:
        print(line)

'''
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
'''