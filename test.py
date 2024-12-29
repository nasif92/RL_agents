alist = [[" "] * 3 for _ in range(3)]


alist[0][0] = "A"
alist[0][1] = "B"
alist[0][2] = "X"


alist[0][0] = "Z"
alist[1][0] = "Z"
alist[2][0] = "Z"
# col
print(alist[:][0])

print(alist)
for row in alist:
	print(" | ".join(row))


