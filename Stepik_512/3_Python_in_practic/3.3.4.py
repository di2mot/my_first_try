import sys
import re

patern = r'\\'
line = '\w'
# for line in sys.stdin:
#     line = line.rstrip()
#     find = re.findall(patern, line)
#     if find:
#         print(line)
find = re.findall(patern, line)
if find:
    print(line)