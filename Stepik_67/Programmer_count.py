a = str(input())
b = int(a)
# Как математик я плох, по этому решил по другому. Я проверял окончание строчки на нужный патерн
# Тут я сверял строку на наличие в конце символа 1, кроме числа 11
if a == '1' or (a[1:2] == '1' and b < 100 and b != 11) or (a[1:2] != '1' and a[2:3] == '1'):
  print(b, 'программист')
 # Тут шла проверка на числа 2, 3, 4, кроме 11, 12, 13, 111, 212, 513 и т.д.
elif (a == '2' or a == '3' or a == '4' or ((a[1:2] == '2' or a[1:2] == '3' or a[1:2] == '4') and a[1:1] != '1' and b < 100) or
  ((a[2:3] == '2' or a[2:3] == '3' or a[2:3] == '4') and a[1:2] != '1')):
  print(b, "программиста")
# Тут всё что оканчивается на "0", т.е. 0, 10, 20, 100, 220, 570 и т.д.
elif a == '0' or (a[1:2] == '0' and b < 100) or a[2:3] == 0:
  print(b, "программистов")
# А тут всё что не попало и на всяк случай
else:
  print(b, 'программистов')
