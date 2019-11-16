import sys
import re

patern = r'cat'
for line in sys.stdin:
    line = line.rstrip()
    find = re.findall(patern, line)
    if len(find) >= 2:
        print(line)
    # process line

'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

'''