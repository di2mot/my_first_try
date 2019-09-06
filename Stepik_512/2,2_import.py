from datetime import date, timedelta

a, b, c =  input().split()

d1 = date(year = int(a), month = int(b), day = int(c))
d2 = timedelta(days = int(input()))

d3 = str(d1 + d2)
y = d3.split('-')
print(int(y[0]), int(y[1]), int(y[2]))
print(d3.year, d3.month, d3.day)