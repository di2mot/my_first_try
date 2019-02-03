n_start, n_end, n_1, n_2 = int(input()), int(input()), int(input()), int(input())
print( '   ', *range(n_1, n_2 + 1), sep = "\t")
for i in range(n_start, n_end + 1):
    print(i, end = " ")
    for k in range(n_1, n_2 + 1):
    	print('\t', i * k, end = " ")
    print()
