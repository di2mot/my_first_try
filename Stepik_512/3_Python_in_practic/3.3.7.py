import sys
import re

patern = r'\b[aA]+\b'
repl = 'argh'
line = 'There’ll be no more "Aaaaaaaaaaaaaaa" aaaa'
for line in sys.stdin:
    line = line.rstrip()
    find = re.sub(patern, repl, line, 1)
    print(find)
# find = re.sub(patern, repl, line, 1)
# print(find)

'''
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
'''