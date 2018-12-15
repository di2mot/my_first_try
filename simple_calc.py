# +, -, /, *, mod, pow, div
a = float(input())
b = float(input())
x = input()
if x == '+':
  print(a + b)
  
elif x == '-':
    print(a - b)
    
elif x == '/' and b != 0:
    print(a / b)
    
elif x == '*':
    print(a * b)
    
elif x == 'mod'  and b != 0:
    print(a % b)
    
elif x == 'pow':
    print(a ** b)
    
elif x == 'div'  and b != 0:
    print(a // b)
    
else:
  print("Деление на 0!")
