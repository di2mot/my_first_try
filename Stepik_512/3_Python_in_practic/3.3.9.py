import re

patern_1 = r'(\w)\1+'
patern_2 = r'\1'

line = 'Theree mannny woords'
# #
# for line in sys.stdin:
#     line = line.rstrip()
#     find = re.sub(patern_1, patern_2, line)
#     print(find)
find = re.sub(patern_1, patern_2, line)
print(line)
print(find)