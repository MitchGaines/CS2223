
B = ["E", "X", "A", "M", "P", "L", "E"]

print(*B, sep=' ')
i = 0
for i in range(0, len(B) - 1):
    min = i

    for j in range(i+1, len(B)):
        if B[j] < B[min]:
            min = j

    B[i], B[min] = B[min], B[i]
    print(*B, sep=' ')