import csv

FILENAME = "Crimes.csv"
primary_type = set()
primary_list = list()
max_len = 0

'''Тут вроде всё ясноБ просто добавляю все 'Primary Type' в список'''

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        primary_list.append(row['Primary Type'])

'''Множества уникальные, по этому формирую спосиок 'Primary Type' '''

primary_type = set(primary_list)

'''Перебираю сколько 'Primary Type' встречается в  primary_list'''

for crime_type in primary_type:
    count = primary_list.count(crime_type)
    if int(count) >= int(max_len):
        name = crime_type
        max_len = count
print(name)


