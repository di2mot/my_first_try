# Програма декодирует используя подстановочный шифр
dict_1 = input()
dict_2 = input()
decode_1 = input()
decode_2 = input()
fin_decod_1, fin_decod_2 = '', ''
for a in decode_1:
    for i in range(len(dict_1)):
        if a == dict_1[i]:
            a = dict_2[i]
            break
    fin_decod_1 += a
for a in decode_2:
    for i in range(len(dict_2)):
        if a == dict_2[i]:
            a = dict_1[i]
            break
    fin_decod_2 += a
print(fin_decod_1)
print(fin_decod_2)
