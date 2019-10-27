import re
# s = 'ababaaba'
# t = 'aba'
s = str(input())
t = str(input())
print(len(re.findall(f'(?={t})', s)))