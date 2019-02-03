school_dict = {a:0 for a in range(1, 12)}
school_dict_1 = {a:0 for a in range(1, 12)}
with open('D:\\1.txt') as inf:
    for line in inf:
        line = line.split()
        key = int(line[0])
        school_dict[key] = float(school_dict[key] + int(line[2]))
        school_dict_1[key] += 1
for i in school_dict:
    if school_dict[i] == 0:
        print(i, '-')
    else:
        print(i, school_dict[i]/school_dict_1[i])