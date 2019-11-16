import sys


repl_in = 'human'
repl_on = 'computer'

for inp_text in sys.stdin:
    inp_text = inp_text.rstrip()
    inp_text = inp_text.replace(repl_in, repl_on)
    print(inp_text)

'''
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
'''