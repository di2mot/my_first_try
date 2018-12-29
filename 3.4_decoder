# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию,
# получая исходный текст.


with open('D:\\1.txt') as file:
    read = file.readline().strip()
number, j, symbol, res = 0, 0, '', ''
while j < len(read):
    symbol = read[j]
    if j != (len(read) - 2) and read[j + 1].isdigit() and read[j + 2].isdigit():
        number = int(read[j + 1] + read[j + 2])
        j += 3
    elif read[j + 1].isdigit():
        number = int(read[j + 1])
        j += 2
    res += symbol * number
    print(symbol * number, end='')
with open('D:\\2.txt', 'w') as ouf:
    ouf.write(res)
    
# А такперь как это правильно делать:

import re                         ﻿#подгрузил библиотеку с регулярными выражениями, рекомендую прочитать статью 
                                  ﻿#https://tproger.ru/translations/regular-expression-python/﻿
vyvod=''  ﻿                        #объявил пустую строку в которую в конце буду все записывать
with open("dataset_3363_2.txt") as file:   #открываю файл
  line = file.readline().strip()           #читаю строку
bukvi = re.findall(r'\D', line)            #re.findall находит все сочетания до цифры и помещает их в список в                                            #виде ('a', 'A', 'c'...) ﻿﻿ 
                                           #\﻿d - ﻿Любая цифра [0-9] (\D — все, кроме цифры)﻿﻿ ﻿
cifri = re.findall(r'\d+', line)           #\d ﻿﻿находит все сочетания цифр, а остальные пропускает, но чтобы он не
                                           #оставлял пробелы вместо пропущенных букв написано '\d+' - где + 
﻿                                          ﻿ #обозначает 1 и ﻿более вхождений цифр (по умолчанию, как я понял 0 и
                                           #более вхождений)﻿  
﻿for i in range(len(bukvi)):                #поскольку букв и сочетаний цифр одинаковое количество, то цикл
                                           #﻿имеет ﻿одинаковую длину (len(bukvi)) как для цифр, так и для букв   
    vyvod+= str(bukvi[i])*int(cifri[i])    #каждую букву записываю в ﻿строку определенное количество раз
with open("textfile_out.txt", "w") as outfile: outfile.write(vyvod) #записываю в файл



s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')




import re
with open('dataset_3363_2.txt', "r") as input_s:
  a = re.split('(\d+)', input_s.readline())
  b = (''.join(i[1] * int(i[0]) for i in zip(a[1::2], a[::2])))
  with open("3.4.3.txt", "w") as out_s:
    out_s.write(b)
    
 
 
import re          #  модуль регулярных выражений
with open("encode.txt") as f:    # откроем файл с кодированной строкой
    lst=re.findall(r'\D\d*', f.read()) # распарсить все группы ("буквачисло") как элементы списка
    strn=""
    for el in lst:         #  каждый элемент списка ("буквачисло") 
        strn+=el[0]*int(el[1:])    # повторить 1й символ("буква")   "число" раз и присоединить к строке

with open("decode.txt", "w") as wf:  # пишем раскодированную строку в файл 
    wf.write(strn)
