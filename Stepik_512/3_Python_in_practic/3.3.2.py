import sys
import re

patern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    find = re.search(patern, line)
    if find is not None:
        print(line)

'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

'''