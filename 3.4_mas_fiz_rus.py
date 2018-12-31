text = open("D:\\1.txt", 'r', encoding='utf-8')
s = text.read().replace('\n', ' ').split()
sum_mass, sum_fiz, sum_rus = 0, 0, 0
out_ = open('D:\\2.txt' , 'w')
for i in s:
    i = i.split(';')
    mass = int(i[1])
    fiz = int(i[2])
    rus = int(i[3])
    sum_mass += mass
    sum_fiz += fiz
    sum_rus += rus
    print(round((mass + fiz + rus) / 3, 9), file=out_)
print(round(sum_mass/len(s), 9), round(sum_fiz/len(s), 9), round(sum_rus/len(s), 9), end=' ', file = out_)






