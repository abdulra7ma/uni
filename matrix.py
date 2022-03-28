n = int(input())
m = int(input())

matrix = []

for _n in range(n):
	sub_matrix = []
	for _m in range(1, m+1):
		if _m % 2 == 0:
			sub_matrix.append(1)
		else:
			sub_matrix.append(0)
	matrix.append(sub_matrix)
print(matrix)
		
