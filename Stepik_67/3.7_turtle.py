coordinates = {'север':0, 'юг':0, 'запад':0, 'восток':0,}
for i in range(int(input())):
    way = input().split()
    coordinates[way[0]] += int(way[1])
a = int(coordinates['север']) - int(coordinates['юг'])
b = int(coordinates['восток']) - int(coordinates['запад'])
print(b, a)

