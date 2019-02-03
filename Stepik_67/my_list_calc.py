b, a = 0, input().split()
if len(a) == 1:
    print(int(a[0]))
else:
    for i in range(0, len(a)):
        if i == len(a) - 1:
            b = int(a[0]) + int(a[i - 1])
        else:
            b = int(a[i - 1]) + int(a[i + 1])
        print(b, end=" ")
