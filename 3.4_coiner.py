text = open("D:\\1.txt", 'r')
s = text.read().replace('\n', ' ').lower().split()
text.close()
max_i, max_str = 0, ''
for i in s:
    if s.count(i) > max_i:
        max_i = s.count(i)
        max_str = i
print(max_str, max_i)




